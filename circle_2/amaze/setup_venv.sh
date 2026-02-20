#!/bin/bash

# Script para configurar el entorno virtual de Python

# Verificar si ya existe
if [ -d "venv" ]; then
    echo "⚠️  El entorno virtual ya existe."
    read -p "¿Deseas recrearlo? (y/N): " response
    response=${response:-n}
    if [[ ! "$response" =~ ^[yY]$ ]]; then
        echo "✓ Usando entorno virtual existente"
        exit 0
    fi
    echo "🗑️  Eliminando entorno virtual anterior..."
    rm -rf venv
fi

echo "🔧 Configurando entorno virtual..."

# Crear el entorno virtual
python3 -m venv venv
echo "✓ Entorno virtual creado"

# Activar el entorno virtual
source venv/bin/activate
echo "✓ Entorno virtual activado"

# Actualizar pip
pip install --upgrade pip > /dev/null 2>&1
echo "✓ pip actualizado"

# Instalar dependencias
pip install flake8 mypy build > /dev/null 2>&1
echo "✓ Dependencias instaladas (flake8, mypy, build)"

echo ""
echo "✅ Entorno virtual configurado exitosamente"
