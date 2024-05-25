from Karnaugh3 import Karnaugh3
from Karnaugh4 import Karnaugh4

ODS_3_truth_table = \
    [
        [0, 0, 0, 0, 1, 1, 1, 1],  # P_i perenos from previous
        [0, 0, 1, 1, 0, 0, 1, 1],  # A
        [0, 1, 0, 1, 0, 1, 0, 1],  # B
        [0, 1, 1, 0, 1, 0, 0, 1],  # S sum
        [0, 0, 0, 1, 0, 1, 1, 1],  # P_i+1 perenos to the next
    ]

D8421_plus_5_truth_table = \
    [
        [0, 0, 0, 0, 0, 1, 0, 1],  # 4 bit A, 4 bit A+5
        [0, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 1, 0, 0]
    ]

def print_ODS_3_truth_table():
    print('Таблица истинности ОДС-3:')
    bits = ['P_i:  ', 'A:    ', 'B:    ', 'S_sum:', 'P_i+1:']
    for i in range(5):
        line_to_print = ''
        for j in range(len(ODS_3_truth_table[i])):
            line_to_print += str(ODS_3_truth_table[i][j]) + ' '
        print(bits[i] + line_to_print)

def print_S_minimization():
    print('Минимизация для S(результата):')
    S_line: list[int] = []
    for i in range(len((ODS_3_truth_table[0]))):
        S_line.append(int(ODS_3_truth_table[3][i]))
    karnaugh_SDNF, karnaugh_SKNF = Karnaugh3(S_line, 'SDNF'), Karnaugh3(S_line, 'SKNF')
    print('SDNF:\n' + karnaugh_SDNF.merged_form())
    print('SKNF:\n' + karnaugh_SKNF.merged_form())

def print_P_i_minimization():
    print('Минимизация для P_i(переноса бита):')
    P_i_line: list[int] = []
    for i in range(len((ODS_3_truth_table[0]))):
        P_i_line.append(int(ODS_3_truth_table[4][i]))
    karnaugh_SDNF, karnaugh_SKNF = Karnaugh3(P_i_line, 'SDNF'), Karnaugh3(P_i_line, 'SKNF')
    print('SDNF:\n' + karnaugh_SDNF.merged_form())
    print('SKNF:\n' + karnaugh_SKNF.merged_form())

def print_D8421_truth_table():
    print('Таблица истинности Д8421:')
    print('A  B  C  D  A\' B\' C\' D\'')
    for i in range(len(D8421_plus_5_truth_table)):
        line_to_print = ''
        for j in range(len(D8421_plus_5_truth_table[i])):
            line_to_print += str(D8421_plus_5_truth_table[i][j]) + '  '
        print(line_to_print)

def print_D8421_A_minimization():
    print('Минимизация для A\':')
    A_line: list[int] = []
    for i in range(len(D8421_plus_5_truth_table)):
        A_line.append(int(D8421_plus_5_truth_table[i][4]))
    karnaugh_SDNF, karnaugh_SKNF = Karnaugh4(A_line, 'SDNF'), Karnaugh4(A_line, 'SKNF')
    print('SDNF:\n' + karnaugh_SDNF.merged_form())
    print('SKNF:\n' + karnaugh_SKNF.merged_form())

def print_D8421_B_minimization():
    print('Минимизация для B\':')
    B_line: list[int] = []
    for i in range(len(D8421_plus_5_truth_table)):
        B_line.append(int(D8421_plus_5_truth_table[i][5]))
    karnaugh_SDNF, karnaugh_SKNF = Karnaugh4(B_line, 'SDNF'), Karnaugh4(B_line, 'SKNF')
    print('SDNF:\n' + karnaugh_SDNF.merged_form())
    print('SKNF:\n' + karnaugh_SKNF.merged_form())

def print_D8421_C_minimization():
    print('Минимизация для C\':')
    C_line: list[int] = []
    for i in range(len(D8421_plus_5_truth_table)):
        C_line.append(int(D8421_plus_5_truth_table[i][6]))
    karnaugh_SDNF, karnaugh_SKNF = Karnaugh4(C_line, 'SDNF'), Karnaugh4(C_line, 'SKNF')
    print('SDNF:\n' + karnaugh_SDNF.merged_form())
    print('SKNF:\n' + karnaugh_SKNF.merged_form())

def print_D8421_D_minimization():
    print('Минимизация для D\':')
    D_line: list[int] = []
    for i in range(len(D8421_plus_5_truth_table)):
        D_line.append(int(D8421_plus_5_truth_table[i][7]))
    karnaugh_SDNF, karnaugh_SKNF = Karnaugh4(D_line, 'SDNF'), Karnaugh4(D_line, 'SKNF')
    print('SDNF:\n' + karnaugh_SDNF.merged_form())
    print('SKNF:\n' + karnaugh_SKNF.merged_form())

print_ODS_3_truth_table()
print_S_minimization()
print_P_i_minimization()
print_D8421_truth_table()
print_D8421_A_minimization()
print_D8421_B_minimization()
print_D8421_C_minimization()
print_D8421_D_minimization()

