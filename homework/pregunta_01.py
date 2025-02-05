import pandas as pd
import os

def crear_directorio_salida(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)

def pregunta_01():
    """
        Realiza la limpieza del archivo "files/input/solicitudes_de_credito.csv".
        El archivo tiene problemas como registros duplicados y datos faltantes.
        Ten en cuenta todas las verificaciones discutidas en clase para
        realizar la limpieza de los datos.

        El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"
    """
    # Eliminar el archivo si existe
    if os.path.exists('files/output/solicitudes_de_credito.csv'):
        os.remove('files/output/solicitudes_de_credito.csv')
    
    # Se abre el archivo
    ruta_archivo = 'files/input/solicitudes_de_credito.csv'
    datos = pd.read_csv(ruta_archivo, sep=';', index_col=0, encoding='UTF-8')

    # Limpiar las columnas
    # Seleccionamos las columnas a evaluar
    columnas_a_limpiar = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "monto_del_credito", "línea_credito"]

    # Hacemos un ciclo for para limpiar las columnas
    for columna in columnas_a_limpiar:
        if columna in datos.columns:
            datos[columna] = datos[columna].str.lower().str.strip().str.replace("_", " ").str.replace("-", " ").str.replace(",", "").str.replace("$", "").str.replace(".00", "").str.strip()

    # Limpiar idea_negocio
    datos['idea_negocio'] = datos['idea_negocio'].str.replace(' ','').str.replace('-','').str.strip('_')

    # Limpiar barrio 
    datos['barrio'] = datos["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")

    # Dar formato a estrato
    datos['estrato'] = datos['estrato'].astype(int)

    # Dar formato a comuna_ciudadano
    datos['comuna_ciudadano'] = pd.to_numeric(datos["comuna_ciudadano"], errors="coerce", downcast="integer")

    # Limpiar la columna fecha_de_beneficio
    datos['fecha_de_beneficio'] = datos["fecha_de_beneficio"] = pd.to_datetime(datos["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce").combine_first(pd.to_datetime(datos["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))

    # Limpiar la columna monto_del_credito
    datos['monto_del_credito'] = pd.to_numeric(datos["monto_del_credito"], errors="coerce")

    # Borrar duplicados y nulos
    datos = datos.drop_duplicates()
    datos = datos.dropna()
    # Guardar el DataFrame limpio
    datos.to_csv('files/output/solicitudes_de_credito.csv', sep=';', index=False)

pregunta_01()