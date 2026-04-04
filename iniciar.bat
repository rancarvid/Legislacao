@echo off
echo.
echo  Comparativo Regulamento 2023/0447 - Coes e Gatos
echo  ================================================
echo  A iniciar servidor local na porta 8080...
echo  Para terminar: fechar esta janela ou premir Ctrl+C
echo.
start "" "http://localhost:8080/comparativo_reuniao_exemplo.html"
python -m http.server 8080
