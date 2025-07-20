from prometheus_client import Counter, Gauge

biometric_counter = Counter(
    "biometric_events_total",
    "Eventos biométricos totales",
    ["event_type"]
)
latency_gauge = Gauge("esp32_latency_ms", "Latencia del ESP32 en milisegundos")
uptime_gauge = Gauge("esp32_uptime_seconds", "Uptime del ESP32 en segundos")
