#!/bin/bash
set -e

cd /home/ubuntu/iot_backend_deploy

echo "==> Verificando instalación de Python3 y pip3"
which python3 || sudo apt-get install -y python3
which pip3 || sudo apt-get install -y python3-pip

echo "==> Refrescando paquetes y asegurando dependencias del sistema"
sudo DEBIAN_FRONTEND=noninteractive apt-get update -yq
sudo DEBIAN_FRONTEND=noninteractive apt-get install -yq python3-venv python3-dev build-essential

echo "==> Borrando entorno anterior (si existe)"
rm -rf venv

echo "==> Creando entorno virtual como usuario ubuntu"
python3 -m venv venv

echo "==> Instalando dependencias en entorno virtual"
./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r requirements.txt

echo "==> Instalación completada exitosamente"
