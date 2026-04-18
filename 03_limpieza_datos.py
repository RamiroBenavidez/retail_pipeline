import pandas as pd
from sqlalchemy import create_engine

# Configuración de la base de datos
engine = create_engine('postgresql://postgres:admin123@localhost:5432/retail_db')

try:
    print("📖 Cargando datos sucios...")
    df = pd.read_csv('datos_sucios.csv')

    # --- LIMPIEZA ---
    # Convertimos precio_unitario a número, lo que sea texto se vuelve NaN
    df['precio_unitario'] = pd.to_numeric(df['precio_unitario'], errors='coerce')

    # Eliminar filas con datos vitales faltantes
    df = df.dropna(subset=['producto', 'precio_unitario', 'id_cliente'])

    # Si la cantidad es negativa, la pasamos a positivo
    df['cantidad'] = df['cantidad'].abs()

    # --- TRANSFORMACIÓN ---
    df['total_venta'] = df['cantidad'] * df['precio_unitario']

    print("✨ Datos procesados internamente.")

    # --- GUARDADO EN CSV (Paso fundamental para S3) ---
    df.to_csv('datos_limpios.csv', index=False)
    print("✅ Archivo 'datos_limpios.csv' generado con éxito en tu carpeta.")

    # --- CARGA EN BASE DE DATOS ---
    try:
        print("Subiendo a la base de datos local...")
        df.to_sql('ventas_crudo', engine, if_exists='append', index=False)
        print("✅ Datos cargados en PostgreSQL.")
    except Exception as db_error:
        print(f"⚠️ Nota: No se pudo subir a la base de datos, pero el CSV ya se guardó. Error: {db_error}")

except Exception as e:
    print(f"❌ Error crítico en el proceso: {e}")