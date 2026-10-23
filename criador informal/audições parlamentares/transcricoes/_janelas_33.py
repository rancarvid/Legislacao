# -*- coding: utf-8 -*-
"""Reprocessamento com medium das janelas relevantes da audição n.º 33-CAM-XIV."""
import time, io
from faster_whisper import WhisperModel

SRC = ("/home/user/Legislacao/criador informal/audições parlamentares/"
       "(Audio) 2020 07 30 - Animais Santo Tirso Audição Ministro da Admin. Interna "
       "e Ministra da Agricultura - Parlapier Político (360p, h264)_compressed.m4a")

JANELAS = [
    (1062, 1120, "A. GNR — estruturas ilegais identificadas 2018-2020"),
    (1302, 1425, "B. Ministra — alojamentos nunca registados; processo administrativo da DGAV; DL 116/98"),
    (6067, 6205, "C. Ministra — contraordenações de 2018, coima, relatorio do MVM, leitura do DL 116/98"),
    (6382, 6450, "D. Ministra — numero de alojamentos registados e demais estatistica"),
    (6807, 6870, "E. Deputado — decisoes nao executadas e o episodio da morada errada"),
    (6908, 6940, "F. Deputado — canis e gatis municipais sem comunicacao previa"),
    (8197, 8310, "G. Deputada — dados da ANMVM: decisao de encerramento de 2012 e a repartição de competências"),
    (8958, 8990, "H. Compromisso de apuramento nos 128 locais"),
]

m = WhisperModel("medium", device="cpu", compute_type="int8", cpu_threads=4)
print("modelo medium pronto", flush=True)
t0 = time.time()
with io.open("33-CAM-XIV_janelas-A-a-H_medium.txt", "w", encoding="utf-8") as f:
    f.write("# Transcricao automatica (faster-whisper medium, pt) das janelas relevantes\n")
    f.write("# Audicao n.o 33-CAM-XIV, Ministro da Administracao Interna e Ministra da Agricultura\n")
    f.write("# Comissao de Agricultura e Mar, 30.7.2020 — NAO e transcricao oficial\n\n")
    for a, b, rot in JANELAS:
        f.write("\n===== %s  [%02d:%02d:%02d - %02d:%02d:%02d] =====\n" %
                (rot, a//3600, (a % 3600)//60, a % 60, b//3600, (b % 3600)//60, b % 60))
        segs, _ = m.transcribe(SRC, language="pt", beam_size=5, vad_filter=False,
                               condition_on_previous_text=True,
                               clip_timestamps=[float(a), float(b)])
        for s in segs:
            hh, rem = divmod(int(s.start), 3600)
            mm, ss = divmod(rem, 60)
            f.write("[%02d:%02d:%02d] %s\n" % (hh, mm, ss, s.text.strip()))
        f.flush()
        print("janela %s concluida | decorrido %.1f min" % (rot[:1], (time.time()-t0)/60), flush=True)
print("CONCLUIDO em %.1f min" % ((time.time()-t0)/60), flush=True)
