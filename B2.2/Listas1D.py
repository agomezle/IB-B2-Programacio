"""
Estructuras de datos estáticas y dinámicas, arrays/listas 1D
y arrays paralelos (B2.2.1 y B2.2.2).
"""


def titulo(texto):
    print("\n" + "=" * 55)
    print(texto)
    print("=" * 55)


# ---------------------------------------------------------------
# 1. ESTRUCTURA ESTÁTICA (tamaño fijo)
# Python no tiene arrays estáticos "puros", así que se simula una
# lista de tamaño fijo: se reserva de antemano con [0] * n.
# ---------------------------------------------------------------
titulo("1. Estructura estática (tamaño fijo)")

CAPACIDAD = 5
estatica = [0] * CAPACIDAD      # memoria reservada aunque no se use
print("Reservada:", estatica)

# Acceso DIRECTO: se llega al elemento con su índice, sin recorrer nada
estatica[2] = 90
print("Elemento en el índice 2:", estatica[2])

# Desventaja: si no hay hueco, no se puede añadir (tamaño fijo)
usados = 3                      # suponemos 3 posiciones ocupadas
estatica[0], estatica[1] = 75, 60
print("Estática con datos:", estatica, "-> posiciones sin usar:",
      CAPACIDAD - usados)

# Desventaja: al eliminar queda un hueco vacío entre dos elementos
estatica[1] = 0                 # "borrar" el 60
print("Tras eliminar el índice 1 queda un hueco:", estatica)


# ---------------------------------------------------------------
# 2. ESTRUCTURA DINÁMICA (crece y decrece en ejecución)
# La lista de Python se comporta como estructura dinámica.
# ---------------------------------------------------------------
titulo("2. Estructura dinámica (crece y decrece)")

dinamica = []                   # empieza vacía, sin tamaño predefinido
for nota in [75, 60, 90]:
    dinamica.append(nota)       # crece en tiempo de ejecución
print("Tras añadir:", dinamica)

dinamica.pop()                  # decrece en tiempo de ejecución
print("Tras eliminar el último:", dinamica)

# Insertar en medio sin dejar huecos (ventaja frente a la estática)
dinamica.insert(1, 85)
print("Tras insertar 85 en el índice 1:", dinamica)

# Subdesbordamiento (underflow): eliminar de una estructura vacía.
# El programador debe controlarlo o dará una excepción.
vacia = []
if len(vacia) > 0:
    vacia.pop()
else:
    print("Cuidado: no se puede eliminar, la estructura está vacía")

# Desbordamiento (overflow): controlar un límite máximo propio. Como las listas
# son dinámicas no dará excepción, pero podemos limitar el tamaño nosotros.
LIMITE = 4
for nota in [70, 55, 95]:
    if len(dinamica) < LIMITE:
        dinamica.append(nota)
    else:
        print(f"Cuidado: límite alcanzado, no se añade {nota}")
print("Dinámica final:", dinamica)


# ---------------------------------------------------------------
# 3. ACCESO DIRECTO vs. ACCESO SECUENCIAL
# ---------------------------------------------------------------
titulo("3. Acceso directo vs. secuencial")

grades = [75, 60, 90, 85, 70]   # array 1D de enteros

# Directo: se va a la posición 3 sin mirar las anteriores
print("Directo, índice 3:", grades[3])

# Secuencial: se comprueba uno tras otro desde el principio, recorriendo la lista
objetivo = 85
posicion = -1
for i in range(len(grades)):
    if grades[i] == objetivo:
        posicion = i
        break
print(f"Secuencial: {objetivo} encontrado en el índice {posicion}")


# ---------------------------------------------------------------
# 4. ARRAYS / LISTAS 1D: creación, relleno y recorrido con bucles
# ---------------------------------------------------------------
titulo("4. Listas 1D: inicialización y bucles")

# [0] * 5 crea cinco ceros: el tamaño existe y se puede rellenar.
# Con grades = [] el bucle fallaría (index out of range).
notas = [0] * 5
entradas_simuladas = [75, 60, 90, 85, 70]   # sustituye a input()

for i in range(5):
    # notas[i] = int(input("Introduce una nota: "))
    notas[i] = entradas_simuladas[i]
print("Lista rellenada con un bucle FOR:", notas)

# El último elemento está en el índice len - 1 (si se empieza en 0)
print("Último elemento:", notas[len(notas) - 1])

# Cálculo con todos los elementos: se usa un bucle
total = 0
for i in range(len(notas)):
    total = total + notas[i]
print("Media:", total / len(notas))

# Una lista también puede ser de string o de booleanos (un único tipo por lista)
names = ["Ana", "Luis", "Marta", "Pau", "Sara"]
passed = [True, False, True, True, False]
print("Nombres:", names)
print("Aprobados:", passed)


# ---------------------------------------------------------------
# 5. ERROR COMÚN: inicializar el mínimo a 0
# ---------------------------------------------------------------
titulo("5. Error común: calcular el mínimo")

# MAL: si todas las notas son positivas, nunca habrá nada menor que 0
minimo_mal = 0
for i in range(len(grades)):
    if grades[i] < minimo_mal:
        minimo_mal = grades[i]
print("Mínimo (INCORRECTO):", minimo_mal)

# BIEN: se inicializa con el primer elemento del array.
# Se evita llamarla "min", que es una función de Python.
minimum = grades[0]
for i in range(1, len(grades)):
    if grades[i] < minimum:
        minimum = grades[i]
print("Nota mínima (CORRECTO):", minimum)


# ---------------------------------------------------------------
# 6. ARRAYS PARALELOS
# Mismo tamaño; el índice n de cada array describe a la misma entidad.
# ---------------------------------------------------------------
titulo("6. Arrays paralelos")

nombres = ["Ana", "Luis", "Marta"]
edades = [16, 17, 16]
direcciones = ["C/ Mayor 1", "C/ Sol 5", "C/ Luna 8"]

# Los tres elementos del índice 2 describen a la misma alumna
print(nombres[2], edades[2], direcciones[2])

# Recorrido conjunto: un solo índice sirve para los tres arrays
for i in range(len(nombres)):
    print(f"Alumno {i + 1}: {nombres[i]}, {edades[i]} años, vive en {direcciones[i]}")

# Búsqueda en arrays paralelos: se busca en uno y se usa el índice en otro
buscado = "Luis"
for i in range(len(nombres)):
    if nombres[i] == buscado:
        print(f"{buscado} tiene {edades[i]} años")