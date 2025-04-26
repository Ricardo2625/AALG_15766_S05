
def selection(a):
    n = len(a)
    for j in range(n-1):
        iMin = j
        for i in range(j+1, n):
            if a[i] < a[iMin]:
                iMin = i
            if iMin != j:
                a[i], a[j] = a[j], a[i]

# Lista original
a = [2, 8, 5, 3, 9, 4, 1]

print("Lista original:", a)
selection(a)
print("Lista ordenada:", a)