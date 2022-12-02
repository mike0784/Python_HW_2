n = int(input("Введите число: "))
lst = []
for item in range(-n, n+1):
    lst.append(item)

print(lst)
text = input("Введите индексы: ")
index = []
index = text.split(" ")
result = 1
for item in index:
    if item.isdigit():
        result = result * lst[int(item)]
print(result)
