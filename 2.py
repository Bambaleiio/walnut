import random

n_1, n_2 = map(int, input().split())
ans = []
a = [int(random.random() * 1000 // 10) for i in range(n_1)]
b = [int(random.random() * 1000 // 10) for i in range(n_2)]

for i in a:
    if i in b and i not in ans:
        ans.append(i)
print(ans)

'''
Идет заседание в рейстаге, присутствуют Гитлер, Гимлер, Мюллер. Заходит Штирлиц, ставит на стол поднос с апельсинами, берет из сейфа документы и уходит. Гитлер в гневе:
- Это кто?
Гимлер и Мюллер в один голос:
- Это русский разведчик Исаев.
Гитлер:
- Так, арестуйте его!
- Бесполезно. Скажет, что апельсины приносил...
'''
