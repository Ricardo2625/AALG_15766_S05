
# Lista inicial
array = [2, 5, 3, 8, 4, 1,9]

# Algoritmo de ordenamiento burbuja
n = len(array)
for i in range(1, n):
    for j in range(0, n - 1):
        if array[j] > array[j + 1]:
            # Intercambiar elementos
            array[j], array[j + 1] = array[j + 1], array[j]

print("Lista ordenada:", array)