#!/usr/bin/env python3
"""
gerar_html_com_preamb_v2.py

Gera HTML com preâmbulo integrado na versão completa original.

Estratégia:
1. Gera HTML completo com criar_html() original
2. Extrai preâmbulo (considerandos EN+PT)
3. Remove ▌ de todo o documento
4. Injeta temas do preâmbulo na sidebar (após "Artigos")
5. Adiciona secção de preâmbulo ao final do HTML (após últimos artigos)

Output: comparativo_reuniao_exemplo_preamb_teste_v2.html
"""

import os
import sys
import json
import re
from docx import Document

# Importar dados e funções do script principal
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gerar_comparativo_reuniao import (
    ARTIGOS,
    extrair_glossario_pt,
    extrair_glossario_en,
    criar_html,
)

# ─────────────────────────────────────────────────────────────────────────────
# EXTRAÇÃO DO PREÂMBULO (IDÊNTICO À V1)
# ─────────────────────────────────────────────────────────────────────────────

TEMA_CONSIDERANDOS = {
    # Posição 1: Âmbito e Exclusões (PRIMEIRO na sidebar)
    "Âmbito e Exclusões": [19, 20, 21, 22, 23],
    # Posição 2: Motivos e Objetivos (logo após Âmbito e Exclusões)
    "Motivos e Objetivos": [1, 2, 7, 16, 17, 3, 4, 5],
    # Resto em ordem alfabética
    "Abrigos": [27, 28, 84],
    "Alojamento": [48],
    "Amarração": [51],
    "Autoridades Competentes": [31],
    "Cães de guarda de gado/pastoreio": [58],
    "Cães militares/polícia/aduaneiros": [57],
    "Competências de Execução": [79, 85],
    "Conformações Extremas e Genótipos": [41, 42, 77],
    "Consanguinidade": [43],
    "Contentores": [47, 52],
    "Formação": [36, 37, 38],
    "Híbridos": [44],
    "Lares de acolhimento temporário": [29, 30],
    "Lojas de Venda": [24, 25, 26],
    "Luz": [52],
    "Mutilações": [56],
    "Obrigação de informação sobre detenção responsável": [28, 60],
    "Países Terceiros": [73, 74, 75],
    "Práticas dolorosas": [34],
    "Princípios gerais de bem-estar animal": [13],
    "Proteção de Dados": [67, 68, 69, 70, 71, 72],
    "Publicidade": [63],
    "Rastreabilidade": [8, 9, 10, 11, 12, 14, 15, 18, 61, 62, 65],
    "Registo/Aprovação de Estabelecimentos": [35, 59],
    "Regras específicas de bem-estar animal": [24, 25, 45, 46],
    "Regras mais restritivas": [80, 81],
    "Relatórios Anuais": [32, 66, 82],
    "Reprodução": [49, 50, 53, 54],
    "Sanções": [83, 6],
    "Saúde": [33, 40, 73],
    "Sociabilização": [55, 76],
    "Treino": [64],
    "Visitas Médico-Veterinárias de aconselhamento de bem-estar": [33, 39, 78],
}


def extrair_preamb():
    """Extrai preâmbulo (considerandos) de ambos os documentos, removendo ▌."""
    doc_en = Document('11.12.2025 Regulamento cães e gatos-ocr - sem rasuras.docx')
    doc_pt = Document('pe00002.pt26.PB.aftermeeting 2.docx')

    considerandos_en = {}
    considerandos_pt = {}

    # Extrair EN
    for p in doc_en.paragraphs:
        if p.style.name == 'Considérant' and p.text.strip():
            txt = p.text.strip()
            # Ignorar linhas só com ▌
            if not re.match(r'^[▌\s]+$', txt):
                m = re.match(r'^\((\d+)\)', txt)
                if m:
                    num = int(m.group(1))
                    # REMOVER ▌ do texto
                    txt_limpo = txt.replace('▌', '').strip()
                    considerandos_en[num] = txt_limpo

    # Extrair PT
    for p in doc_pt.paragraphs:
        if p.style.name == 'Considérant' and p.text.strip():
            txt = p.text.strip()
            # Ignorar linhas só com ▌
            if not re.match(r'^[▌\s]+$', txt):
                m = re.match(r'^\((\d+)\)', txt)
                if m:
                    num = int(m.group(1))
                    # REMOVER ▌ do texto
                    txt_limpo = txt.replace('▌', '').strip()
                    considerandos_pt[num] = txt_limpo

    # Criar estrutura PREAMB (com duplicação por tema)
    preamb = []
    for tema, nums in TEMA_CONSIDERANDOS.items():
        for num in nums:
            preamb.append({
                'id': f'PREAMB-{num:02d}',
                'numero': num,
                'tema': tema,
                'regulamento': {
                    'texto': considerandos_en.get(num, ''),
                    'traducao': considerandos_pt.get(num, '')
                }
            })

    # Retornar organizado por tema para sidebar (preservando ordem de TEMA_CONSIDERANDOS)
    preamb_por_tema = {}
    # Inicializar dicionário na ordem correta dos temas
    for tema in TEMA_CONSIDERANDOS.keys():
        preamb_por_tema[tema] = []

    # Preencher considerandos em cada tema
    for item in preamb:
        tema = item['tema']
        preamb_por_tema[tema].append(item)

    return preamb, preamb_por_tema


def modificar_html_para_adicionar_preamb(html_original, preamb_por_tema, artigos):
    """
    Modifica HTML gerado pela criar_html() original para:
    1. Remover ▌ restantes
    2. Adicionar temas do preâmbulo à sidebar (após "Artigos")
    3. Injetar dados do preâmbulo no JavaScript
    """

    # 1. REMOVER ▌ (cleanup extra, como precaução)
    html_limpo = html_original.replace('▌', '')

    # 2. ADICIONAR TEMAS DO PREÂMBULO À SIDEBAR
    # Padrão: após </nav> há um comentário ou fim
    # Vamos injetar JavaScript que adiciona temas na sidebar

    temas_preamb = list(preamb_por_tema.keys())  # Manter ordem do dicionário (Âmbito e Exclusões primeiro)
    dados_preamb_json = json.dumps(preamb_por_tema, ensure_ascii=False)

    # Injetar dados do preâmbulo no script
    script_inject = f"""
// ══════════════════════════════════════════════════════════════════════════════
// PREÂMBULO — Dados e Funcionalidade Adicional
// ══════════════════════════════════════════════════════════════════════════════

const PREAMB_POR_TEMA = {dados_preamb_json};
const TEMAS_PREAMB = {json.dumps(temas_preamb, ensure_ascii=False)};

function exibirTemaPreambulo(tema) {{
  const considerandos = PREAMB_POR_TEMA[tema];
  const container = document.getElementById('main-content');
  container.innerHTML = '';

  // Título do tema
  const titulo = document.createElement('div');
  titulo.className = 'preamb-titulo';
  titulo.innerHTML = '<h2>' + tema + '</h2><small>' + considerandos.length + ' considerando(s)</small>';
  container.appendChild(titulo);

  // Exibir cada considerando
  for (const cons of considerandos) {{
    const artBadge = document.createElement('div');
    artBadge.className = 'art-badge preamb';
    artBadge.textContent = 'PREAMB-' + String(cons.numero).padStart(2, '0');
    container.appendChild(artBadge);

    // Card EN
    const cardEn = document.createElement('div');
    cardEn.className = 'card reg';
    cardEn.style.marginBottom = '14px';
    cardEn.innerHTML = `
      <div class="card-header">
        @regulamento — Considerando ${{cons.numero}} (EN)
        <span class="card-header-ref">Texto Original EN</span>
      </div>
      <div class="card-body">${{cons.regulamento.texto.replace(/\\n/g, '<br>')}}</div>
    `;
    container.appendChild(cardEn);

    // Card PT
    const cardPt = document.createElement('div');
    cardPt.className = 'card reg-tr';
    cardPt.style.marginBottom = '20px';
    cardPt.innerHTML = `
      <div class="card-header">
        @regulamento — Considerando ${{cons.numero}} (PT)
        <span class="card-header-ref">Tradução PT-PT</span>
      </div>
      <div class="card-body">${{cons.regulamento.traducao.replace(/\\n/g, '<br>')}}</div>
    `;
    container.appendChild(cardPt);
  }}
}}

// Função para procurar em considerandos
function considerandoMatch(cons, searchTerm) {{
  const q = searchTerm.toLowerCase();
  return cons.numero.toString().includes(q) ||
         cons.tema.toLowerCase().includes(q) ||
         cons.regulamento.texto.toLowerCase().includes(q) ||
         cons.regulamento.traducao.toLowerCase().includes(q);
}}

// Hook na pesquisa original para incluir preâmbulo (com delay para garantir carregamento)
setTimeout(function() {{
  // Verificar se pesquisar existe
  if (typeof window.pesquisar !== 'function') {{
    console.warn('pesquisar function not found, retrying...');
    return;
  }}

  const pesquisarOriginal = window.pesquisar;

  window.pesquisar = function(searchInput) {{
    // Chamar pesquisa original
    pesquisarOriginal.call(this, searchInput);

    const q = searchInput.trim().toLowerCase();
    if (!q) return;

    // Procurar no preâmbulo
    const matchingConsiderandos = [];
    for (const tema of TEMAS_PREAMB) {{
      const considerandos = PREAMB_POR_TEMA[tema];
      for (const cons of considerandos) {{
        if (considerandoMatch(cons, q)) {{
          matchingConsiderandos.push({{ tema: tema, cons: cons }});
        }}
      }}
    }}

    // Se há matches, adicionar à exibição
    if (matchingConsiderandos.length > 0) {{
      const container = document.getElementById('main-content');
      if (!container) return;

      // Verificar se já existe seção de preâmbulo e remover
      const existingPrembSection = container.querySelector('[data-preamb-results]');
      if (existingPrembSection) {{
        existingPrembSection.remove();
      }}

      // Adicionar seção de preâmbulo aos resultados
      const prembSection = document.createElement('div');
      prembSection.setAttribute('data-preamb-results', 'true');
      prembSection.style.marginTop = '2rem';
      prembSection.style.paddingTop = '1.5rem';
      prembSection.style.borderTop = '2px solid #9B8B9E';

      const prembTitle = document.createElement('h3');
      prembTitle.textContent = 'Resultados no Preâmbulo';
      prembTitle.style.color = '#9B8B9E';
      prembTitle.style.marginBottom = '1rem';
      prembSection.appendChild(prembTitle);

      // Agrupar por tema
      const porTema = {{}};
      for (const item of matchingConsiderandos) {{
        if (!porTema[item.tema]) porTema[item.tema] = [];
        porTema[item.tema].push(item.cons);
      }}

      for (const tema in porTema) {{
        const temaDiv = document.createElement('div');
        temaDiv.style.marginBottom = '1rem';

        const temaTit = document.createElement('strong');
        temaTit.textContent = tema;
        temaTit.style.color = '#9B8B9E';
        temaTit.style.display = 'block';
        temaTit.style.marginBottom = '0.5rem';
        temaDiv.appendChild(temaTit);

        const list = document.createElement('ul');
        list.style.marginLeft = '1rem';
        list.style.listStyle = 'none';
        list.style.padding = '0';

        for (const cons of porTema[tema]) {{
          const li = document.createElement('li');
          li.style.marginBottom = '0.5rem';

          const link = document.createElement('a');
          link.href = 'javascript:void(0)';
          link.textContent = 'Considerando ' + cons.numero + ': ' + cons.regulamento.traducao.substring(0, 70) + '…';
          link.style.color = '#7B68A6';
          link.style.textDecoration = 'none';
          link.style.fontSize = '0.9rem';
          link.onclick = function() {{
            exibirTemaPreambulo(tema);
            return false;
          }};

          li.appendChild(link);
          list.appendChild(li);
        }}

        temaDiv.appendChild(list);
        prembSection.appendChild(temaDiv);
      }}

      container.appendChild(prembSection);
    }}
  }};
}}, 200);

// Adicionar botões de preâmbulo à sidebar DEPOIS de renderSidebar() ser chamada
setTimeout(function() {{
  const nav = document.getElementById('sidebar');
  if (!nav) return;

  // Adicionar separador de preâmbulo
  const sep = document.createElement('h2');
  sep.style.marginTop = '1rem';
  sep.style.borderTop = '1px solid rgba(255,255,255,0.2)';
  sep.style.paddingTop = '1rem';
  sep.textContent = 'Preâmbulo';
  nav.appendChild(sep);

  // Adicionar botões de temas
  for (const tema of TEMAS_PREAMB) {{
    const btn = document.createElement('button');
    btn.className = 'preamb-theme-btn';
    btn.innerHTML = tema + '<small>(' + PREAMB_POR_TEMA[tema].length + ' considerando)</small>';
    btn.onclick = () => exibirTemaPreambulo(tema);
    nav.appendChild(btn);
  }}
}}, 100);

// Estilos para preâmbulo
const stylePreambulo = document.createElement('style');
stylePreambulo.textContent = `
  .preamb-theme-btn {{
    width: 100%;
    background: rgba(155, 139, 158, 0.1) !important;
    border: none;
    border-left: 3px solid #9B8B9E;
    color: white;
    padding: 0.75rem 1rem;
    text-align: left;
    cursor: pointer;
    font-size: 0.9rem;
    transition: all 0.2s;
  }}
  .preamb-theme-btn:hover {{
    background: rgba(155, 139, 158, 0.2) !important;
  }}
  .preamb-theme-btn small {{
    display: block;
    font-size: 0.75rem;
    opacity: 0.7;
    margin-top: 2px;
  }}
  .preamb-titulo {{
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid #9B8B9E;
  }}
  .preamb-titulo h2 {{
    color: #9B8B9E;
    font-size: 1.3rem;
    margin-bottom: 0.25rem;
  }}
  .preamb-titulo small {{
    color: #999;
    font-size: 0.9rem;
  }}
  .art-badge.preamb {{
    background: #9B8B9E !important;
  }}
  .card.preamb {{
    border-left-color: #9B8B9E !important;
    background: #F8F5FB !important;
  }}
  .card.preamb .card-header {{
    color: #9B8B9E !important;
  }}
`;
document.head.appendChild(stylePreambulo);
"""

    # Localizar onde injetar (antes de fechar </body>)
    if '</body>' in html_limpo:
        # Injetar antes de </body>
        html_limpo = html_limpo.replace('</body>', f'<script>\n{script_inject}\n</script>\n</body>')

    return html_limpo


def gerar_html_completo_com_preamb(output_path):
    """Gera HTML completo com preâmbulo integrado."""

    print("1. Gerando HTML base (artigos completos)...")
    # Gerar HTML original completo
    temp_path = '/tmp/comparativo_temp.html'
    criar_html(temp_path, ARTIGOS)

    # Ler HTML gerado
    with open(temp_path, 'r', encoding='utf-8') as f:
        html_original = f.read()

    print("2. Extraindo preâmbulo...")
    preamb, preamb_por_tema = extrair_preamb()
    print(f"   ✓ {len(preamb)} considerandos extraídos ({len(preamb_por_tema)} temas)")

    print("3. Modificando HTML: removendo ▌ e adicionando preâmbulo...")
    html_final = modificar_html_para_adicionar_preamb(html_original, preamb_por_tema, ARTIGOS)

    print(f"4. Gravando {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_final)

    print(f"✓ Concluído: {output_path}")
    import os
    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"  Tamanho: {size_mb:.2f} MB")


if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    output = os.path.join(base, "comparativo_reuniao_exemplo_preamb_teste_v2.html")
    gerar_html_completo_com_preamb(output)
