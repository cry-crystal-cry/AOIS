class BinaryMethods:
    MAX_BITS = 31
    TOTAL_BITS = 32
    FLOAT_BITS = 127
    num_23 = 23
    num_24 = 24
    BIN_127 = '00000000000000000000000001111111'

    @classmethod
    def get_positive_binary(cls, decimal_number: int) -> str:
        binary_number = ""
        while decimal_number > 0:
            remainder = decimal_number % 2
            binary_number = str(remainder) + binary_number
            decimal_number = decimal_number // 2
        binary_number = binary_number.rjust(cls.TOTAL_BITS, "0")
        return binary_number

    @staticmethod
    def add_1(binary_number: str):
        remainder = True
        added_1_number = ''
        for bit in reversed(binary_number):
            if bit == '1' and remainder:
                added_1_number += '0'
            elif bit == '0' and remainder:
                added_1_number += '1'
                remainder = False
            else:
                added_1_number += bit
        return added_1_number

    @staticmethod
    def get_negative_binary(decimal_number: str) -> str:
        inverted_number = ''.join(['1' if bit == '0' else '0' for bit in decimal_number])
        # Add 1 to the inverted bits to get the two's complement
        two_complement_number = BinaryMethods.add_1(inverted_number)
        answer = ''
        for i in reversed(two_complement_number):
            answer += i
        return answer

    @staticmethod
    def decimal_to_binary(decimal_number) -> str:
        if decimal_number >= 0:
            # If the decimal number is positive, return its positive binary representation
            return BinaryMethods.get_positive_binary(decimal_number)
        else:
            # Convert the absolute value of the decimal number to binary and pad with leading zeros
            abs_decimal_number = abs(decimal_number)
            abs_number = BinaryMethods.get_positive_binary(abs_decimal_number)
            return BinaryMethods.get_negative_binary(abs_number)

    @staticmethod
    def binary_to_decimal(binary_number) -> int:
        length_of_number = len(binary_number)
        result = 0
        for i in range(length_of_number):
            if binary_number[i] == '1':
                result += 2 ** (length_of_number - i - 1)
        if binary_number[0] == '1':
            result -= 2 ** length_of_number
        return result

    @staticmethod
    def positive_binary_to_decimal(binary_number: str):
        length_of_number = len(binary_number)
        result = 0
        for i in range(length_of_number):
            if binary_number[i] == '1':
                result += 2 ** (length_of_number - i - 1)
        return result

    @classmethod
    def binary_sum(cls, first_binary: list, second_binary: list) -> str:
        first_binary: list = ['0' for _ in range(cls.TOTAL_BITS - len(first_binary))] + first_binary
        second_binary: list = ['0' for _ in range(cls.TOTAL_BITS - len(second_binary))] + second_binary
        result = ""
        reminder = 0
        for i in range(cls.MAX_BITS, -1, -1):
            sum_bit = int(first_binary[i]) + int(second_binary[i]) + reminder
            if sum_bit >= 2:
                reminder = 1
            else:
                reminder = 0
            result = str(sum_bit % 2) + result
        return result

    @staticmethod
    def decimal_sum(first: int, second: int) -> int:
        first_binary = list(BinaryMethods.decimal_to_binary(first))
        second_binary = list(BinaryMethods.decimal_to_binary(second))
        result: str = BinaryMethods.binary_sum(first_binary, second_binary)
        return BinaryMethods.binary_to_decimal(result)

    @classmethod
    def positive_multiplication_of_numbers(cls, first: int, second: int) -> int:
        result = '0' * cls.TOTAL_BITS
        first_binary: str = BinaryMethods.decimal_to_binary(first)
        second_binary: str = BinaryMethods.decimal_to_binary(second)
        for i in range(cls.MAX_BITS, -1, -1):
            result = list(result)
            # Если текущий бит второго числа равен 1, прибавляем к результату первое число, сдвинутое на i позиций
            if second_binary[i] == '1':
                # Сдвигаем первое число на i позиций влево, добавляя i нулей в конец
                zero_to_fill = '0' * (cls.MAX_BITS - i)
                shifted_first = list(first_binary[(cls.MAX_BITS - i):] + zero_to_fill)
                # Добавляем сдвинутое число к результату
                result = BinaryMethods.binary_sum(result, shifted_first)
            # Возвращаем результат, обрезанный до 32 бит
        result = BinaryMethods.binary_to_decimal(result)
        return result

    @staticmethod
    def multiplication_of_numbers(first: int, second: int) -> int:
        multiplied_result = BinaryMethods.positive_multiplication_of_numbers(abs(first), abs(second))
        if first > 0 and second > 0:
            return multiplied_result
        elif first < 0 and second < 0:
            return multiplied_result
        else:
            return -multiplied_result

    @staticmethod
    def is_less(bin1: str, bin2: str) -> bool:
        bin1 = bin1.lstrip('0')
        bin2 = bin2.lstrip('0')
        if len(bin1) != len(bin2):
            return len(bin1) < len(bin2)
        return bin1 < bin2

    @classmethod
    def divide_bin(cls, first: str, second: str):
        if first == cls.decimal_to_binary(0):
            raise ZeroDivisionError("Division by zero")
        if first == second:
            return cls.decimal_to_binary(1)

        remainder, result = '', ''
        first += '00000'

        for i in range(len(first)):
            current = remainder + first[i]
            # Если текущее значение меньше b, добавляем следующий бит и переходим к следующей цифре
            if cls.is_less(current, second):
                remainder = current
                result += '0'
                continue
            # Иначе, вычитаем b из текущего значения и добавляем единицу к результату
            remainder = BinaryMethods.binary_sum(
                list(current.zfill(32)),
                list(BinaryMethods.get_negative_binary(second.zfill(32)))
            )
            remainder = ''.join(remainder).lstrip('0')
            result += '1'

        float_path = result[-5:]
        result = result[:-5].zfill(32)
        return result, float_path

    @staticmethod
    def divide_decimal(first, second):
        result, float_path = BinaryMethods.divide_bin(BinaryMethods.decimal_to_binary(abs(first)),
                                                      BinaryMethods.decimal_to_binary(abs(second)))
        result = BinaryMethods.binary_to_decimal(result)
        result += BinaryMethods.binary_fractional_to_decimal(float_path)

        if first > 0 and second > 0:
            return result
        elif first < 0 and second < 0:
            return result
        else:
            return -result

    @classmethod
    def fraction_to_binary(cls, fraction_part: str):
        fraction_part = float(f'0.{fraction_part}')
        result = ""
        while fraction_part != 0 and len(result) < cls.FLOAT_BITS:
            fraction_part *= 2
            if fraction_part >= 1:
                result += "1"
                fraction_part -= 1
            else:
                result += "0"
        return result

    @classmethod
    def find_shift_order(cls, binary_int: str, binary_fractional: str) -> str:
        if binary_int != '0':
            exponent = len(binary_int.lstrip()) - 1
        else:
            fractional = binary_fractional
            exponent = 0
            for i in range(len(fractional)):
                if fractional[i] != '0':
                    exponent = i
                    break
            exponent = -exponent - 1
        shift_order = BinaryMethods.decimal_to_binary(BinaryMethods.decimal_sum(cls.FLOAT_BITS, exponent))
        return shift_order

    @classmethod
    def decimal_to_float(cls, decimal_num: float) -> str:
        if decimal_num >= 0:
            result = '0'
        else:
            result = '1'
        int_number = BinaryMethods.decimal_to_binary(abs(int(decimal_num)))
        int_number = int_number[int_number.find('1'):]

        fractional_number = BinaryMethods.fraction_to_binary(
            str(decimal_num)[str(decimal_num).find('.') + 1:])

        if int_number == '0' and fractional_number == '0':
            return '0' * cls.TOTAL_BITS

        shift_order = BinaryMethods.find_shift_order(int_number, fractional_number)[cls.num_24:]
        result = result + ' ' + shift_order

        mantissa = str(int(int_number + fractional_number))[1:cls.num_24]
        mantissa = mantissa.ljust(cls.num_23, '0')
        result = result + ' ' + mantissa
        return result

    @staticmethod
    def binary_fractional_to_decimal(binary_remainder):
        decimal_remainder = 0
        for i in range(len(binary_remainder)):
            if binary_remainder[i] == '1':
                decimal_remainder += 2 ** (-i - 1)
        return decimal_remainder

    @classmethod
    def float_to_decimal(cls, float_number_binary: str) -> float:
        float_number_binary = float_number_binary.replace(' ', '')
        if float_number_binary == cls.num_23 * '0':
            return 0.0

        exponent = float_number_binary[1:9]
        shift = -BinaryMethods.binary_to_decimal(BinaryMethods.binary_sum(list(cls.BIN_127),
                                                                          list(BinaryMethods.get_negative_binary(
                                                                              exponent.rjust(cls.TOTAL_BITS, '0')))))
        if shift > 0:
            integer_part = '1' + float_number_binary[9:][:shift]
            fractional_part = float_number_binary[9:][shift:]
        elif shift < 0:
            integer_part = '0'
            fractional_part = '0' * (abs(shift) - 1) + '1' + float_number_binary[9:]
        else:
            integer_part = '1'
            fractional_part = float_number_binary[9:]

        result = float(
            str(BinaryMethods.binary_to_decimal(integer_part.rjust(cls.TOTAL_BITS, '0'))) + str(
                BinaryMethods.binary_fractional_to_decimal(fractional_part))[1:])

        if float_number_binary[0] == '0':
            return result
        else:
            return -result

    @classmethod
    def search_of_initial_arguments(cls, first_number: str, second_number: str):
        first_number_sign = first_number[0]
        second_number_sign = second_number[0]
        first_exponent = -BinaryMethods.binary_to_decimal(BinaryMethods.binary_sum(list(cls.BIN_127),
                                                                         list(BinaryMethods.get_negative_binary(
                                                                             first_number[1:9].rjust(cls.TOTAL_BITS, '0')))))
        second_exponent = -BinaryMethods.binary_to_decimal(BinaryMethods.binary_sum(list(cls.BIN_127),
                                                                         list(BinaryMethods.get_negative_binary(
                                                                             second_number[1:9].rjust(cls.TOTAL_BITS, '0')))))
        return first_number_sign, second_number_sign, first_exponent, second_exponent

    @staticmethod
    def diff_between_shifts_and_mantissa_additions(first_number: str, second_number: str, first_exponent: int,
                                                   second_exponent: int):
        first_mantissa = '1' + first_number[9:]
        second_mantissa = '1' + second_number[9:]
        if first_exponent > second_exponent:
            diff = BinaryMethods.binary_sum(list(str(BinaryMethods.decimal_to_binary(first_exponent))),
                                            list(BinaryMethods.get_negative_binary(
                                                str(BinaryMethods.decimal_to_binary(second_exponent)))))  # exp1 - exp2

            decimal_diff = BinaryMethods.binary_to_decimal(diff)
            second_mantissa = '0' * decimal_diff + second_mantissa[:-decimal_diff]
            exponent_for_two = first_exponent
        elif first_exponent < second_exponent:
            diff = BinaryMethods.binary_sum(list(str(BinaryMethods.decimal_to_binary(second_exponent))),
                                            list(BinaryMethods.get_negative_binary(
                                                str(BinaryMethods.decimal_to_binary(first_exponent)))))  # exp2 - exp1
            decimal_diff = BinaryMethods.binary_to_decimal(diff)
            first_mantissa = '0' * decimal_diff + first_mantissa[:-decimal_diff]
            exponent_for_two = second_exponent
        else:
            exponent_for_two = first_exponent
        return first_mantissa, second_mantissa, exponent_for_two

    @classmethod
    def check_which_mantissa_is_less(cls, first_number: str, second_number: str):
        first_mantissa = '1' + first_number[9:]
        second_mantissa = '1' + second_number[9:]
        first_mantissa = first_mantissa.lstrip('0')
        second_mantissa = second_mantissa.lstrip('0')
        if len(first_mantissa) != len(second_mantissa):
            return len(first_mantissa) < len(second_mantissa)
        return first_mantissa < second_mantissa

    @classmethod
    def check_which_exponent_is_less(cls, first_number: str, second_number: str):
        first_sign, second_sign, first_exponent, second_exponent = \
            BinaryMethods.search_of_initial_arguments(first_number, second_number)
        if first_sign == second_sign:
            if first_exponent == '1':
                return first_exponent < second_exponent
            else:
                return first_exponent > second_exponent
        else:
            if first_exponent == '1':
                return False
            else:
                return True

    @classmethod
    def mantissa_addition(cls, first_sign: str, second_sign: str, first_mantissa: str, second_mantissa: str,
                          exponent_for_two: int):
        if first_sign == second_sign:
            mantissa_sum = BinaryMethods.binary_sum(list(first_mantissa.rjust(cls.TOTAL_BITS, '0')),
                                                    list(second_mantissa.rjust(cls.TOTAL_BITS, '0')))
        elif int(first_mantissa) < int(second_mantissa):
            mantissa_sum = BinaryMethods.binary_sum(list(second_mantissa.rjust(cls.TOTAL_BITS, '0')),
                                                    list(BinaryMethods.get_negative_binary(
                                                        first_mantissa.rjust(cls.TOTAL_BITS, '0'))))
        elif int(first_mantissa) > int(second_mantissa):
            mantissa_sum = BinaryMethods.binary_sum(list(first_mantissa.rjust(cls.TOTAL_BITS, '0')),
                                                    list(BinaryMethods.get_negative_binary(
                                                        second_mantissa.rjust(cls.TOTAL_BITS, '0'))))
        else:
            return '0' * cls.TOTAL_BITS, 0

        mantissa_sum = mantissa_sum[mantissa_sum.find('1'):]
        addition_shift = len(mantissa_sum) - cls.num_24

        if addition_shift < 0:
            mantissa_sum += '0' * abs(addition_shift)

        mantissa_sum = mantissa_sum[:cls.num_24]
        exponent_for_two = exponent_for_two + addition_shift
        return mantissa_sum, exponent_for_two

    @staticmethod
    def define_sign(first_sign: str, second_sign: str, first_exponent: int, second_exponent: int, first_mantissa: str,
                    second_mantissa: str):
        if first_sign == second_sign:
            result_sign = first_sign
        else:
            if first_exponent < second_exponent:
                result_sign = second_sign
            elif first_exponent > second_exponent:
                result_sign = first_sign
            else:
                if int(first_mantissa) < int(second_mantissa):
                    result_sign = second_sign
                else:
                    result_sign = first_sign
        return result_sign

    @classmethod
    def binary_float_addition(cls, first_number: str, second_number: str) -> str:
        first_number = first_number.replace(' ', '')
        second_number = second_number.replace(' ', '')

        if int(first_number) == 0 and int(second_number) == 0:
            return '0' * cls.TOTAL_BITS

        first_sign, second_sign, first_exponent, second_exponent = \
            BinaryMethods.search_of_initial_arguments(first_number, second_number)

        first_mantissa, second_mantissa, exponent_for_two = \
            BinaryMethods.diff_between_shifts_and_mantissa_additions(first_number, second_number, first_exponent,
                                                                     second_exponent)
        mantissa_sum, exponent_for_two = \
            BinaryMethods.mantissa_addition(first_sign, second_sign, first_mantissa, second_mantissa, exponent_for_two)

        if int(mantissa_sum) == 0:
            return '0' * cls.TOTAL_BITS

        result_sign = BinaryMethods.define_sign(first_sign, second_sign, first_exponent, second_exponent,
                                                first_mantissa, second_mantissa)
        shift_result = BinaryMethods.binary_sum(list(BinaryMethods.decimal_to_binary(exponent_for_two)),
                                                list('01111111'))  # итоговое значение сдвига

        result_mantissa = mantissa_sum[1:]

        result = result_sign + shift_result[-8:] + result_mantissa
        return result

    @staticmethod
    def binary_subtraction(binary_number1: str, binary_number2: str) -> str:
        # Преобразуем второе число в отрицательное дополнение до двух
        inverted_binary2 = ''.join('1' if bit == '0' else '0' for bit in binary_number2)
        negative_binary2 = BinaryMethods.add_1(inverted_binary2)

        result = BinaryMethods.binary_sum(list(binary_number1), list(negative_binary2))
        # Проверяем знак результата и возвращаем его
        if result[0] == '1':
            negative_result = ''.join('1' if bit == '0' else '0' for bit in result)
            final_result = BinaryMethods.add_1(negative_result)
            return "-" + final_result.lstrip('0')
        return result.lstrip('0').zfill(BinaryMethods.TOTAL_BITS)

    @staticmethod
    def binary_float_addition2(first_float: float, second_float: float) -> float:
        first_number = BinaryMethods.decimal_to_float(first_float)
        second_number = BinaryMethods.decimal_to_float(second_float)
        result = BinaryMethods.binary_float_addition(first_number, second_number)
        return BinaryMethods.float_to_decimal(result)
