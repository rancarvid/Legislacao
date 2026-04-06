#!/usr/bin/env python3
"""
Gera documento HTML com disposições novas do Regulamento 2023/0447
que não têm correspondência na legislação portuguesa.
"""

import csv
from collections import defaultdict
from html import escape

# Ler CSV
disposicoes = []
with open('/tmp/disposicoes_novas_regulamento.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['artigo'].strip() and row['artigo'].strip().isdigit():
            disposicoes.append(row)

# Agrupar por categoria
por_categoria = defaultdict(list)
categorias_ordem = []
for disp in disposicoes:
    cat = disp['categoria_novidade']
    if cat not in por_categoria:
        categorias_ordem.append(cat)
    por_categoria[cat].append(disp)

# Gerar HTML
html = """<!DOCTYPE html>
<html lang="pt-PT">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Disposições Novas — Regulamento 2023/0447</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', Tahoma, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
        }
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 3rem 2rem;
            text-align: center;
        }
        header h1 { font-size: 2.2rem; margin-bottom: 0.5rem; }
        header p { font-size: 1.1rem; opacity: 0.9; }
        
        .container { max-width: 1100px; margin: 0 auto; padding: 2rem; }
        
        .indice {
            background: white;
            border-radius: 8px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .indice h2 { color: #667eea; margin-bottom: 1rem; font-size: 1.4rem; }
        .indice a {
            display: inline-block;
            margin: 0.5rem 1rem 0.5rem 0;
            padding: 0.75rem 1.5rem;
            background: #f0f0f0;
            color: #667eea;
            text-decoration: none;
            border-radius: 20px;
            transition: all 0.3s;
        }
        .indice a:hover { background: #667eea; color: white; }
        
        .categoria {
            margin-bottom: 3rem;
            scroll-margin-top: 100px;
        }
        .categoria-titulo {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border-left: 5px solid #667eea;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-radius: 4px;
        }
        .categoria-titulo h2 {
            color: #667eea;
            font-size: 1.6rem;
            margin-bottom: 0.3rem;
        }
        .categoria-titulo .count {
            color: #999;
            font-size: 0.9rem;
        }
        
        .artigo-card {
            background: white;
            border-radius: 8px;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            overflow: hidden;
            transition: all 0.3s;
        }
        .artigo-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.12); }
        
        .artigo-header {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
            padding: 1.5rem;
            border-bottom: 1px solid #eee;
            cursor: pointer;
            user-select: none;
        }
        .artigo-header:hover { background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%); }
        
        .artigo-numero {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 0.4rem 0.8rem;
            border-radius: 4px;
            font-weight: bold;
            margin-right: 1rem;
            font-size: 0.9rem;
        }
        .artigo-titulo {
            font-size: 1.3rem;
            color: #333;
            font-weight: 500;
            display: inline-block;
        }
        .artigo-toggle {
            float: right;
            font-size: 1.4rem;
            color: #667eea;
        }
        
        .artigo-corpo {
            padding: 1.5rem;
            display: none;
        }
        .artigo-corpo.expanded { display: block; }
        
        .secao {
            margin-bottom: 1.5rem;
        }
        .secao-titulo {
            font-weight: bold;
            color: #667eea;
            margin-bottom: 0.5rem;
            font-size: 0.95rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .secao-conteudo {
            background: #f9f9f9;
            padding: 1rem;
            border-left: 3px solid #667eea;
            border-radius: 4px;
            line-height: 1.7;
            font-size: 0.95rem;
        }
        
        .texto-en {
            font-style: italic;
            color: #555;
            border-left-color: #764ba2;
        }
        
        .achados-pt {
            border-left-color: #f39c12;
        }
        
        .por-que-novo {
            background: #fff3cd;
            border-left-color: #ffc107;
        }
        
        footer {
            text-align: center;
            padding: 2rem;
            color: #999;
            font-size: 0.9rem;
        }
        
        .badge {
            display: inline-block;
            background: #f0f0f0;
            padding: 0.3rem 0.8rem;
            border-radius: 12px;
            font-size: 0.8rem;
            color: #667eea;
            margin-right: 0.5rem;
            font-weight: 500;
        }
    </style>
</head>
<body>
    <header>
        <h1>🔍 Disposições Novas — Regulamento 2023/0447</h1>
        <p>Artigos e normas sem correspondência na legislação portuguesa vigente</p>
    </header>
    
    <div class="container">
        <div class="indice">
            <h2>Índice de Categorias</h2>
"""

# Adicionar links do índice
for cat in categorias_ordem:
    cat_id = cat.replace(' ', '-').replace('/', '-').lower()
    count = len(por_categoria[cat])
    html += f'<a href="#{cat_id}">{cat} ({count})</a>\n'

html += """
        </div>
"""

# Adicionar artigos por categoria
for cat in categorias_ordem:
    cat_id = cat.replace(' ', '-').replace('/', '-').lower()
    artigos = por_categoria[cat]
    
    html += f"""
        <div class="categoria" id="{cat_id}">
            <div class="categoria-titulo">
                <h2>{escape(cat)}</h2>
                <span class="count">{len(artigos)} artigo(s)</span>
            </div>
"""
    
    for disp in artigos:
        art_num = disp['artigo'].strip()
        titulo = disp['titulo'].strip()
        por_que = disp['por_que_novo'].strip()
        achados = disp['achados_legislacao_pt'].strip()
        texto = disp['texto_en_resumido'].strip()
        
        html += f"""
            <div class="artigo-card">
                <div class="artigo-header" onclick="this.nextElementSibling.classList.toggle('expanded'); this.querySelector('.artigo-toggle').textContent = this.nextElementSibling.classList.contains('expanded') ? '▼' : '▶';">
                    <span class="artigo-numero">ART. {art_num}</span>
                    <span class="artigo-titulo">{escape(titulo)}</span>
                    <span class="artigo-toggle">▶</span>
                </div>
                <div class="artigo-corpo">
                    <div class="secao">
                        <div class="secao-titulo">ℹ️ Por que é novo:</div>
                        <div class="secao-conteudo por-que-novo">{escape(por_que)}</div>
                    </div>
                    
                    <div class="secao">
                        <div class="secao-titulo">📋 O que existe em Portugal:</div>
                        <div class="secao-conteudo achados-pt">{escape(achados)}</div>
                    </div>
                    
                    <div class="secao">
                        <div class="secao-titulo">📝 Texto do Regulamento (EN — resumido):</div>
                        <div class="secao-conteudo texto-en">{escape(texto)}</div>
                    </div>
                </div>
            </div>
"""
    
    html += "        </div>\n"

html += """
    </div>
    
    <footer>
        <p>Análise comparativa de disposições novas — Regulamento (UE) 2023/0447 vs. legislação portuguesa</p>
        <p>Gerado em 6 de abril de 2026</p>
    </footer>
</body>
</html>
"""

# Salvar
with open('disposicoes_novas_regulamento.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Documento gerado: disposicoes_novas_regulamento.html")
print(f"   - {len(disposicoes)} artigos analisados")
print(f"   - {len(categorias_ordem)} categorias de novidade")
