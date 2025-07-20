from flask import Flask, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from mqtt_client import start as start_mqtt

app = Flask(__name__)
start_mqtt()

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
