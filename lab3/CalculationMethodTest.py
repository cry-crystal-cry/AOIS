import unittest
from CalculationMethod import CalculationMethod
from BooleanExpression import BooleanExpression as BooleanExpression


class CalculationMethodTest(unittest.TestCase):
    def test_SDNF_1(self):
        self.exp = BooleanExpression('(a>(b>c))')
        calculation_method = CalculationMethod(self.exp.build_SDNF(), 'SDNF')
        merged_form = calculation_method.merged_form()
        self.assertEqual(merged_form, '((!a)|((!b)|c))')

    def test_SDNF_2(self):
        self.exp: BooleanExpression = BooleanExpression('(a&(b>(c|d)))')
        calculation_method = CalculationMethod(self.exp.build_SDNF(), 'SDNF')
        merged_form = calculation_method.merged_form()
        self.assertEqual(merged_form, '((a&(!b))|((a&d)|(a&c)))')

    def test_SKNF_1(self):
        self.exp: BooleanExpression = BooleanExpression('(a>(b>c))')
        calculation_method = CalculationMethod(self.exp.build_SKNF(), 'SKNF')
        merged_form = calculation_method.merged_form()
        self.assertEqual(merged_form, '((!a)|((!b)|c))')

    def test_SKNF_2(self):
        self.exp: BooleanExpression = BooleanExpression('(a&(b>(c|d)))')
        calculation_method = CalculationMethod(self.exp.build_SKNF(), 'SKNF')
        merged_form = calculation_method.merged_form()
        self.assertEqual(merged_form, '(a&((!b)|(c|d)))')
