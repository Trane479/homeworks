from test_task.even_numbers import enter_list as el


def unique_sequence(list_of_numbers: list):
    set_of_numbers = set(list_of_numbers)
    if len(set_of_numbers) == len(list_of_numbers):
        return f'последовательность {set_of_numbers} уникальна'
    else:
        return 'последовательность не уникальна'


if __name__ == '__main__':
    print(unique_sequence(el()))