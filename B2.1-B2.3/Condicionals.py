"""
B2.3.2. Estructuras de selección
"""

# ---------------------------------------------------------------
# 1. IF SIMPLE
#    Si la condición es verdadera se ejecutan unas instrucciones;
#    si no, no ocurre nada.
# ---------------------------------------------------------------
print("1. IF SIMPLE")

# 1.1 Descuento del 20 % si la compra es de 100 o más
#     En un programa real se usaría input(), aquí se simulan los valores.
purchase_value = 150
discount = 0                      # se inicializa a 0 por si no se cumple la condición

if purchase_value >= 100:
    discount = purchase_value * 0.2

print("1.1 Compra:", purchase_value, "-> Descuento:", discount)

# 1.2 Misma condición con una compra que NO llega a 100
purchase_value = 80
discount = 0

if purchase_value >= 100:
    discount = purchase_value * 0.2

print("\n1.2 Compra:", purchase_value, "-> Descuento:", discount)

# 1.3 La indentación indica qué instrucciones pertenecen al IF
purchase_value = 80
print("\n1.3 La indentación importa:")
if purchase_value >= 100:
    print("   Esto solo se muestra si la compra es de 100 o más")
print("   Esto se muestra SIEMPRE (no está indentado)")


# ---------------------------------------------------------------
# 2. IF - ELSE
#    Añade instrucciones que se ejecutan cuando la condición es falsa.
# ---------------------------------------------------------------
print("\n2. IF - ELSE")

purchase_value = 150
if purchase_value >= 100:
    discount = purchase_value * 0.2
else:
    discount = 0
print("2.1 Compra:", purchase_value, "-> Descuento:", discount)

purchase_value = 60
if purchase_value >= 100:
    discount = purchase_value * 0.2
else:
    discount = 0
print("2.2 Compra:", purchase_value, "-> Descuento:", discount)


# ---------------------------------------------------------------
# 3. IF ANIDADOS (NESTED IF)
#    Un IF dentro de otro IF.
#    Compra >= 100: 20 % si es socio, 10 % si no lo es.
# ---------------------------------------------------------------
print("\n3. IF ANIDADOS (NESTED IF)")

purchase_value = 150
member = True                     # debe ser booleano (True / False)

if purchase_value >= 100:
    if member == True:
        discount = purchase_value * 0.2
    else:
        discount = purchase_value * 0.1
else:
    discount = 0
print("3.1 Compra:", purchase_value, "| Socio:", member, "-> Descuento:", discount)

member = False
if purchase_value >= 100:
    if member == True:
        discount = purchase_value * 0.2
    else:
        discount = purchase_value * 0.1
else:
    discount = 0
print("3.2 Compra:", purchase_value, "| Socio:", member, "-> Descuento:", discount)


# ---------------------------------------------------------------
# 4. IF - ELIF - ELSE
#    Lo mismo que el apartado 3, pero con el operador lógico AND
#    y varias condiciones encadenadas. En Python, 'else if' es 'elif'.
# ---------------------------------------------------------------
print("\n4. IF - ELIF - ELSE")

purchase_value = 150
member = True

if purchase_value >= 100 and member:
    discount = purchase_value * 0.2
elif purchase_value >= 100 and not member:
    discount = purchase_value * 0.1
else:
    discount = 0
print("4.1 Compra:", purchase_value, "| Socio:", member, "-> Descuento:", discount)

member = False
if purchase_value >= 100 and member:
    discount = purchase_value * 0.2
elif purchase_value >= 100 and not member:
    discount = purchase_value * 0.1
else:
    discount = 0
print("4.2 Compra:", purchase_value, "| Socio:", member, "-> Descuento:", discount)

purchase_value = 50
if purchase_value >= 100 and member:
    discount = purchase_value * 0.2
elif purchase_value >= 100 and not member:
    discount = purchase_value * 0.1
else:
    discount = 0
print("4.3 Compra:", purchase_value, "| Socio:", member, "-> Descuento:", discount)


# ---------------------------------------------------------------
# 5. OTROS OPERADORES LÓGICOS: OR y NOT
# ---------------------------------------------------------------
print("\n5. OPERADORES LÓGICOS: OR y NOT")

# 5.1 OR: descuento si la compra es de 100 o más O el comprador es socio
purchase_value = 50
member = True
discount = 0
if purchase_value >= 100 or member:
    discount = purchase_value * 0.2
print("5.1 OR  -> Compra:", purchase_value, "| Socio:", member, "-> Descuento:", discount)

# 5.2 'if member:' equivale a 'if member == True:'
member = True
print("\n5.2 member vale", member)
if member:
    print("   if member -> verdadero")
if not member:
    print("   if not member -> verdadero")
else:
    print("   if not member -> falso")

member = False
print("\n5.3 member vale", member)
if member:
    print("   if member -> verdadero")
else:
    print("   if member -> falso")
if not member:
    print("   if not member -> verdadero (se lee como 'si no es socio')")

