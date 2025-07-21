#!/bin/bash
set -e

cd /home/ubuntu/iot_backend_deploy

echo "==> Verificando instalación de Python3 y pip3"
which python3 || sudo apt-get install -y python3
which pip3 || sudo apt-get install -y python3-pip

echo "==> Refrescando paquetes y asegurando dependencias del sistema"
sudo DEBIAN_FRONTEND=noninteractive apt-get update -yq
sudo DEBIAN_FRONTEND=noninteractive apt-get install -yq python3-venv python3-dev build-essential

echo "==> Creando entorno virtual"
python3 -m venv venv

echo "==> Activando entorno virtual"
source venv/bin/activate

echo "==> Instalando dependencias del proyecto en entorno virtual"
pip install --upgrade pip
pip install -r requirements.txt

echo "==> Instalación completada exitosamente"
