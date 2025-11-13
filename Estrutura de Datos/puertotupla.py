#tupla puertos criticos
puerto_criticos=(22,23,25,80,389,53,123)

Conexiones_detectadas=[("192.168.1.10",22),
                       ("10.0.0.5",80),
                       ("172.16.0.3",445),
                       ("192.168.1.12",123),
                       ("192.168.1.20",53),
                       ("200.200.1.10",8080)]

conexiones_sopechosa=[
    #List-compresion
    (ip,puerto) for (ip,puerto) in Conexiones_detectadas if puerto in puerto_criticos
]
print("Conexiones sopechosa detectada: ")
for ip, puerto in conexiones_sopechosa:
    print(f"IP {ip} conectada al puerto \n critico {puerto}")
