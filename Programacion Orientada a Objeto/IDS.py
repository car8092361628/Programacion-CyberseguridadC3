class IntrusionDetectionSystem:
    def __init__(self):
        # Base de datos de patrones sospechosos
        self.threat_signatures = [
            "nmap", "sqlmap", "hydra", "masscan",
            "admin'--", "union select", "etc/passwd"
        ]
        self.alerts = []

    def analyze_traffic(self, packet_data):
        """
        Analiza el contenido del paquete para buscar patrones sospechosos
        """
        for signature in self.threat_signatures:
            if signature.lower() in packet_data.lower():
                alert_msg = f"⚠️ Alerta: patrón '{signature}' detectado en el tráfico."
                self.alerts.append(alert_msg)
                print(alert_msg)

    def report(self):
        """
        Muestra un resumen de las alertas detectadas
        """
        print("\n📊 Reporte de Intrusiones Detectadas:")
        if self.alerts:
            for alert in self.alerts:
                print(f" - {alert}")
        else:
            print("✅ No se detectaron amenazas.")
# Simulación de tráfico de red
# Crear instancia del sistema IDS
ids = IntrusionDetectionSystem()

# Simular tráfico de red (peticiones)
trafico = [
    "GET /index.html HTTP/1.1",
    "GET /login.php?user=admin'-- HTTP/1.1",
    "Running nmap scan...",
    "POST /data HTTP/1.1",
]

# Analizar cada paquete
for paquete in trafico:
    ids.analyze_traffic(paquete)

# Mostrar reporte
ids.report()
