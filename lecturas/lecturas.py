def contar_palabra_en_fichero(nombre_fichero, separador, palabra):
    """
    Cuenta cuántas veces aparece una palabra en un archivo de texto dado un separador.

    :param nombre_fichero:lin_quijote.txt
    :param separador: sep
    :param palabra: quijote
    :return: Número de veces que aparece la palabra.
    """
    try:
        with open(nombre_fichero, 'r', encoding='utf-8') as fichero:
            contenido = fichero.read()  # Lee el contenido del archivo
            # Separa el contenido usando el separador
            terminos = contenido.split(separador)
            # Cuenta las ocurrencias de la palabra
            conteo = terminos.count(palabra)
            return conteo
    except FileNotFoundError:
        print(f"El archivo '{nombre_fichero}' no se encontró.")
        return 0
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return 0

# Ejemplo de uso
nombre_fichero = 'lin_quijote.txt'  # Nombre del archivo
separador = ','  # Separador usado en el archivo
palabra = 'quijote'  # Palabra a contar

# Llamada a la función
conteo_palabra = contar_palabra_en_fichero(nombre_fichero, separador, palabra)
print(f"La palabra '{palabra}' aparece {conteo_palabra} veces en el archivo '{nombre_fichero}'.")

def buscar_lineas_con_cadena(nombre_fichero, cadena):
    """
    Devuelve una lista de líneas que contienen una cadena específica en un archivo de texto.

    :param nombre_fichero: Nombre del archivo de texto.
    :param cadena: Cadena de texto a buscar en las líneas.
    :return: Lista de líneas que contienen la cadena.
    """
    lineas_encontradas = []  # Lista para almacenar las líneas que contienen la cadena
    try:
        with open(nombre_fichero, 'r', encoding='utf-8') as fichero:
            for linea in fichero:  # Lee el archivo línea por línea
                if cadena in linea:  # Comprueba si la cadena está en la línea
                    lineas_encontradas.append(linea.strip())  # Agrega la línea a la lista
    except FileNotFoundError:
        print(f"El archivo '{nombre_fichero}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    
    return lineas_encontradas

# Ejemplo de uso
nombre_fichero = 'lin_quijote.txt'  # Nombre del archivo
cadena = 'quijote'  # Cadena a buscar

# Llamada a la función
lineas_con_cadena = buscar_lineas_con_cadena(nombre_fichero, cadena)
print(f"Líneas que contienen la cadena '{cadena}'son:")
for linea in lineas_con_cadena:
    print(linea)
    
def encontrar_palabras_unicas(nombre_fichero):
    """
    Encuentra todas las palabras únicas en un archivo de texto y las devuelve en una lista.

    :param nombre_fichero: Nombre del archivo de texto.
    :return: Lista de palabras únicas.
    """
    palabras_unicas = set()  # Usamos un conjunto para almacenar palabras únicas
    try:
        with open(nombre_fichero, 'r', encoding='utf-8') as fichero:
            for linea in fichero:  # Lee el archivo línea por línea
                # Separa la línea en palabras usando espacios como delimitador
                palabras = linea.split()
                # Agrega cada palabra al conjunto
                palabras_unicas.update(palabras)
    except FileNotFoundError:
        print(f"El archivo '{nombre_fichero}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    
    return list(palabras_unicas)  # Convertimos el conjunto a lista y la devolvemos

# Ejemplo de uso
nombre_fichero = 'archivo_palabras.txt'  # Nombre del archivo

# Llamada a la función
palabras_unicas = encontrar_palabras_unicas(nombre_fichero)
print(f"Palabras únicas en el archivo '{nombre_fichero}':")
print(palabras_unicas)


from typing import Optional

def longitud_promedio_lineas(file_path: str) -> Optional[float]:
    """
    Devuelve la longitud media de las líneas en un archivo CSV.

    :param file_path: Ruta del archivo CSV.
    :return: Longitud media de las líneas o None si el archivo está vacío.
    """
    try:
        total_longitud = 0
        contador_lineas = 0
        
        with open(file_path, 'r', encoding='utf-8') as fichero:
            for linea in fichero:
                total_longitud += len(linea.strip())  # Sumar la longitud de la línea (sin espacios en blanco)
                contador_lineas += 1  # Contar la línea

        # Calcular la longitud media
        if contador_lineas == 0:
            return None  # Retornar None si no hay líneas en el archivo

        longitud_media = total_longitud / contador_lineas
        return longitud_media

    except FileNotFoundError:
        print(f"El archivo '{file_path}' no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None

# Ejemplo de uso
nombre_fichero = 'palabras_random.csv'  # Nombre del archivo CSV

# Llamada a la función
media_lineas = longitud_promedio_lineas(nombre_fichero)
if media_lineas is not None:
    print(f"La longitud media de las líneas en '{nombre_fichero}' es: {media_lineas:.2f}")
else:
    print("No se pudo calcular la longitud media de las líneas.")
    
from typing import Optional

def longitud_promedio_lineas(file_path: str) -> Optional[float]:
    """
    Devuelve la longitud media de las líneas en un archivo CSV.

    :param file_path: Ruta del archivo CSV.
    :return: Longitud media de las líneas o None si el archivo está vacío.
    """
    try:
        total_longitud = 0
        contador_lineas = 0
        
        with open(file_path, 'r', encoding='utf-8') as fichero:
            for linea in fichero:
                total_longitud += len(linea.strip())  # Sumar la longitud de la línea (sin espacios en blanco)
                contador_lineas += 1  # Contar la línea

        # Calcular la longitud media
        if contador_lineas == 0:
            return None  # Retornar None si no hay líneas en el archivo

        longitud_media = total_longitud / contador_lineas
        return longitud_media

    except FileNotFoundError:
        print(f"El archivo '{file_path}' no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None

# Ejemplo de uso
nombre_fichero = 'vacio.csv'  # Nombre del archivo CSV

# Llamada a la función
media_lineas = longitud_promedio_lineas(nombre_fichero)
if media_lineas is not None:
    print(f"La longitud media de las líneas en '{nombre_fichero}' es: {media_lineas:.2f}")
else:
    print("No se pudo calcular la longitud media de las líneas del archivo vacio.csv")