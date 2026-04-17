import pandas as pd
from sqlalchemy import create_engine

# 1. Configura tu conexión (verifica que la contraseña sea la que pusiste en el paso anterior)
engine = create_engine('postgresql://postgres:admin123@localhost:5432/retail_db')

# 2. Datos de prueba
data = {
    'id_venta': [1, 2],
    'fecha': ['2023-10-01', '2023-10-01'],
    'producto': ['Monitor', 'Teclado'],
    'cantidad': [1, 2],
    'precio_unitario': [250.00, 50.00],
    'id_cliente': [101, 102]
}

df = pd.DataFrame(data)

# 3. Envío a la base de datos
try:
    df.to_sql('ventas_crudo', engine, if_exists='append', index=False)
    print("✅ ¡Éxito! Los datos ya están en PostgreSQL.")
except Exception as e:
    print(f"❌ Error: {e}")