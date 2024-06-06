import unittest
from CalculationMethod import CalculationMethod
from BooleanExpression import BooleanExpression


class CalculationMethodTest(unittest.TestCase):
    def test_SDNF_1(self):
        self.exp = BooleanExpression('(a|(r~s))')
        calculation_method = CalculationMethod(self.exp.build_SDNF(), 'SDNF')
        merged_form = calculation_method.merged_form()
        self.assertEqual(merged_form, '(a|((a&(!s))|(((!r)&(!s))|(r&s))))')

    def test_SDNF_2(self):
        self.exp: BooleanExpression = BooleanExpression('((!a)|(d|(c~a)))')
        calculation_method = CalculationMethod(self.exp.build_SDNF(), 'SDNF')
        merged_form = calculation_method.merged_form()
        self.assertEqual(merged_form, '((!a)|(((!a)&(!d))|(d|((!c)|(c|(c&(!d)))))))')

    def test_SKNF_1(self):
        self.exp: BooleanExpression = BooleanExpression('(a|(r~s))')
        calculation_method = CalculationMethod(self.exp.build_SKNF(), 'SKNF')
        merged_form = calculation_method.merged_form()
        self.assertEqual(merged_form, '((a|(r|(!s)))&(a|((!r)|s)))')

    def test_SKNF_2(self):
        self.exp: BooleanExpression = BooleanExpression('((!a)|(d|(c~a)))')
        calculation_method = CalculationMethod(self.exp.build_SKNF(), 'SKNF')
        merged_form = calculation_method.merged_form()
        self.assertEqual(merged_form, '((!a)|(c|d))')
