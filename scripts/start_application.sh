#!/bin/bash
cd /home/ubuntu/iot_backend_deploy
nohup python3 app.py > app.log 2>&1 &
