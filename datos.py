import csv

# Nombre del archivo CSV
archivo = "datos.csv"

# Leer y mostrar los datos
with open(archivo, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for fila in reader:
        print(fila)
