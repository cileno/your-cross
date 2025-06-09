#!/bin/bash
echo "🧪 Gerando SVG do Mermaid..."
mmdc -i docs/tech/diagramas/arquitetura_backend.mmd -o docs/tech/diagramas/arquitetura_backend.svg

if [ $? -eq 0 ]; then
  echo "✅ Diagrama gerado com sucesso!"
else
  echo "❌ Falha ao gerar o diagrama."
fi