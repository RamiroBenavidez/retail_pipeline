import subprocess
import sys

def correr_script(nombre_archivo):
    print(f"\n>> Ejecutando: {nombre_archivo}...")
    # Ejecuta el script y espera a que termine
    resultado = subprocess.run(["python", nombre_archivo])
    
    if resultado.returncode != 0:
        print(f"❌ Error en {nombre_archivo}. El proceso se detuvo.")
        sys.exit(1)
    else:
        print(f"✅ {nombre_archivo} finalizado con éxito.")

def iniciar_proceso_completo():
    print("🚀 INICIANDO PIPELINE DE RETAIL")
    print("================================")

    # 1. Paso de Transformación (Limpieza)
    correr_script("03_limpieza_datos.py")

    # 2. Paso de Carga (AWS S3)
    correr_script("04_subir_a_s3.py")

    print("\n================================")
    print("🎉 PIPELINE FINALIZADO EXITOSAMENTE")

if __name__ == "__main__":
    iniciar_proceso_completo()