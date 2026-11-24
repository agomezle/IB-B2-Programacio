"""
B2.3.3. Bucles e iteración
"""

# ---------------------------------------------------------------
# 1. BUCLE CONTROLADO POR CONTADOR (FOR)
#    Se conoce de antemano el número de repeticiones.
# ---------------------------------------------------------------
print("1. BUCLE CONTROLADO POR CONTADOR (FOR)")

# 1.1 range(inicio, fin): el valor 'fin' NO se incluye
n = 5
print("1.1 range(0, n) con n = 5 -> i toma los valores de 0 a 4:")
for i in range(0, n):
    print(i)
print()

# 1.2 range(n) equivale a range(0, n) (el inicio por defecto es 0)
print("\n1.2 range(n) es lo mismo que range(0, n):")
for i in range(n):
    print(i)
print()

# 1.3 Cambiar el punto de partida: del 1 al 10 (fin = 11 para incluir el 10)
print("\n1.3 Del 1 al 10 con range(1, 11):")
for i in range(1, 11):
    print(i)
print()

# 1.4 Alternativa: de 0 a 9 mostrando i + 1
print("\n1.4 Alternativa: range(0, 10) mostrando i + 1:")
for i in range(0, 10):
    print(i + 1)
print()

# 1.5 Números impares con IF y el operador módulo (%)
print("\n1.5 Impares del 1 al 20 con IF (i % 2 == 1):")
for i in range(1, 21):
    if i % 2 == 1:
        print(i)
print()

# 1.6 Números impares SIN IF, usando un paso (step) de 2
print("\n1.6 Impares del 1 al 20 con paso 2, range(1, 21, 2):")
for i in range(1, 21, 2):
    print(i)
print()

# 1.7 Cuenta atrás: paso negativo
print("\n1.7 Cuenta atrás del 10 al 1 con range(10, 0, -1):")
for i in range(10, 0, -1):
    print(i)
print()


# ---------------------------------------------------------------
# 2. BUCLE DE PRECONDICIÓN (WHILE)
#    No se conoce el número de repeticiones. La condición se
#    comprueba ANTES de cada repetición, así que puede no
#    ejecutarse ni una vez.
# ---------------------------------------------------------------
print("2. BUCLE DE PRECONDICIÓN (WHILE)")

# 2.1 Verificación de doble entrada de contraseña.
#     En un programa real se usaría input(), aquí se simulan las entradas.
print("2.1 Verificación de contraseña (entradas simuladas):")
entrada1 = "abcd"   # lo que "teclearía" el usuario
entrada2 = "efgh"
entrada3 = "abcd"

password = entrada1            # primera entrada
pass_check = entrada2          # segunda entrada (no coincide)
print("   Contraseña:", password, "| Repetición:", pass_check)

while password != pass_check:     # se repite mientras NO coincidan
    print("   Las contraseñas no coinciden.")
    pass_check = entrada3         # equivale a pass_check = input(...)
    print("   Nueva repetición:", pass_check)
print("   Contraseña verificada (este mensaje sale DESPUÉS del bucle).")

# 2.2 Un WHILE puede no ejecutarse ni una vez
print("\n2.2 Un WHILE puede no ejecutarse nunca:")
x = 10
while x < 5:                      # la condición es falsa desde el principio
    print("   Esto no se imprime nunca")
    x = x + 1
print("   El bucle se ha saltado porque x < 5 era falso desde el inicio.")

# 2.3 Convertir un FOR en un WHILE (del 1 al 10)
print("\n2.3 Del 1 al 10 con WHILE:")
i = 1                             # inicialización
while i < 11:                     # condición de terminación: i >= 11
    print(i)
    i = i + 1                     # incremento: sin él, el bucle sería infinito
print()


# ---------------------------------------------------------------
# 3. BUCLE DE POSTCONDICIÓN (REPEAT-UNTIL)
#    La condición se comprueba al FINAL, por lo que el código se
#    ejecuta al menos una vez. Python no tiene repeat-until:
#    se simula con 'while True' + 'break'.
# ---------------------------------------------------------------
print("3. BUCLE DE POSTCONDICIÓN (REPEAT-UNTIL)")

# 3.1 Del 1 al 10
print("3.1 Del 1 al 10 con while True + break:")
i = 1
while True:
    print(i)
    i = i + 1
    if i > 10:                    # condición de terminación (UNTIL)
        break
print()

# 3.2 Se ejecuta al menos una vez, aunque la condición ya se cumpla
print("\n3.2 Se ejecuta una vez aunque la condición de salida ya sea cierta:")
i = 100                           # ya cumple i > 10 desde el principio
while True:
    print("   Cuerpo del bucle ejecutado con i =", i)
    i = i + 1
    if i > 10:
        break
print("   Comparación: un WHILE normal con i = 100 no habría entrado nunca.")


# ---------------------------------------------------------------
# RESUMEN
# ---------------------------------------------------------------
print("\nRESUMEN")
print("Controlado por contador (FOR)  -> nº de repeticiones conocido")
print("Precondición (WHILE)           -> puede no ejecutarse ni una vez")
print("Postcondición (REPEAT-UNTIL)   -> se ejecuta al menos una vez")