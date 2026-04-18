# Retail Data Pipeline: De Local a AWS S3 🚀

Este proyecto implementa un pipeline de datos (ETL) completo para procesar información de ventas retail. Automatiza la limpieza de datos locales y su posterior carga en un entorno de nube profesional.

## 📋 Descripción del Proyecto
El pipeline extrae datos crudos de archivos CSV, aplica transformaciones lógicas utilizando **Python** y **Pandas**, para finalmente persistir los resultados tanto en una base de datos **PostgreSQL** como en un Data Lake en **AWS S3**.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.10+
* **Procesamiento de Datos:** Pandas
* **Base de Datos:** PostgreSQL & SQLAlchemy (ORM)
* **Cloud Storage:** AWS S3 (usando la librería Boto3)
* **Entorno:** Virtualenv para gestión de dependencias

## ⚙️ Arquitectura del Pipeline
1. **Extract:** Carga de archivos CSV.
2. **Transform:** Limpieza de nulos y cálculos de negocio.
3. **Load:** Carga en PostgreSQL local y AWS S3.

## 🚀 Cómo Ejecutar
1. Clonar el repositorio.
2. Instalar dependencias: `pip install -r requirements.txt`.
3. Ejecutar el orquestador: `python ejecutar_pipeline.py`.