n = int(input("Введите число: "))
lst = []
result = 0
for item in range(1, n+1):
    i = (1 + 1/item)**item
    result = result + i
    lst.append(i)
print(lst, end=" = ")
print(result)
