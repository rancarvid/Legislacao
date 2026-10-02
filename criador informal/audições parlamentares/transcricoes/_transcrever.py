# -*- coding: utf-8 -*-
import sys, time, io, os
from faster_whisper import WhisperModel

src, out, modelo = sys.argv[1], sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "small")
m = WhisperModel(modelo, device="cpu", compute_type="int8", cpu_threads=4)
segs, info = m.transcribe(
    src, language="pt", vad_filter=True,
    vad_parameters=dict(min_silence_duration_ms=700),
    beam_size=5, condition_on_previous_text=False,
)
t0 = time.time()
n = 0
with io.open(out, "w", encoding="utf-8") as f:
    f.write("# Transcrição automática (faster-whisper %s, pt) — NÃO é transcrição oficial\n" % modelo)
    f.write("# Fonte: %s\n\n" % os.path.basename(src))
    for s in segs:
        mm, ss = divmod(int(s.start), 60)
        hh, mm = divmod(mm, 60)
        f.write("[%02d:%02d:%02d] %s\n" % (hh, mm, ss, s.text.strip()))
        n += 1
        if n % 40 == 0:
            f.flush()
            print("  %d segmentos | audio %.1f min | decorrido %.1f min" % (n, s.end/60, (time.time()-t0)/60), flush=True)
print("CONCLUIDO: %d segmentos em %.1f min -> %s" % (n, (time.time()-t0)/60, out), flush=True)
