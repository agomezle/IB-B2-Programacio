k = int(input())

array = [""] * k  # Array buit

for i in range(k):
    palabra = input()
    array[i] = palabra  # L'omplim string a string

n = int(input())

for i in range(len(array)):  # Recórrer i accedir a cada valor de l'array seqüencialment
    print(array[i])

print(array[n])  # Accedir directament al valor d'una posició
