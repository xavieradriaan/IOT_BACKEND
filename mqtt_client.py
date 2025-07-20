import os
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from metrics import (
    latency_gauge,
    uptime_gauge,
    record_biometric_event
)

load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST", "mqtt")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))

def on_connect(client, userdata, flags, rc):
    print(f"[MQTT] Conectado con código: {rc}")
    client.subscribe("esp32/metrics")
    client.subscribe("iot/biometric")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    topic = msg.topic
    print(f"[MQTT] Topic: {topic} | Payload: {payload}")

    if topic == "esp32/metrics":
        try:
            parts = dict(x.split("=") for x in payload.split(";") if "=" in x)
            latency = float(parts.get("latencia", "0").replace("ms", ""))
            uptime = int(parts.get("uptime", "0"))
            latency_gauge.set(latency)
            uptime_gauge.set(uptime)
        except Exception as e:
            print("[MQTT] Error parseando métricas:", e)

    elif topic == "iot/biometric":
        print("[BACKEND] Evento biométrico recibido:", payload)
        event_type = "unknown"
        employee = "desconocido"

        try:
            parts = payload.split(";")
            if len(parts) == 2:
                # Caso 1: Formato nuevo -> juan.perez;entrada=22:17:39
                if "=" in parts[1]:
                    employee = parts[0]
                    event_type = parts[1].split("=")[0]
                else:
                    # Caso 2: Formato antiguo -> empleadoB;entrada
                    employee = parts[0]
                    event_type = parts[1]
        except Exception as e:
            print("[MQTT] Error parseando evento biométrico:", e)

        record_biometric_event(event_type, employee=employee)

def start_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_HOST, MQTT_PORT, 60)
    client.loop_start()
