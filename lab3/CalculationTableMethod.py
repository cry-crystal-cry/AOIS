import math
from CalculationMethod import CalculationMethod, BooleanExpression


class CalculationTableMethod:
    def __init__(self, calculation_method: CalculationMethod):
        self.__calculation_method = calculation_method
        self.__form_to_minimize = self.__calculation_method.form_to_minimize
        self.__uniting_variables: list[list[str]] = calculation_method.sub_expressions_variables_after_merge
        self.__parent_indexes: dict = calculation_method.parent_indexes.copy()
        self.__result_variables: list[list[str]] = []

    def merge(self):
        sub_exps: list[str] = self.__calculation_method.sub_expressions
        result_variables: list[str] = [str(i) for i in self.__uniting_variables]
        for i in self.__calculation_method.parent_indexes.keys():
            if i not in result_variables:
                self.__parent_indexes.pop(i)
        sub_exps_amount: list[int] = [0 for _ in range(len(sub_exps))]
        for i in range(len(sub_exps_amount)):
            for j in self.__parent_indexes.values():
                sub_exps_amount[i] += j.count(i)
        indexes_to_append: list[int] = []
        for i in range(len(result_variables)):
            if self.append_index_status(sub_exps_amount, self.__parent_indexes[result_variables[i]]):
                indexes_to_append.append(i)
        for i in indexes_to_append:
            self.__result_variables.append(self.__uniting_variables[i])

    @staticmethod
    def append_index_status(sub_expression_amount, father_indexes) -> bool:
        for i in father_indexes:
            if sub_expression_amount[i] < 2:
                return True
        return False

    def build_table(self):
        key_expressions = [self.exp_fine_brackets(self.__uniting_variables[i])
                           for i in range(len(self.__uniting_variables))]
        column_len = 0
        for exp in key_expressions:
            column_len = max(column_len, len(exp))
        header = ' ' * column_len
        sub_expressions = self.__calculation_method.sub_expressions
        for exp in sub_expressions:
            header += exp + ' '
        print(header)
        for i in range(len(key_expressions)):
            line_to_print = key_expressions[i] + ' ' * (column_len - len(key_expressions[i]))
            for j in range(len(sub_expressions)):
                half = len(sub_expressions[j]) // 2
                line_to_print += ' ' * half
                line_to_print += 'x' if j in self.__parent_indexes[self.__uniting_variables[i].__str__()] else 'O'
                line_to_print += ' ' * (half - 1) + ' ' * (len(sub_expressions[j]) % 2)
                line_to_print += ' '
            print(line_to_print)

    def exp_fine_brackets(self, expression_variables: list[str]) -> str:
        if len(expression_variables) == 1 and len(expression_variables[0]) >= 3:
            return expression_variables[0]
        separator = '&' if self.__form_to_minimize == 'SDNF' else '|'
        str_exp = '(' + expression_variables[0]
        for i in range(1, len(expression_variables)):
            str_exp += separator + expression_variables[i]
        str_exp += ')'
        return str_exp

    def merged_form(self):
        return self.__calculation_method.merged_form()

    @property
    def result_variables(self) -> list[list[str]]:
        return self.__result_variables

    @property
    def united_variables(self) -> list[list[str]]:
        return self.__uniting_variables

    @property
    def parent_indexes(self) -> dict:
        return self.__parent_indexes


# Debug or hand usage mode

# expression = BooleanExpression('(a>(b&c))')
#
# SDNF = expression.build_SDNF()
# calculation_method = CalculationMethod(SDNF, 'SDNF')
# calculation_table_method = CalculationTableMethod(calculation_method)
# # for (a&(b>(c|f))) correct answer -> a !b v a f v a c
# calculation_table_method.build_table()
#
# SKNF = expression.build_SKNF()
# calculation_method = CalculationMethod(SKNF, 'SKNF')
# calculation_table_method = CalculationTableMethod(calculation_method)
# calculation_table_method.build_table()
