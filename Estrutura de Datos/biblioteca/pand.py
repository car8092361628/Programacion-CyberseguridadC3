
import pandas as pd

# Crear un DataFrame (tabla de datos) con un diccionario
datos = {
    'Producto': ['Camiseta', 'Pantalón', 'Zapatos', 'Sombrero', 'Guantes'],
    'Cantidad': [10, 5, 7, 2, 3],
    'Precio': [15.0, 25.0, 50.0, 12.0, 8.0],
    'Fecha': ['2025-04-01', '2025-04-01', '2025-04-02', '2025-04-02', '2025-04-03']
}

# Crear el DataFrame a partir del diccionario
df = pd.DataFrame(datos)

# Mostrar el DataFrame
print("Datos de ventas:")
print(df)

# 1. Calcular el total por producto (Cantidad * Precio)
df['Total'] = df['Cantidad'] * df['Precio']

# 2. Calcular el total de ventas (sumando todos los Totales)
total_ventas = df['Total'].sum()

# 3. Filtrar los productos vendidos el 2025-04-01
ventas_abril_01 = df[df['Fecha'] == '2025-04-01']

# Mostrar los resultados
print("\nDatos con total de ventas por producto:")
print(df)

print("\nTotal de ventas en todos los productos:", total_ventas)

print("\nVentas del 2025-04-01:")
print(ventas_abril_01)
