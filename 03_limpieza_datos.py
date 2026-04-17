import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:admin123@localhost:5432/retail_db')

try:
    print("📖 Cargando datos sucios...")
    # 'errors="coerce"' hará que si hay texto en el precio, lo convierta en NaN (vacío)
    df = pd.read_csv('datos_sucios.csv')

    # --- LIMPIEZA 1: Manejar valores no numéricos ---
    # Convertimos precio_unitario a número, lo que sea texto se vuelve NaN
    df['precio_unitario'] = pd.to_numeric(df['precio_unitario'], errors='coerce')

    # --- LIMPIEZA 2: Eliminar filas con datos vitales faltantes ---
    # Si no tiene producto o no tiene precio, no nos sirve.
    df = df.dropna(subset=['producto', 'precio_unitario', 'id_cliente'])

    # --- LIMPIEZA 3: Corregir valores imposibles ---
    # Si la cantidad es negativa, la pasamos a positivo (suponiendo error de carga)
    df['cantidad'] = df['cantidad'].abs()

    # --- TRANSFORMACIÓN: Ahora sí calculamos el total ---
    df['total_venta'] = df['cantidad'] * df['precio_unitario']

    print("✨ Datos limpios y procesados:")
    print(df)

    # CARGA
    df.to_sql('ventas_crudo', engine, if_exists='append', index=False)
    print("\n✅ Datos limpios cargados exitosamente.")

except Exception as e:
    print(f"❌ Error en el proceso: {e}")