num = 0
while True:
    num_str = input("Введите количество введённых значений:")
    try:
        num = int(num_str)
    except ValueError:
        print("Ошибка, ValueError! Введённая строка не является числом")
        continue
    if type(num) != int:
        print("Ошибка! Введённая строка не является числом")
    else:
        if num <= 0 :
            print("Ошибка! Введённое число должно быть больше 0")
        else:
            if num > 1000:
                print("Ошибка! Введённое число должно быть меньше или равно 1000")
            else:
                break;

max_value = 0
i = 0
while i != num:
    try:
        number = int(input("Введите следующее число:"))
    except ValueError:
        print("Ошибка, ValueError! Введённая строка не является числом")
        continue
    if type(number) != int:
        print("Ошибка! Введённое значение не является числом")
    else:
        if number > 30000:
            print("Ошибка! Введённое значение должно быть меньше или равнятся 1000")
            continue
        i += 1
        if number % 4 == 0:
            if number > max_value:
                max_value = number
            
if max_value == 0:
    print("Ни одно введённое число не было кратно 4.")
else:
    print("Максимальное введённое число кратное 4: ", max_value)
