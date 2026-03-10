#!/bin/bash
echo ""
echo " Comparativo Regulamento 2023/0447 - Cães e Gatos"
echo " ================================================"
echo " A iniciar servidor local na porta 8080..."
echo " Para terminar: Ctrl+C"
echo ""

python3 -m http.server 8080 &
SERVER_PID=$!
sleep 1

# Abrir browser (macOS ou Linux)
xdg-open "http://localhost:8080/comparativo_reuniao_exemplo.html" 2>/dev/null \
  || open "http://localhost:8080/comparativo_reuniao_exemplo.html" 2>/dev/null

wait $SERVER_PID
