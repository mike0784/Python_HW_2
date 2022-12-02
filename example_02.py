n = int(input("Введите число: "))
result = 1
for item in range(1, n+1):
    #print(item)
    result = result * item
    print(result, end=", ")
