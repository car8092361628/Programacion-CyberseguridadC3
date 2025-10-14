# Lista de puertos abiertos encontrados
puertos_abiertos = [22, 80, 443, 8080, 3389, 445]

# Lista de puertos críticos o vulnerables
puertos_riesgo = [21, 23, 25, 135, 139, 445, 3389]

# Detectar coincidencias
puertos_sospechosos = [p for p in puertos_abiertos if p in puertos_riesgo]

print("Puertos abiertos con riesgo de explotación:")
for p in puertos_sospechosos:
    print(f"⚠️ Puerto {p}")
