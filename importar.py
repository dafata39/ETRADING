import csv

# Ruta del archivo
ruta_archivo = "C:\\Users\\User\\Downloads\\eTrading\\Casos_positivos_de_COVID-19-Cund-Boy.csv"

# Abrir el archivo en modo lectura
with open(ruta_archivo, 'r') as archivo:

    # Crear un lector de CSV
    lector_csv = csv.reader(archivo, delimiter=',')

    # Saltar la cabecera
    next(lector_csv, None)

    # Recorrer las filas del archivo
    for fila in lector_csv:

        # Imprimir la fila
        print(fila)
