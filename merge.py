import pandas as pd
import os
import glob

def leer_archivo_con_codificacion(filename, sep='|', header=None):
    codificaciones = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
    for encoding in codificaciones:
        try:
            return pd.read_csv(filename, sep=sep, header=header, encoding=encoding)
        except UnicodeDecodeError:
            print(f"Error de codificación con {encoding} para el archivo {filename}. Intentando con otra codificación.")
    raise UnicodeDecodeError(f"No se pudo leer el archivo {filename} con las codificaciones probadas.")

def combinar_archivos_txt_a_csv(indir="E:/CONCENTRADO TOTAL", archivo_salida="archivo_salida.csv"):
    dfs = []  # Lista para almacenar los DataFrames
    os.chdir(indir)  # Cambia al directorio donde están los archivos TXT
    fileList = glob.glob("*.txt")  # Obtiene la lista de nombres de archivos TXT
    for filename in fileList:
        try:
            data = leer_archivo_con_codificacion(filename)  # Lee el archivo TXT con separador "|"
            dfs.append(data)
        except Exception as e:
            print(f"Error al leer el archivo {filename}: {e}")
    # Concatena todos los DataFrames en uno solo
    outputDf = pd.concat(dfs, ignore_index=True)
    # Guarda el resultado en un archivo CSV
    outputDf.to_csv(archivo_salida, index=False)

# Llama a la función para combinar los archivos
combinar_archivos_txt_a_csv()



