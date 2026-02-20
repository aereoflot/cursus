#!/bin/bash

# Script de ayuda para activar el entorno virtual

if [ ! -d "venv" ]; then
    echo "⚠️  El entorno virtual no existe."
    echo "Ejecuta primero: make venv"
    exit 1
fi

echo "Activando entorno virtual..."
source venv/bin/activate

echo "✅ Entorno virtual activado"
echo ""
echo "Para desactivar, ejecuta: deactivate"
