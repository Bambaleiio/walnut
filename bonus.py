# вводим массив: ввод, полученный в одной строке, разбиваем на целые числа
array = [int(i) for i in input("Enter the array: ").split()] 
# вводим дельту
delta = int(input("Enter the delta: "))

# инициализируем переменную, в которой будем хранить минимальное значение 
# пусть она будет равна первому элементу массива
mmin = array[0]

# проходимся по всему массиву и если mmin < array[k], то mmin = array[k] (i = array[k])
for i in array:
    mmin = min(i, mmin)

# инициализируем переменную в которой будем хранить ответ (cnt от count, ну или cunt тут хз) 
cnt = 0

# если array[k] = min(array) + delta, то увеличиваем ответ на 1
for i in array:
    if mmin + delta == i:
        cnt += 1

# выводим ответ
print(cnt)
