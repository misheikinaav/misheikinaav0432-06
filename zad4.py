do = input("Выберите операцию: +, -, /, *, возведение в степень, модуль, рандомное число, факториал и арккосинус: ")
while do != "exit":
    if do == "+":
        number1 = float(input("ввести 1 значение: "))
        number2 = float(input("ввести 2 значение: "))
        print(number1 + number2)
    elif do == "-":
        number1 = float(input("ввести 1 значение: "))
        number2 = float(input("ввести 2 значение: "))
        print(number1 - number2)
    elif do == "/":
        number1 = float(input("ввести 1 значение: "))
        number2 = float(input("ввести 2 значение: "))
        if number2 != 0:
            print(number1 / number2)
        else:
            print("на 0 делить нельзя")
    elif do == "*":
        number1 = float(input("ввести 1 значение: "))
        number2 = float(input("ввести 2 значение: "))
        print(number1 * number2)
    elif do == "pow": #возведение в степень
        number1 = float(input("ввести 1 значение: "))
        number2 = float(input("ввести 2 значение: "))
        print(pow(number1, number2))
    elif do == "module": #модуль
        number1 = float(input("ввести значение: "))
        print(abs(number1))
    elif do == "0": #рандомное число
        print(random.randint(0, 1000))
    elif do == "f": #факториал
        number1 = int(input("ввести  значение: "))
        print(math.factorial(number1))
    elif do == "arccos": #арккосинус
        number1 = float(input("ввести значение: "))
        number11 = number1*math.pi/180
        print(math.acos(number11))
    do = input("Введите следующую операцию или введите exit, что бы закончить: ")
