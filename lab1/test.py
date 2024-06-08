import unittest
from BinaryMethods import BinaryMethods


class TestBinaryMethods(unittest.TestCase):

    def test_get_positive_binary(self):
        self.assertEqual(BinaryMethods.get_positive_binary(10), '00000000000000000000000000001010')
        self.assertEqual(BinaryMethods.get_positive_binary(23), '00000000000000000000000000010111')
        self.assertEqual(BinaryMethods.get_positive_binary(127), '00000000000000000000000001111111')

    def test_get_negative_binary(self):
        self.assertEqual(BinaryMethods.get_negative_binary('00000000000000000000000000001010'),
                         '11111111111111111111111111110110')
        self.assertEqual(BinaryMethods.get_negative_binary('00000000000000000000000001111111'),
                         '11111111111111111111111110000001')

    def test_from_decimal_to_binary(self):
        self.assertEqual(BinaryMethods.decimal_to_binary(10), '00000000000000000000000000001010')
        self.assertEqual(BinaryMethods.decimal_to_binary(-10), '11111111111111111111111111110110')
        self.assertEqual(BinaryMethods.decimal_to_binary(0), '00000000000000000000000000000000')

    def test_from_binary_to_decimal(self):
        self.assertEqual(BinaryMethods.binary_to_decimal('00000000000000000000000000001010'), 10)
        self.assertEqual(BinaryMethods.binary_to_decimal('11111111111111111111111111110110'), -10)
        self.assertEqual(BinaryMethods.binary_to_decimal('00000000000000000000000000000000'), 0)
        self.assertEqual(BinaryMethods.binary_to_decimal('01111111111111111111111111111111'), 2147483647)
        self.assertEqual(BinaryMethods.binary_to_decimal('10000000000000000000000000000000'), -2147483648)

    def test_add_binary(self):
        self.assertEqual(BinaryMethods.binary_sum(list('00000000000000000000000000001010'),
                                                  list('00000000000000000000000000001010')),
                         '00000000000000000000000000010100')
        self.assertEqual(BinaryMethods.binary_sum(list('01111111111111111111111111111111'),
                                                  list('00000000000000000000000000000001')),
                         '10000000000000000000000000000000')

    def test_add_decimal(self):
        self.assertEqual(BinaryMethods.decimal_sum(10, 5), 15)
        self.assertEqual(BinaryMethods.decimal_sum(2147483647, 1), -2147483648)

    def test_positive_multiplication_of_numbers(self):
        self.assertEqual(BinaryMethods.positive_multiplication_of_numbers(10, 5), 50)

    def test_multiplication_of_numbers(self):
        self.assertEqual(BinaryMethods.multiplication_of_numbers(10, 5), 50)
        self.assertEqual(BinaryMethods.multiplication_of_numbers(-10, -5), 50)
        self.assertEqual(BinaryMethods.multiplication_of_numbers(10, -5), -50)

    def test_divide_dec(self):
        self.assertEqual(BinaryMethods.divide_decimal(10, 5), 2)
        self.assertEqual(BinaryMethods.divide_decimal(10, -5), -2)
        self.assertEqual(BinaryMethods.divide_decimal(-10, 5), -2)
        self.assertEqual(BinaryMethods.divide_decimal(-10, -5), 2)

    def test_from_fraction_to_bin(self):
        self.assertEqual(BinaryMethods.fraction_to_binary('625'), '101')
        self.assertEqual(BinaryMethods.fraction_to_binary('3125'), '0101')

    def test_find_shift_order(self):
        self.assertEqual(BinaryMethods.find_shift_order('10000000', '10101'), '00000000000000000000000010000110')

    def test_from_decimal_to_float(self):
        self.assertEqual(BinaryMethods.decimal_to_float(1.25), '0 01111111 01000000000000000000000')
        self.assertEqual(BinaryMethods.decimal_to_float(-1.25), '1 01111111 01000000000000000000000')

    def test_from_binary_remainder_to_decimal(self):
        self.assertAlmostEqual(BinaryMethods.binary_fractional_to_decimal('101'), 0.625)

    def test_from_float_to_decimal(self):
        self.assertAlmostEqual(BinaryMethods.float_to_decimal('00111111101000000000000000000000'), 1.25)
        self.assertAlmostEqual(BinaryMethods.float_to_decimal('10111111101000000000000000000000'), -1.25)

    def test_diff_between_shifts_and_mantissa_additions(self):
        mantissa1, mantissa2, exp_result = BinaryMethods.diff_between_shifts_and_mantissa_additions(
            '00111111101000000000000000000000', '10111111101000000000000000000000', -127, -127)
        BinaryMethods.check_first_mantissa_is_less('00111111101000000000000000000000',
                                                   '10111111101000000000000000000000')
        self.assertEqual((mantissa1, mantissa2, exp_result),
                         ('101000000000000000000000', '101000000000000000000000', -127))

    def test_mantissa_addition(self):
        mantissa_sum, exp_result = BinaryMethods.mantissa_addition('0', '1', '01000000000000000000000',
                                                                   '01000000000000000000000', -127)
        BinaryMethods.check_first_exponent_is_less('00111111101000000000000000000000',
                                                   '10111111101000000000000000000000')
        self.assertEqual((mantissa_sum, exp_result), ('00000000000000000000000000000000', 0))

    def test_define_sign(self):
        result_sign = BinaryMethods.define_sign('0', '1', -127, -127, '01000000000000000000000',
                                                '01000000000000000000000')
        self.assertEqual(result_sign, '0')

    def test_binary_float_addition(self):
        # Test case 1: Addition of two positive floats
        result_1 = BinaryMethods.binary_float_addition('00111111101000000000000000000000',
                                                       '00111111000000000000000000000000')
        self.assertEqual(result_1, '00111111111000000000000000000000')

        # Test case 2: Addition of a positive and a negative float
        result_2 = BinaryMethods.binary_float_addition('00111111101000000000000000000000',
                                                       '10111111000000000000000000000000')
        self.assertEqual(result_2, '00111111010000000000000000000000')

        # Test case 3: Addition of two negative floats
        result_3 = BinaryMethods.binary_float_addition('10111111101000000000000000000000',
                                                       '10111111000000000000000000000000')
        self.assertEqual(result_3, '10111111111000000000000000000000')

        # Test case 4: Addition of positive and negative floats giving zero
        result_4 = BinaryMethods.binary_float_addition('00111111101000000000000000000000',
                                                       '10111111101000000000000000000000')
        self.assertEqual(result_4, '00000000000000000000000000000000')

    def test_binary_float_addition2(self):
        # Test case 1: Addition of two positive floats
        result_1 = BinaryMethods.binary_float_addition2(1.5, 2.5)
        self.assertAlmostEqual(result_1, 4.0)

        # Test case 2: Addition of a positive and a negative float
        result_2 = BinaryMethods.binary_float_addition2(3.0, -1.5)
        self.assertAlmostEqual(result_2, 1.5)

        # Test case 3: Addition of two negative floats
        result_3 = BinaryMethods.binary_float_addition2(-2.5, -1.5)
        self.assertAlmostEqual(result_3, -4.0)

        # Test case 4: Addition resulting in zero
        result_4 = BinaryMethods.binary_float_addition2(1.0, -1.0)
        self.assertAlmostEqual(result_4, 0.0)
