class DiagonalMatrix:
    def __init__(self, rows, cols):
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.colums = cols

    def set_word(self, word, start_row, col):
        for i, val in enumerate(word):
            row = (start_row + i) % self.rows
            self.matrix[row][col] = val

    def set_index_colum(self, index, start_row, start_colum):
        for i, val in enumerate(index):
            self.matrix[(start_row + i) % self.rows][(start_colum + i) % self.colums] = val

    def get_word(self, start_row, col, length):
        return [self.matrix[(start_row + i) % self.rows][col] for i in range(length)]

    def get_index_column(self, start_row, start_colum, length):
        return [self.matrix[(start_row + i) % self.rows][(start_colum + i) % self.colums] for i in range(length)]

    def logical_or(self, col1, col2):
        word1 = self.get_word(col1, col1, self.rows)
        word2 = self.get_word(col2, col2, self.rows)
        word3 = [int(bool(word1[i]) | bool(word2[i])) for i in range(self.rows)]
        return word3

    def logical_or_not(self, col1, col2):
        word1 = self.get_word(col1, col1, self.rows)
        word2 = self.get_word(col2, col2, self.rows)
        word3 = [int(not (bool(word1[i]) | bool(word2[i]))) for i in range(self.rows)]
        return word3

    def logical_not_and(self, col1, col2):
        word1 = self.get_word(col1, col1, self.rows)
        word2 = self.get_word(col2, col2, self.rows)
        word3 = [int(bool(word1[i]) & (not bool(word2[i]))) for i in range(self.rows)]
        return word3

    def implication(self, col1, col2):
        word1 = self.get_word(col1, col1, self.rows)
        word2 = self.get_word(col2, col2, self.rows)
        word3 = [int((not bool(word1[i])) | bool(word2[i])) for i in range(self.rows)]
        return word3

    def add_binary(self, a, b):
        result = []
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            total = a[i] + b[i] + carry
            result.insert(0, total % 2)
            carry = total // 2
        if carry:
            result.insert(0, carry)
        return result

    def sum_fields(self, key_bits):
        for column in range(self.colums):
            word = self.get_word(column, column, self.rows)
            if word[:len(key_bits)] == key_bits:
                length = (len(word) - len(key_bits) - 1) // 3
                A = word[len(key_bits):len(key_bits) + length]
                B = word[len(key_bits) + len(A):len(key_bits) + len(A) + length]
                word = key_bits + A + B + self.add_binary(A, B)
                self.set_word(word, column, column)

    def compare(self, value1: list[int], value2: list[int]):
        for j in range(self.colums):
            g = 0
            l = 0
            for i in range(len(value1)):
                if value1[i] > value2[i]:
                    g = 1
                    break
                elif value1[i] < value2[i]:
                    l = 1
                    break
            if g:
                return 1
            elif l:
                return -1
            else:
                return 0

    def find_words_in_range(self, top: list[int], bottom: list[int]):
        flags = []
        for i in range(self.rows):
            top_compare = self.compare(top, self.get_word(i,i,self.rows))
            bottom_compare = self.compare(bottom,self.get_word(i,i,self.rows))
            if top_compare >= 0 and bottom_compare <= 0:
                flags.append(True)
            else:
                flags.append(False)
        return flags


# Debug or hand-usage mode
#
# matrix = DiagonalMatrix(16, 16)
#
# matrix.set_word([1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], 0, 0)
# matrix.set_word([1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 1, 1)
# matrix.set_word([0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1], 2, 2)
# matrix.set_index_colum([0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1], 1, 0)
# matrix.set_index_colum([1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1], 3, 1)
# print("Матрица после записи слов и адресных столбцов:")
# for row in matrix.matrix:
#     print(row)
#
# print("Слово из столбца 0:", matrix.get_word(0, 0, 16))
# print("Слово из столбца 1:", matrix.get_word(1, 1, 16))
# print("Слово из столбца 2:", matrix.get_word(2, 2, 16))
# print("Адресный столбец 1 из 0 столбца", matrix.get_index_column(1, 0, 16))
# print("Адресный столбец 3 из 1 столбца", matrix.get_index_column(3, 1, 16))
#
# print("Логическое ИЛИ:", matrix.logical_or(1, 2))
# print("Логическое ИЛИ-НЕ:", matrix.logical_or_not(1, 2))
# print("Логическое НЕТ И:", matrix.logical_not_and(1, 2))
# print("Импликация:", matrix.implication(1, 2))
#
# matrix.sum_fields([1, 0, 1])
# print("Матрица после сложения полей:")
# for row in matrix.matrix:
#     print(row)
#
# print(matrix.find_words_in_range([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
#                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))


