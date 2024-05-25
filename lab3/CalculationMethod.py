from BooleanExpression import BooleanExpression


class CalculationMethod:
    def __init__(self, expression, form_to_minimize: str):
        self.__form_to_minimize = form_to_minimize
        self.__exp = expression
        self.__sub_expressions = self.__split_expression()
        self.__sub_expressions_variables = self.__split_sub_expressions_variables()
        self.__sub_expressions_values = self.__replace_variables_by_values()
        self.__father_indexes: dict = {self.__sub_expressions_variables[i].__str__(): [i]
                                       for i in range(len(self.__sub_expressions_variables))}
        self.__sub_expressions_variables_after_merge, self.__sub_expressions_values_after_merge = self.merge()

    def __split_expression(self) -> list[str]:
        sub_expressions = []
        sub_exp = ''
        separator = '|' if self.__form_to_minimize == 'SDNF' else '&'
        for char in self.__exp:
            if char == separator:
                sub_expressions.append(sub_exp)
                sub_exp = ''
            else:
                sub_exp += char

        if sub_exp != '':
            sub_expressions.append(sub_exp)
        return sub_expressions

    def __split_sub_expressions_variables(self) -> list[list[str]]:
        variables = []
        for i in range(len(self.__sub_expressions)):
            variables.append([])
            sub_exp = self.__sub_expressions[i]
            for j in range(len(sub_exp)):
                if 'a' <= sub_exp[j] <= 'z':
                    variables[i].append(('(!' + sub_exp[j] + ')') if sub_exp[j - 1] == '!' else sub_exp[j])
        return variables

    def __replace_variables_by_values(self) -> list[list[int]]:
        sub_expressions_values = []
        for i in range(len(self.__sub_expressions_variables)):
            sub_expressions_values.append([])
            for variable in self.__sub_expressions_variables[i]:
                sub_expressions_values[i].append(1 if len(variable) == 1 else 0)
        return sub_expressions_values

    def merge(self) -> (list[list[str]], list[list[bool]]):
        variables, values = self.__sub_expressions_variables, self.__sub_expressions_values
        loop_exit = False
        while not loop_exit:
            variables, values, loop_exit = self.uniting(variables, values)
        new_values, new_variables = values.copy(), variables.copy()
        for i in range(len(new_values)):
            # mark by -1 value of variable to unite
            count_minus_1 = 0
            for j in new_values[i]:
                if j == -1:
                    count_minus_1 += 1
            if len(new_values[i]) - count_minus_1 != len(new_variables[i]):
                values.remove(new_values[i])
                variables.remove(new_variables[i])
        return variables, values

    def uniting(self, expressions_variables: list[list[str]], expressions_values: list[list[int]]):
        united_expression_variables = []
        united_expression_values = []
        loop_exit = False
        used = [False] * len(expressions_variables)
        for i in range(len(expressions_variables) - 1):
            for j in range(i + 1, len(expressions_variables)):
                ready_status, dif_val_pos, dif_var_pos = self.check_ready_for_unite(expressions_values[i],
                                                                                expressions_values[j],
                                                                                len(expressions_variables[i]) - 1)
                if ready_status:
                    i_father_indexes = self.__father_indexes[expressions_variables[i].__str__()][:]
                    j_father_indexes = self.__father_indexes[expressions_variables[j].__str__()]
                    for index in j_father_indexes:
                        if index not in i_father_indexes:
                            i_father_indexes.append(index)

                    used[i], used[j] = True, True
                    temp_uniting_variables, temp_uniting_values = self.get_uniting_lists(expressions_variables[i],
                                                                                         expressions_values[i],
                                                                                         dif_val_pos,
                                                                                         dif_var_pos)
                    united_expression_variables.append(temp_uniting_variables)
                    united_expression_values.append(temp_uniting_values)
                    self.__father_indexes[temp_uniting_variables.__str__()] = i_father_indexes
        not_used_amount = 0
        for i in range(len(used)):
            if not used[i]:
                not_used_amount += 1
                united_expression_variables.append(expressions_variables[i])
                united_expression_values.append(expressions_values[i])
        if not_used_amount == len(used):
            loop_exit = True
        return united_expression_variables, united_expression_values, loop_exit

    @staticmethod
    def check_ready_for_unite(first_exp_values: list[int], sec_exp_values: list[int], asked_amount_of_variables: int):
        if CalculationMethod.minus_indexes(first_exp_values) != CalculationMethod.minus_indexes(sec_exp_values):
            return False, 0, 0
        dif_value_pos = 0
        present_count_of_variables = 0
        for i in range(len(first_exp_values)):
            if first_exp_values[i] != -1 and sec_exp_values[i] != -1:
                if first_exp_values[i] == sec_exp_values[i]:
                    present_count_of_variables += 1
                else:
                    dif_value_pos = i
        minuses_amount_before_difference = 0
        for i in range(dif_value_pos):
            if first_exp_values[i] == -1:
                minuses_amount_before_difference += 1
        if present_count_of_variables != asked_amount_of_variables:
            return False, 0, 0
        dif_variable_pos = dif_value_pos - minuses_amount_before_difference
        return True, dif_value_pos, dif_variable_pos

    @staticmethod
    def minus_indexes(values: list[int]) -> list[int]:
        # mark by -1 value of variable to unite
        indexes = []
        for i in range(len(values)):
            if values[i] == -1:
                indexes.append(i)
        return indexes

    @staticmethod
    def get_uniting_lists(expressions_variables: list[str], expression_values: list[int], dif_value_pos: int,
                          dif_var_pos: int) -> (list[str], list[bool]):
        uniting_variables = []
        uniting_values = expression_values[:]
        for i in range(len(expressions_variables)):
            if i != dif_var_pos:
                uniting_variables.append(expressions_variables[i])
            elif i == dif_value_pos:
                # mark by -1 value of variable to unite
                uniting_values[i] = -1
        return uniting_variables, uniting_values

    def merged_form(self):
        final_form = ''
        sub_expressions: list[list[str]] = []
        separator = '|' if self.__form_to_minimize == 'SDNF' else '&'
        inside_separator = '&' if self.__form_to_minimize == 'SDNF' else '|'
        for sub_epx in self.__sub_expressions_variables_after_merge:
            sub_expressions.append(sub_epx)
        for i in range(len(sub_expressions) - 1):
            inside_exp = ''
            for j in range(len(sub_expressions[i]) - 1):
                inside_exp += '(' + sub_expressions[i][j] + inside_separator
            inside_exp += sub_expressions[i][-1] + ')' * (len(sub_expressions[i]) - 1)  # list[-1] -> last el from list
            final_form += '(' + inside_exp + separator

        inside_exp = ''
        last_sub_exp = sub_expressions[len(sub_expressions) - 1]
        for i in range(len(last_sub_exp) - 1):
            inside_exp += '(' + last_sub_exp[i] + inside_separator
        inside_exp += last_sub_exp[-1] + ')' * (len(last_sub_exp) - 1)

        final_form_is_empty = len(final_form) == 0
        final_form += ('(' if final_form_is_empty else '') + inside_exp
        final_form += ')' * (len(sub_expressions) - 1 + int(final_form_is_empty))
        if len(sub_expressions) == 1:
            final_form = final_form[1:len(final_form) - 1]
        return final_form

    @property
    def form_to_minimize(self):
        return self.__form_to_minimize

    @property
    def sub_expressions(self):
        return self.__sub_expressions

    @property
    def father_indexes(self):
        return self.__father_indexes

    @property
    def sub_expressions_variables(self):
        return self.__sub_expressions_variables

    @property
    def sub_expressions_values(self):
        return self.__sub_expressions_values

    @property
    def sub_expressions_variables_after_merge(self):
        return self.__sub_expressions_variables_after_merge


# Debug or hand usage mode

# expression = BooleanExpression('(a&(b>(c|f)))')
#
# SDNF = expression.build_SDNF()
# print('SDNF\n' + SDNF)
#
# calculation_method = CalculationMethod(SDNF, 'SDNF')
# merged_by_SDNF = calculation_method.merged_form()
# # for (a&(b>(c|f))) correct answer -> a !b v a f v a c
# print('merged by SDNF expression\n' + merged_by_SDNF)
#
# SKNF = expression.build_SKNF()
# print('SKNF\n' + SKNF)
#
# calculation_method = CalculationMethod(SKNF, 'SKNF')
# merged_by_SKNF = calculation_method.merged_form()
# print('merged by SKNF expression\n' + merged_by_SKNF)
