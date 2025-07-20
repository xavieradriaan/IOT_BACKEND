import os
import paho.mqtt.client as mqtt
from metrics import biometric_counter, latency_gauge, uptime_gauge
from dotenv import load_dotenv

load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))

def on_connect(client, userdata, flags, rc):
    print("MQTT conectado con código:", rc)
    client.subscribe("esp32/metrics")
    client.subscribe("iot/biometric")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    topic = msg.topic

    if topic == "esp32/metrics":
        try:
            parts = dict(x.split("=") for x in payload.split(";") if "=" in x)
            latency = float(parts.get("latencia", "0").replace("ms", ""))
            uptime = int(parts.get("uptime", "0"))
            latency_gauge.set(latency)
            uptime_gauge.set(uptime)
        except Exception as e:
            print("Error parseando métricas:", e)

    elif topic == "iot/biometric":
        print("Evento biométrico recibido:", payload)
        event_type = "unknown"
        if "tipo=" in payload:
            try:
                event_type = payload.split("tipo=")[1].split(";")[0]
            except Exception:
                pass
        biometric_counter.labels(event_type=event_type).inc()

def start():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_HOST, MQTT_PORT, 60)
    client.loop_start()
