#Lista de Ips que se detectaron en el trafico de red
ips_detectadas=["192.168.1.10",
                "10.0.0.5",
                "8.8.8.8",
                "185.220.101.4",
                "45.83.64.1"]

#Lista de IPs conocidas por actividad maliciosa (Blacklist)

ips_maliciosas=["185.220.101.4", #Nodo Tor
                "45.83.64.1", #servidor conocido
                "103.27.202.18"]

#Buscar Coincidencia entre las Ips Detectadad y las Ips maliciosa

Ips_Sospechosa=[]

for ip in ips_detectadas:
    if ip in ips_maliciosas:
        Ips_Sospechosa.append(ip)
 
print("Ips sospechosas detectadas : ") 
for ip in Ips_Sospechosa:
    print(f"Las ips sospechosa son {ip}")      
