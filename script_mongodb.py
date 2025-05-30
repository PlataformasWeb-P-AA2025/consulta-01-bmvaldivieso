# ---------------------- IMPORTACIONES Y CONEXION A MONGODB ----------------------

import pandas as pd  # Importar pandas para manejar archivos Excel
from pymongo import MongoClient  # Importar la biblioteca para conectar con MongoDB

# Conectar con MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Conectar con el servidor MongoDB en localhost
db = client["miBaseDeDatos"]  # Seleccionar o crear la base de datos "miBaseDeDatos"
collection = db["miColeccion"]  # Seleccionar o crear la colección "miColeccion"


# ---------------------- CARGA, CONVERSION E INSERCION DE LA DATA A LA BASE DE DATOS ----------------------

# Cargar archivos Excel
df_2022 = pd.read_excel("data/2022.xlsx")  # Leer el archivo 2022.xlsx y guardarlo en un DataFrame
df_2023 = pd.read_excel("data/2023.xlsx")  # Leer el archivo 2023.xlsx y guardarlo en otro DataFrame

# Convertir los datos a formato JSON
data_2022 = df_2022.to_dict(orient="records")  # Convertir el DataFrame en una lista de diccionarios (JSON)
data_2023 = df_2023.to_dict(orient="records")  # Convertir el otro DataFrame en lista de diccionarios (JSON)

# Insertar los datos en MongoDB
collection.insert_many(data_2022)  # Insertar todos los registros del archivo 2022.xlsx en MongoDB
collection.insert_many(data_2023)  # Insertar todos los registros del archivo 2023.xlsx en MongoDB

print("=" * 100) # Separador

print("Datos insertados correctamente en MongoDB.")  # Mensaje de confirmación

print("=" * 100) # Separador  


# ---------------------- CONSULTAS EN MONGODB ----------------------

# Consulta 01: Contar el total de registros en la colección
total_registros = collection.count_documents({})  # Contar todos los documentos almacenados en la colección

# Mostrar el total de registros
print(f"CONSULTA 01: Total de registros en la base de datos: {total_registros}") 

print("=" * 100) # Separador


# Consulta 02: Obtener los primeros 5 registros con datos relevantes de los torneos
primeros_datos = collection.find({}, {"_id": 0, "Tournament": 1, "Location": 1, "Date": 1, "Winner": 1, "Loser": 1, "Round": 1}).limit(5)

# Imprimir los resultados de manera organizada
print("CONSULTA 02: Primeros 5 partidos registrados en la base de datos:")
print("=" * 70) # Separador

for doc in primeros_datos:
    print(f"Torneo: {doc.get('Tournament', 'Desconocido')}")
    print(f"Ubicación: {doc.get('Location', 'No especificada')}")
    print(f"Fecha: {doc.get('Date', 'Sin fecha')}")
    print(f"Ganador: {doc.get('Winner', 'No registrado')}")
    print(f"Perdedor: {doc.get('Loser', 'No registrado')}")
    print(f"Ronda: {doc.get('Round', 'Sin información')}")
    print("=" * 70)  # Separador entre registros
   




