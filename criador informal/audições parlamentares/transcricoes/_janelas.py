# -*- coding: utf-8 -*-
import time, io
from faster_whisper import WhisperModel
SRC = "/home/user/Legislacao/criador informal/audições parlamentares/(Audio) audicao-do-presidente-da-camara-municipal-de-santo-tirso_compressed v.2"
JANELAS = [(2040,2260,"A. Despacho DGAV 2012 e vistorias desde 2006"),
           (2590,2710,"B. Deputados sobre a inacção após 2012"),
           (2960,3100,"C. Competencia do diretor-geral e execucao municipal"),
           (3670,4180,"D. Defesa juridica do presidente e coimas urbanisticas")]
m = WhisperModel("medium", device="cpu", compute_type="int8", cpu_threads=4)
print("modelo medium pronto", flush=True)
t0=time.time()
with io.open("st_medium_janelas.txt","w",encoding="utf-8") as f:
    f.write("# Transcricao automatica (faster-whisper medium, pt) das janelas relevantes\n")
    f.write("# Audicao n.o 32-CAM-XIV, Comissao de Agricultura e Mar, 30.7.2020\n\n")
    for a,b,rot in JANELAS:
        f.write("\n===== %s  [%02d:%02d:%02d - %02d:%02d:%02d] =====\n" %
                (rot, a//3600,(a%3600)//60,a%60, b//3600,(b%3600)//60,b%60))
        segs,_ = m.transcribe(SRC, language="pt", beam_size=5, vad_filter=False,
                              condition_on_previous_text=True, clip_timestamps=[float(a),float(b)])
        for s in segs:
            hh,rem=divmod(int(s.start),3600); mm,ss=divmod(rem,60)
            f.write("[%02d:%02d:%02d] %s\n" % (hh,mm,ss,s.text.strip()))
        f.flush()
        print("janela %s concluida | decorrido %.1f min" % (rot[:1], (time.time()-t0)/60), flush=True)
print("CONCLUIDO em %.1f min" % ((time.time()-t0)/60), flush=True)
