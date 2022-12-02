text = input("Введите вещественное число: ")
result = 0
for item in text:
    if item.isdigit():
        result = result + int(item)
print(result)
