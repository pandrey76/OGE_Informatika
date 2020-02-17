# Creating universal realization of task 15.2

is_must_present_value = True

title_count_of_values = "Введите количество введённых значений:"
title_of_values = "Введите следующее число:"

min_count_value = 0
max_count_value = 1000

min_enter_value = 0
max_enter_value = 30000


def gettingInputValue(title_str, min_count, max_count):
    """

    :param title_str:
    :param min_count:
    :param max_count:
    :return:
    """
    while True:
        num_str = input(title_str)
        try:
            num = int(num_str)
        except ValueError:
            print("Ошибка, ValueError! Введённая строка не является числом")
            continue
        if type(num) != int:
            print("Ошибка! Введённая строка не является числом")
        else:
            if num <= min_count:
                print("Ошибка! Введённое число должно быть больше ", min_count)
            else:
                if num >= max_count:
                    print("Ошибка! Введённое число должно быть меньше или равно ", max_count)
                else:
                    return num


def isCorrectValue(int_val, ):
    if int_val % 4 == 0:
        return True
    else:
        return False


def constructValueList():
    count = gettingInputValue(title_count_of_values, min_count_value, max_count_value)
    i = 0
    val = None
    is_correct_action_flag = False
    result_value_list = []
    while i != count:

        if not is_must_present_value:
            val = gettingInputValue(title_of_values, min_enter_value, max_enter_value)
        else:
            if (i == count - 1) & (not is_correct_action_flag):
                while not is_correct_action_flag:
                    val = gettingInputValue(title_of_values, min_enter_value, max_enter_value)
                    is_correct_action_flag = isCorrectValue(val)
            else:
                val = gettingInputValue(title_of_values, min_enter_value, max_enter_value)
                if isCorrectValue(val):
                    is_correct_action_flag = True

        i += 1
        result_value_list.append(val)

    return result_value_list


def resultPrint(result_list):
    max_value = 0
    for val in result_list:
        if isCorrectValue(val):
            if max_value < val:
                max_value = val

    if max_value == 0:
        print("Ни одно введённое число не было кратно 4.")
    else:
        print("Максимальное введённое число кратное 4: ", max_value)


resultPrint(constructValueList())