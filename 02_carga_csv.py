import pandas as pd
from sqlalchemy import create_engine

# --- CONFIGURACIÓN ---
engine = create_engine('postgresql://postgres:admin123@localhost:5432/retail_db')

try:
    # A. EXTRACCIÓN: Leer desde el archivo físico
    print("📖 Cargando datos desde el archivo CSV...")
    df = pd.read_csv('datos_ventas.csv')

    # B. TRANSFORMACIÓN: Agregar valor a los datos
    # Creamos la columna 'total_venta' multiplicando otras dos
    df['total_venta'] = df['cantidad'] * df['precio_unitario']
    
    print("✨ Transformación completada. Datos listos para subir:")
    print(df) # Esto te mostrará la tabla con la nueva columna en la terminal

    # C. CARGA: Guardar en la base de datos
    # 'if_exists=append' para no borrar lo que ya tenías de la lección 1
    df.to_sql('ventas_crudo', engine, if_exists='append', index=False)
    
    print("\n✅ ¡Éxito total! Datos del CSV guardados en PostgreSQL.")

except Exception as e:
    print(f"❌ Hubo un error: {e}")