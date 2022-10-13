n = int(input())
array = [float(i) for i in input().split()]
imax = 0
for i in range(1, n):
    if (array[i] >= array[imax]):
        imax = i
for i in range (imax + 1, n):
    array[i] = 0
print(array)
