
import pandas as pd
import zipfile
import os
import requests

# 1. Descargar el archivo ZIP
url = "https://github.com/robintux/Datasets4StackOverFlowQuestions/blob/master/Cancer_Pulmon.zip?raw=true"
file_name = "Cancer_Pulmon.zip"

# Descargar el archivo desde GitHub
response = requests.get(url)
with open(file_name, 'wb') as file:
    file.write(response.content)

# 2. Descomprimir el archivo ZIP
with zipfile.ZipFile(file_name, 'r') as zip_ref:
    zip_ref.extractall("Cancer_Pulmon")  # Extrae en una carpeta llamada Cancer_Pulmon

# 3. Ver los archivos descomprimidos
extracted_files = os.listdir("Cancer_Pulmon")
print(f"Archivos descomprimidos: {extracted_files}")

# 4. Leer el archivo CSV (o el archivo adecuado) en un DataFrame
# Aquí, supongo que el archivo es un CSV. Si es otro tipo de archivo, ajusta el código de lectura en consecuencia.
csv_file = "Cancer_Pulmon/" + extracted_files[0]  # El primer archivo descomprimido

# Cargar el CSV en un DataFrame
df = pd.read_csv(csv_file)

# Mostrar las primeras filas del DataFrame
print(df.head())
