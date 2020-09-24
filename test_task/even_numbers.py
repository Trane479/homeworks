def enter_list():
    count = (input('Введите длину списка: '))
    input_list_of_numbers = []
    i = 0

    while i < int(count):
        input_number = (input(f'Введите {i} элемент списка: '))
        if not input_number.isdigit():
            print('Введите число')
            continue
        else:
            input_list_of_numbers.append(int(input_number))

        i += 1
    return input_list_of_numbers


def even_numbers(list_of_numbers):
    even_numbres_list = []
    for number in list_of_numbers:
        if int(number) % 2 == 0:
            even_numbres_list.append(number)
        elif number == 257:
            break

    return even_numbres_list


if __name__ == '__main__':
    print(even_numbers(enter_list()))