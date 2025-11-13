import socket

class PortScanner: # clase para escanear puertos
    def __init__(self, host, ports): # funcion que recibe parametros
        self.host = host # atributo de la clase
        self.ports = ports # atributo de la clase
        self.open_ports = [] # lista para puertos abiertos

    def scan(self):
        print(f"🔍 Iniciando escaneo en {self.host}...") #inicializar el escaneo
        for port in self.ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crear socket
            sock.settimeout(0.5)# tiempo de espera
            result = sock.connect_ex((self.host, port)) # conectar al puerto
            if result == 0:
                print(f"✅ Puerto {port} abierto")
                self.open_ports.append(port)
            sock.close()# cerrar socket

    def report(self):
        print("\n📊 Resultados del escaneo:")
        if self.open_ports: # si hay puertos abiertos
            for port in self.open_ports:# recorrer puertos abiertos
                print(f" - Puerto {port}: ABIERTO") # mostrar puerto abierto
        else:
            print("No se encontraron puertos abiertos.")
            
            
host = "57.144.196.1" # definir host  
puertos= [21, 22, 23, 25, 80, 443, 8080] # definir puertos   

#crear objeto y ejecutar
scanner1 = PortScanner(host, puertos)
scanner1.scan()
scanner1.report()      