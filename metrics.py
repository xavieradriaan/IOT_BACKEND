from prometheus_client import Counter, Gauge
from datetime import datetime

# Conteo simple por tipo de evento (entrada, salida)
biometric_counter = Counter(
    "biometric_events_total",
    "Total de eventos biométricos por tipo",
    ["event_type"]
)

# Conteo detallado por tipo, fecha y empleado
biometric_counter_by_date = Counter(
    "biometric_events_by_date_total",
    "Total de eventos biométricos por tipo, fecha y empleado",
    ["event_type", "date", "employee"]
)

# Métricas del ESP32
latency_gauge = Gauge("esp32_latency_ms", "Latencia del ESP32 en milisegundos")
uptime_gauge = Gauge("esp32_uptime_seconds", "Uptime del ESP32 en segundos")

def record_biometric_event(event_type, employee="unknown"):
    date_str = datetime.now().strftime('%Y-%m-%d')
    biometric_counter.labels(event_type=event_type).inc()
    biometric_counter_by_date.labels(
        event_type=event_type,
        date=date_str,
        employee=employee
    ).inc()
