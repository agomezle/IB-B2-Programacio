"""
EXCEPCIONES EN PYTHON
"""

print("""
Un programa puede detenerse o dar un resultado inesperado por:
  - Errores lógicos en el código
  - Entradas inesperadas del usuario
  - Indisponibilidad de recursos (archivo no encontrado, impresora no lista...)

DEFINICIONES
  Error lógico ........ error que hace que el programa funcione mal,
                        pero NO lo bloquea. Solo se detecta con pruebas.
  Error de ejecución .. error que ocurre al ejecutar el programa;
                        puede detenerlo de forma inesperada (runtime error).
  Excepción ........... evento inesperado que detiene la ejecución,
                        p. ej. una división entre 0.
  Manejo de excepciones proceso de responder a una excepción para que
                        el sistema no se detenga inesperadamente.

ERROR vs EXCEPCIÓN (idea clave)
  "Excepción"            = el EVENTO que interrumpe el programa.
  "Manejo de excepciones" = la ACCIÓN para tratarlo (try/except).

ESTRUCTURA EN PYTHON
  try:      código que podría fallar
  except:   qué hacer si falla
  else:     se ejecuta si NO hubo excepción
  finally:  se ejecuta SIEMPRE, haya o no error

NOTAS
  - Puede usarse solo try/except.
  - No es obligatorio indicar el tipo de error, pero es útil para depurar
    y para que el usuario entienda el problema.
  - Objetivo: mantener el flujo normal del programa. Aunque la operación
    falle, el usuario sabe qué pasó y puede seguir con otras funciones.
""")

# ---------------------------------------------------------------------
# Ejemplo de error lógico (no lanza excepción, pero el resultado no es correcto)
# ---------------------------------------------------------------------
a = 6
b = 9
c = 12
print("EJEMPLO DE ERROR LÓGICO (media de 6, 9 y 12)")
print("  Incorrecto (/ 2):", (a + b + c) / 2, " <- no falla, pero está mal")
print("  Correcto   (/ 3):", (a + b + c) / 3)

# ---------------------------------------------------------------------
# Ejemplo de capturar la excepción (try / except / else / finally)
# ---------------------------------------------------------------------
print("\nEJEMPLO CAPTURAR EXCEPCIÓN - try / except / else / finally")

print("\n Divisor = 5")
try:
    resultado = 100 / 5
except ZeroDivisionError:
    print("[except] No se puede dividir entre 0.")
else:
    print(f"[else] Todo bien. Resultado = {resultado}")
finally:
    print("[finally] Esto se ejecuta siempre.")

print("\n Divisor = 0")
try:
    resultado = 100 / 0
except ZeroDivisionError:
    print("[except] No se puede dividir entre 0.")
else:
    print(f"[else] Todo bien. Resultado = {resultado}")
finally:
    print("[finally] Esto se ejecuta siempre.")

# =====================================================================
# TIPOS DE EXCEPCIONES EN PYTHON (aquí las provocamos a propósito para probar)
# =====================================================================
print("===TIPOS DE EXCEPCIONES EN PYTHON===")
print("""
  Problema                                Excepción en Python
  -----------------------------------  ---------------------------
  División entre 0 .................... ZeroDivisionError
  Texto en lugar de un número ......... ValueError
  Archivo no encontrado / ruta incorrecta ... FileNotFoundError
  Desbordamiento (overflow) ........... OverflowError
  Clase o módulo no encontrado ........ ImportError
  Dispositivo no disponible (impresora) OSError
 
  Truncamiento y subdesbordamiento (underflow): en Python no lanzan
  excepción (int(3.9) da 3; un número diminuto pasa a 0.0).
""")
 
# ---- ZeroDivisionError ----
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("ZeroDivisionError -> división entre cero")
    print("  mensaje:", e)
 
# ---- ValueError ----
try:
    int("hola")
except ValueError as e:
    print("\nValueError -> el usuario escribe texto en lugar de un número")
    print("  mensaje:", e)
 
# ---- FileNotFoundError ----
try:
    open("archivo_que_no_existe.txt")
except FileNotFoundError as e:
    print("\nFileNotFoundError -> el archivo o la ruta no existe")
    print("  mensaje:", e)
 
# ---- OverflowError ----
try:
    import math
    math.exp(1000)
except OverflowError as e:
    print("\nOverflowError -> el resultado es demasiado grande")
    print("  mensaje:", e)
 
# ---- ImportError ----
try:
    import modulo_que_no_existe
except ImportError as e:
    print("\nImportError -> no se encuentra el módulo/clase a cargar")
    print("  mensaje:", e)
 
# ---- OSError (dispositivo no disponible) ----
print("\nOSError -> problema del sistema, p. ej. dispositivo no disponible")
print("  (FileNotFoundError es un caso concreto de OSError)")
 
# ---- Truncamiento y underflow ----
print("\nTruncamiento y underflow (no lanzan excepción en Python):")
print("  int(3.9)  ->", int(3.9), " (se pierde la parte decimal)")
print("  1e-400    ->", 1e-400, " (underflow: pasa a 0.0)")
 
# ---- Lanzar una excepción manualmente con raise ----
try:
    anyo_nacimiento = 2050
    if anyo_nacimiento > 2026:
        raise ValueError("El año de nacimiento no puede ser futuro")
except ValueError as e:
    print("\nraise -> lanzar una excepción manualmente")
    print("mensaje:", e)


# =====================================================================
# RIESGOS DE MOSTRAR MENSAJES DETALLADOS
# =====================================================================
print("===RIESGO: MENSAJES DETALLADOS AL USUARIO FINAL===")
try:
    open("/ruta/interna/servidor/config_secreta.ini")
except FileNotFoundError as e:
    print("Detalle técnico (solo para logs):", e)
    print("Mensaje seguro para el usuario  : No se pudo cargar la configuración.")
print("""
  Mostrar el detalle completo puede revelar rutas internas y la estructura
  del sistema, ayudar a un atacante y confundir a usuarios no técnicos.
""")
 
