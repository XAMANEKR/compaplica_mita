#imprime la conjetura de collatz

print("imprime la conjetura de collatz")

num = int(input("dame un numero ?"))

while(num > 1):
    print(num)
    if num % 2 == 0:
        num = num // 2
    else:
        num =num * 3 + 1

print("num")

    