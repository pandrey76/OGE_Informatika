# Creating universal realization of task 15.2

is_must_present_value = True

title_count_of_values = "Введите количество введённых значений:"
title_of_values = "Введите следующее число:"

min_count_value = 0
max_count_value = 51

min_enter_value = -1
max_enter_value = 21


def getting_input_value(title_str, min_count, max_count):
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


def construct_value_list():
    count = getting_input_value(title_count_of_values, min_count_value, max_count_value)
    i = 0
    val = None
    is_correct_action_flag = False
    result_value_list = []
    while i != count:
        if not is_must_present_value:
            val = getting_input_value(title_of_values, min_enter_value, max_enter_value)
        else:
            if (i == count - 1) & (not is_correct_action_flag):
                while not is_correct_action_flag:
                    val = getting_input_value(title_of_values, min_enter_value, max_enter_value)
                    is_correct_action_flag = is_correct_value(val)
            else:
                val = getting_input_value(title_of_values, min_enter_value, max_enter_value)
                if is_correct_value(val):
                    is_correct_action_flag = True
        i += 1
        result_value_list.append(val)

    return result_value_list


def is_correct_value(int_val):
    if int_val >= 1:
        return True
    else:
        return False


def getting_result1(result_list):
    value = 0
    for val in result_list:
        if is_correct_value(val):
            if value < val:
                value = val
    return value


def getting_result2(result_list):
    value = 0
    for val in result_list:
        if val == 0:
            return 'YES'
    return 'NO'


list_of_entering_value = construct_value_list()

print(getting_result1(list_of_entering_value))

print(getting_result2(list_of_entering_value))


def getting_min_value(result_list):
    min_value = max_enter_value
    for val in result_list:
        if is_correct_value(val):
            if val < min_value:
                min_value = val
    if min_value == max_enter_value:
        min_value = 0
    return min_value


def getting_max_value(result_list):
    value = 0
    for val in result_list:
        if is_correct_value(val):
            if val > value:
                value = val
    return value
