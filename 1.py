n = int(input("Введите размерность массива, нажмите ENTER, введите элементы массива,нажмите ENTER "))
array = [float(i) for i in input().split()]
imax = 0
for i in range(1, n):
    if (array[i] >= array[imax]):
        imax = i
        
for i in range (imax + 1, n):
    array[i] = 0
print(array)