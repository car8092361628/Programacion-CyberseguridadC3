import socket

class PortScanner:
    def __init__(self, host, ports):
        self.host = host
        self.ports = ports
        self.open_ports = []

    def scan(self):
        print(f"🔍 Iniciando escaneo en {self.host}...")
        for port in self.ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((self.host, port))
            if result == 0:
                print(f"✅ Puerto {port} abierto")
                self.open_ports.append(port)
            sock.close()

    def report(self):
        print("\n📊 Resultados del escaneo:")
        if self.open_ports:
            for port in self.open_ports:
                print(f" - Puerto {port}: ABIERTO")
        else:
            print("No se encontraron puertos abiertos.")

# Definir host y puertos
host = "scanme.nmap.org"
puertos = [21, 22, 23, 25, 80, 443]

# Crear objeto y ejecutar
scanner = PortScanner(host, puertos)
scanner.scan()
scanner.report()
