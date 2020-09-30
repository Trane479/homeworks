def reverse_string(string: str):
    string_to_list = string.split()
    string_to_list.reverse()
    return string_to_list


if __name__ == '__main__':
    input_string = input('Введите строку')
    for word in reverse_string(input_string):
        print(word, end=' ')
