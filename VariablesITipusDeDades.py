
"""
VARIABLES (B2.1.1).

Teoria clau:
- Variable: ubicació de memòria que emmagatzema un valor que pot canviar.
- Identificador: el nom que li donem a la variable.
- Declaració: especificar el tipus de dada (enter, decimal, text...)
    -> En Python, el llenguatge no exigeix la declaració, però nosaltres ho indiquem amb
        un comentari per aclarir-nos.
- Inicialització: assignar-li un valor inicial.
- Cada variable només pot tenir UN valor a la vegada.
"""

# <-- Això és un comentari, vol dir que el programa no llegeix aquesta línia, ens serveix
#       a nosaltres per explicar el codi

# ============================================
#   B2.1.1 VARIABLES
# ============================================

# --- 1. QUÈ ÉS UNA VARIABLE? ---
# Una variable és una ubicació de memòria que emmagatzema
# un valor que pot canviar durant l'execució del programa.
# Identificador = nom de la variable | Valor = contingut actual

# declaració (comentari) + inicialització (donar-li valor)
bonus_mensual = 150.75 # float
print("Identificador: bonus_mensual")
print("Valor inicial: ", bonus_mensual)

bonus_mensual = 220.30  # el valor canvia (reassignació)
print("Nou valor:", bonus_mensual)
print()

# --- 2. TIPUS DE DADES PRIMITIUS ---

# STRING: seqüència de caràcters, dígits o símbols
password = "Bob@123"  # string (cometes simples o dobles en Python)
print("String  -> ", password, "  | tipus: ", type(password).__name__)

# INTEGER: nombre enter (positiu o negatiu)
edat = 17  # int
print("Integer ->", edat, "        | tipus: ", type(edat).__name__)

# FLOAT / DOUBLE: nombre decimal
preu = 19.99  # float (Python no distingeix float de double, al contrari que altres llenguatges)
print("Float   ->", preu, "      | tipus: ", type(preu).__name__)

# CHAR: un sol caràcter (Python no té tipus char propi, s'utilitza un string d'un sol caràcter)
inicial = "M"  # char
print("Char    ->", inicial, "         | tipus: ", type(inicial).__name__, "(longitud 1)")

# BOOLEAN: true o false
en_estoc = True  # boolean
print("Boolean -> ", en_estoc, "      | tipus: ", type(en_estoc).__name__)
print()

# --- 3. EXEMPLE PRÀCTIC: SOU FIX + BONUS VARIABLE ---
salari_base = 1200.00     # float -> és fix (constant)
bonus_gener = 300.50      # float -> variable, canvia cada mes
bonus_febrer = 410.25     # float -> mateix concepte, valor diferent

sou_total_gener = salari_base + bonus_gener
sou_total_febrer = salari_base + bonus_febrer

print("Salari base (fix): ", salari_base, "€")
print("Bonus gener (variable): ", bonus_gener, "€ -> Total: ", sou_total_gener, "€")
print("Bonus febrer (variable): ", bonus_febrer, "€ -> Total: ", sou_total_febrer, "€")
print()

# --- 4. OPERADORS LÒGICS AMB BOOLEANS ---
a = 7
b = 54

cond_and = (a < 9) and (b > 30)
cond_or = (a > 3) or (b < 3)

print("a = ", a, " b = ", b)
print("(a < 9) and (b > 30) -> ", cond_and, " (cal que es compleixin les dues)")
print("(a > 3) or (b < 3)   -> ", cond_or, " (n'hi ha prou amb una)")