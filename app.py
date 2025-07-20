from flask import Flask
from prometheus_client import start_http_server
from mqtt_client import start_mqtt

app = Flask(__name__)

# Iniciar cliente MQTT
start_mqtt()

# Iniciar servidor de métricas en puerto 5000
start_http_server(5000)

# (Opcional) Puedes dejar una ruta raíz viva si lo deseas:
@app.route('/')
def home():
    return "Servidor backend activo. Las métricas están en /metrics."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)  # Esto es opcional si quieres servir Flask también
