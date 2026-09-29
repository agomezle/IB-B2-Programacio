"""
OPERACIONS ARITMÈTIQUES.

Teoria clau:
- Operadors aritmètics bàsics: + (suma), - (resta), * (multiplicació),
    / (divisió), % (residu o mòdul).
- Reutilitzar variables: podem tornar a assignar un valor a una variable quan
    ja no necessitem el resultat anterior (cada variable només guarda UN valor).
- Divisió en Python:
    -> "/" sempre retorna un decimal (float), encara que els dos números siguin enters.
    -> "//" és la divisió entera: descarta els decimals (és l'equivalent a la
        divisió d'enters de Java).
- Residu (%): retorna el que sobra d'una divisió.
    -> Si num % 2 == 0, el número és divisible entre 2 (és parell).
"""

a = 5   # int
b = 13  # int
c = 0   # int

# --------------------------------------------------
# SUMA
# --------------------------------------------------
c = a + b
print(c)  # 18

# --------------------------------------------------
# RESTA
# --------------------------------------------------
c = a - b  # Reutilitzo la variable "c" perquè el resultat anterior no el necessitaré més
print(c)  # -8

# --------------------------------------------------
# MULTIPLICACIÓ
# --------------------------------------------------
c = a * b
print(c)  # 65

# --------------------------------------------------
# DIVISIÓ
# --------------------------------------------------
# A Java, int / int donava 0 perquè "c" era de tipus int i es perdien els decimals.
# A Python, "/" ja retorna un decimal (float) automàticament:
c = a / b
print(c)  # 0.38461538461538464

# Si volem el mateix comportament que a Java (divisió entera), fem servir "//":
c = a // b
print(c)  # 0

# En Python no cal declarar la variable com a "double": n'hi ha prou amb
# assignar un valor decimal (o convertir-lo amb float()).
a_decimal = 5.0     # float
b_decimal = 13.0    # float

c_decimal = a_decimal / b_decimal
print(c_decimal)  # 0.38461538461538464

# --------------------------------------------------
# RESIDU / MÒDUL
# --------------------------------------------------
c_decimal = a_decimal % b_decimal
print(c_decimal)  # 5.0 (5 entre 13 dóna 0 i sobra 5)

num1 = 14

# --------------------------------------------------
# EXEMPLE: ÉS DIVISIBLE ENTRE 2?
# --------------------------------------------------
divisible = num1 % 2
print(divisible)  # 0 -> és divisible perquè el residu és 0

# Podem comprovar-ho directament amb una comparació (retorna True o False):
print(num1 % 2 == 0)  # True