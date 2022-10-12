n = int(input())
array = [float(i) for i in input().split()]
imin = 0
for i in range(1, n):
    if (array[i] >= array[imin]):
        imin = i
for i in range (imin + 1, n):
    array[i] = 0
print(array)

# кто прочел тот лох
