from Karnaugh4 import Karnaugh4

digital_device_truth_table: list[list[int]] = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
]




def print_digital_device_truth_table():
    print('Таблица истинности цифрового устройства')
    arguments: list[str] = ['q3\'', 'q2\'', 'q1\'', 'V  ', 'q3 ', 'q2 ', 'q1 ', 'h3 ', 'h2 ', 'h1 ']
    for i in range(len(digital_device_truth_table)):
        print_string: str = arguments[i] + ' |'
        for j in range(len(digital_device_truth_table[i])):
            print_string += f' {digital_device_truth_table[i][j]}'
        print(print_string)

def print_h3_minimization():
    print('Минимизация h3:')
    truth_table_str: str = ''
    for i in range(len(digital_device_truth_table[7])):
        truth_table_str += digital_device_truth_table[7][i].__str__()
    karnaugh: Karnaugh4 = Karnaugh4(truth_table_str, 'sdnf')
    print(karnaugh.final_normal_form())

def print_h2_minimization() -> None:
    print('Минимизация h2:')
    truth_table_str: str = ''
    for i in range(len(digital_device_truth_table[8])):
        truth_table_str += digital_device_truth_table[8][i].__str__()
    karnaugh: Karnaugh4 = Karnaugh4(truth_table_str, 'sdnf')
    print(karnaugh.final_normal_form())

def print_h1_minimization() -> None:
    print('Минимизация h1:')
    truth_table_str: str = ''
    for i in range(len(digital_device_truth_table[9])):
        truth_table_str += digital_device_truth_table[9][i].__str__()
    karnaugh: Karnaugh4 = Karnaugh4(truth_table_str, 'sdnf')
    print(karnaugh.final_normal_form())


print_digital_device_truth_table()
print_h3_minimization()
print_h2_minimization()
print_h1_minimization()
