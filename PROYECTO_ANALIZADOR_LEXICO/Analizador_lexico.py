# Importando la biblioteca de expresiones regulares y la biblioteca tabulada.
import re
from tabulate import tabulate

# Abriendo el archivo textojava.txt y leyendo las líneas del archivo.
with open('C:/Users/EDISSON/Desktop/7 SEMESTRE U/COMPILADORES/MODULO 2/PROYECTO_ANALIZADOR_LEXICO/LenguajeJava.txt', 'r') as archivo:
    lineas = [re.sub(r'\/\/.*|\\/*[\s\S]*?\*\/', '', linea) for linea in archivo.readlines()]

# Una lista de palabras y símbolos que se van a utilizar en el programa.

condicionales = ['if', 'else', 'switch']
ciclos = ['for', 'while']
palabras_clave = [ 'String', 'int', 'double', 'public', 'class', 'main', 'import', 'Java.utils', 'float', 'void', 'args', 'case', 'continue', 'default', 'this', 'break', 'try', 'false', 'true', 'protected']
operadores = ['+', '-', '*', '/', '{', '}', '(', ')']
identificadores = []
numeros = []

# Crear una lista llamada tokens y agregarle los tokens que se encuentran en el archivo de texto.
tokens = []
for linea_numero, linea in enumerate(lineas):
    palabras_linea = re.findall(r'\w+|[^\w\s]', linea)
    for palabra_numero, palabra in enumerate(palabras_linea):
        if palabra in condicionales:
            tokens.append(('CONDICIONAL', palabra, linea_numero, palabra_numero))
        elif palabra in ciclos:
            tokens.append(('CICLOS', palabra, linea_numero, palabra_numero))
        elif palabra in palabras_clave:
            tokens.append(('PALABRA_CLAVE', palabra, linea_numero, palabra_numero))
        elif palabra in operadores:
            tokens.append(('OPERADOR', palabra, linea_numero, palabra_numero))
        # Comprobar si la palabra es un identificador.
        elif re.match(r'[a-zA-Z]\w*', palabra):
            if palabra not in identificadores:
                identificadores.append(palabra)
            tokens.append(('IDENTIFICADOR', palabra, linea_numero, palabra_numero))
        # Comprobar si la palabra es un número.
        elif re.match(r'\d+(\.\d*)?', palabra):
            if palabra not in numeros:
                numeros.append(palabra)
            tokens.append(('NUMERO', palabra, linea_numero, palabra_numero))
        else:
            tokens.append(('ERROR', palabra, linea_numero, palabra_numero))
            
# Creando un archivo llamado grupo2_resultados.txt y escribiendo en él los resultados del programa.
with open('C:/Users/EDISSON/Desktop/7 SEMESTRE U/COMPILADORES/MODULO 2/PROYECTO_ANALIZADOR_LEXICO/grupo2_resultados.txt', 'w') as archivo:
    archivo.write('TOKENS:\n')
    for token in tokens:
        archivo.write(f'{token[0]}: {token[1]} (linea {token[2]})\n')
    archivo.write('\n')
    archivo.write('LEXEMAS:\n')
    for linea in lineas:
        archivo.write(linea)
    archivo.write('\n\n')
    archivo.write(f'Condicional: {len([token for token in tokens if token[0]=="CONDICIONAL"])}\n')
    archivo.write(f'Ciclo: {len([token for token in tokens if token[0]=="CICLOS"])}\n')
    archivo.write(f'Palabras clave: {len([token for token in tokens if token[0]=="PALABRA_CLAVE"])}\n')
    archivo.write(f'Operadores: {len([token for token in tokens if token[0]=="OPERADOR"])}\n')
    archivo.write(f'Identificadores: {len(identificadores)}\n')
    archivo.write(f'Numeros: {len(numeros)}\n')
    archivo.write(f'Errores: {len([token for token in tokens if token[0]=="ERROR"])}\n')

# Impresión de los resultados del programa.
print('\nRESULTADOS:')
print('TOKENS:')
for token in tokens:
    print(f'{token[0]}: "{token[1]}"   ---->  ( línea {token[2]})')
print('')
print('\nLEXEMAS:\n')
for linea in lineas:
    print(linea)
print(f'\nCondicionales: {len([token for token in tokens if token[0]=="CONDICIONAL"])}')
print(f'Ciclos: {len([token for token in tokens if token[0]=="CICLOS"])}')
print(f'Palabras clave: {len([token for token in tokens if token[0]=="PALABRA_CLAVE"])}')
print(f'Operadores: {len([token for token in tokens if token[0]=="OPERADOR"])}')
print(f'Identificadores: {len(identificadores)}')
print(f'Números: {len(numeros)}')
print(f'Errores: {len([token for token in tokens if token[0]=="ERROR"])}')
print('')

# Crear un diccionario llamado tabla_simbolos y agregarle los tokens que son identificadores.
tabla_simbolos = {}
        
# Creando una tabla con los tokens y sus tipos.
filas_tabla = [(palabra, tipo) for palabra, tipo in tabla_simbolos.items()]

for linea_numero, linea in enumerate(lineas):
    palabras_linea = re.findall(r'\w+|[^\w\s]', linea)
    for palabra_numero, palabra in enumerate(palabras_linea):
        if palabra in condicionales:
            filas_tabla.append((palabra, "Condicional"))
        elif palabra in ciclos:
                filas_tabla.append((palabra, "Ciclo"))
        elif palabra in palabras_clave:
                filas_tabla.append((palabra, "Palabra_clave"))
        elif palabra in operadores:
                filas_tabla.append((palabra, "Operador"))
            # Comprobar si la palabra es un identificador.
        elif re.match(r'[a-zA-Z]\w*', palabra):
            if palabra not in identificadores:
                identificadores.append(palabra)
                filas_tabla.append((palabra, "Identificador"))
            # Comprobar si la palabra es un número.
        elif re.match(r'\d+(\.\d*)?', palabra):
            if palabra not in numeros:
                    numeros.append(palabra)
            filas_tabla.append((palabra, "Numero"))
        else:
            filas_tabla.append((palabra, "Desconocido"))

# Creando una tabla con los tokens y sus tipos.
tabla = tabulate(filas_tabla, headers=["Token", "Tipo"], tablefmt="pipe")
with open("C:/Users/EDISSON/Desktop/7 SEMESTRE U/COMPILADORES/MODULO 2/PROYECTO_ANALIZADOR_LEXICO/tabla_simbolos2.txt", "w") as archivo:
    archivo.write(f'{tabla}')