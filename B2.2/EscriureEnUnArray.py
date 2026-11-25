k = int(input())

array = [0] * k  # Array de ints (estàtic, per això l'omplim amb un nombre determinat de 0)

numeros = input().split(" ")  # Array de strings perquè input és str si no el convertim

for i in range(k):
    array[i] = int(numeros[i])  # Convertir de str a int

n = int(input())

for i in range(k):
    print(f"{array[i]} ", end="")  # end="" --> Per evitar salt de línia

print() # Salt de línia
print(array[n])  # Accedir a posició n
