import boto3
import os

# --- CONFIGURACIÓN ---
# Usamos el nombre que te apareció en la terminal antes
NOMBRE_BUCKET = 'retail-pipeline-data-benavidez'
# El archivo que tenés en tu carpeta de proyecto
ARCHIVO_LOCAL = 'datos_limpios.csv' 
# Cómo querés que se llame cuando esté guardado en Amazon
NOMBRE_EN_NUBE = 'datos_limpios_retail.csv' 

def subir_archivo():
    # Creamos el cliente de S3 (el "traductor" Boto3)
    s3 = boto3.client('s3', region_name='us-east-2')
    
    try:
        print(f"Buscando el archivo {ARCHIVO_LOCAL}...")
        
        # Verificamos si el archivo existe en tu carpeta antes de subirlo
        if os.path.exists(ARCHIVO_LOCAL):
            print("Subiendo a AWS S3... esto puede tardar unos segundos.")
            
            # El comando mágico de subida:
            s3.upload_file(ARCHIVO_LOCAL, NOMBRE_BUCKET, NOMBRE_EN_NUBE)
            
            print("---------------------------------------------")
            print("¡ÉXITO! El archivo ya está guardado en la nube.")
            print(f"Lo podés encontrar en el bucket: {NOMBRE_BUCKET}")
            print("---------------------------------------------")
        else:
            print(f"Error: No encontré el archivo '{ARCHIVO_LOCAL}' en esta carpeta.")
            
    except Exception as e:
        print(f"No se pudo subir. Error técnico: {e}")

if __name__ == "__main__":
    subir_archivo()