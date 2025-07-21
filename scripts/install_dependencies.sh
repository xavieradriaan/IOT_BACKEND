#!/bin/bash
cd /home/ubuntu/iot_backend_deploy
# Actualizar sistema e instalar Python3 y pip3 si no están
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv
# Instalar dependencias usando pip3
pip3 install -r requirements.txt
