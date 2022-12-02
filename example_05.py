import random
n = int(input("Введите диапазон массива: "))
arr = []
for item in range(0, n + 1):
    arr.append(random.randint(-100, 100))
print(arr)

for item in range(0, n + 1):
    n1 = random. randint(0, n)
    n2 = random. randint(0, n)
    temp = arr[n1]
    arr[n1] = arr[n2]
    arr[n2] = temp
print(arr)