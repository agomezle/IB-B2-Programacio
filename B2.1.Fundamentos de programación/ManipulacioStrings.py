"""
STRINGS (CADENES DE TEXT).

Teoria clau:
- String: seqüència de caràcters (lletres, números, símbols i espais) que es
    guarda dins d'una variable.
    -> En Python s'escriu entre cometes dobles (" ") o simples (' ').
- Cometes dins d'un text: si volem incloure una cometa dins del text, fem servir
    la barra invertida (\) davant del caràcter:
    \"  ->  cometa doble
    \'  ->  cometa simple
    \\  ->  barra invertida
    \n  ->  salt de línia
- Blocs de text: les cadenes de vàries línies s'escriuen amb cometes dobles
    triples (\"\"\" ... \"\"\").
- Longitud (len): retorna el nombre de caràcters, espais inclosos.
- Concatenació: unir dues o més cadenes de text amb l'operador +.
    -> No es poden concatenar text i números directament: cal convertir el número
        amb str(), o bé fer servir %, str.format() o f-strings.
    -> Amb print() podem mostrar diverses variables separades per comes.
- Subcadena (slicing): obtenir una part del text amb [inici:fi].
    -> La primera posició sempre és la 0.
    -> La posició final NO s'inclou.
- Replace: substitueix un o més caràcters per uns altres.
- Strip: elimina els espais sobrants a l'inici i al final del text.
- Les cadenes són immutables: els mètodes no modifiquen l'original, sinó que
    retornen una còpia nova.
"""

# =====================================================
# 1. COMETES DINS D'UN TEXT (caràcters d'escapament)
# =====================================================
print("Ella va dir: \"Hola!\"")        # \" -> cometa doble
print('L\'exemple és senzill')         # \' -> cometa simple
print("Ruta: C:\\Users\\alumne")       # \\ -> barra invertida

# Alternativa: alternar tipus de cometes evita l'escapament
print('Ella va dir: "Hola!"')
print("L'exemple és senzill")

# \n és el salt de línia
print("Primera línia\nSegona línia")


# =====================================================
# 2. BLOCS DE TEXT (cadenes de vàries línies)
# =====================================================
poema = """Aquesta és la línia 1
Aquesta és la línia 2
Aquesta és la línia 3"""
print(poema)


# =====================================================
# 3. LONGITUD (len)
# =====================================================
text = "Computer Science is fun!"
print("Longitud:", len(text))          # 24 (compta els espais)


# =====================================================
# 4. CONCATENACIÓ
# =====================================================
nom = "Anna"
cognom = "Puig"

# Amb l'operador +
complet = nom + " " + cognom
print(complet)

# Mostrar dues variables sense guardar-les: print amb comes
print(nom, cognom)

# Cadenes + números: no es pot fer "Edat: " + 20 (dóna TypeError)
edat = 20
print("Edat: " + str(edat))                    # amb str()
print("Edat: %d" % edat)                       # operador %
print("Edat: {}".format(edat))                 # str.format
print(f"Edat: {edat}")                         # f-string (la més moderna)


# =====================================================
# 5. SUBCADENA (slicing) - la primera posició és 0
# =====================================================
text = "Computer Science is fun!"
print(text[0])        # 'C'  -> primera lletra
print(text[0:8])      # 'Computer'  -> de la posició 0 a la 7
print(text[9:16])     # 'Science'
print(text[-4:])      # 'fun!'  -> últimes 4 lletres
print(text.split()[0])  # 'Computer' -> primera paraula


# =====================================================
# 6. REEMPLAÇAR (replace)
# =====================================================
print(text.replace("e", "@"))          # Comput@r Sci@nc@ is fun!
print(text.replace("Computer", "Data"))  # funciona amb un o més caràcters


# =====================================================
# 7. ELIMINAR ESPAIS (strip)
# =====================================================
brut = "   Hola món   "
print("[" + brut.strip() + "]")        # [Hola món]
print("[" + brut.lstrip() + "]")       # només esquerra
print("[" + brut.rstrip() + "]")       # només dreta

# =====================================================
# 8. ENTRADA PER TECLAT (input)
# =====================================================
# input() mostra un missatge, espera que l'usuari escrigui i premi Enter,
# i retorna el que ha escrit SEMPRE com a text (str).
nom = input("Com et dius? ")
print("Hola, " + nom + "!")

# Si necessitem un número, cal convertir el text amb int() o float()
edat = int(input("Quants anys tens? "))        # enter
alcada = float(input("Quant medeixes (m)? "))  # decimal
print(f"{nom} té {edat} anys i fa {alcada} m")

# Sense conversió, el número és text i no podem operar amb ell:
anys = input("Anys: ")         # "20" (str)
# print(anys + 1)              # TypeError: no es pot sumar text + número
print(int(anys) + 1)           # correcte: ara és un enter

# Combinació amb el que hem vist abans: strip, len, slicing i replace
frase = input("Escriu una frase: ").strip()    # elimina espais sobrants
print("Longitud:", len(frase))
print("Primera lletra:", frase[0])
print("Amb guions:", frase.replace(" ", "-"))