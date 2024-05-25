from KarnaughTemplate import KarnaughTemplate, BooleanExpression


class Karnaugh2(KarnaughTemplate):
    def __init__(self, exp: BooleanExpression, form_to_minimize: str):
        self.header_line = ['0', '1']
        self.header_column = ['0', '1']
        super().__init__(exp, form_to_minimize)
        self.map: list[list[int]] = self.build_map()

    def build_map(self) -> list[list[int]]:
        for i in self.header_column:
            for j in self.header_line:
                self.index_chain_for_iteration.append(self.to_decimal_form(i + j))
        table = []
        counter = 0
        for i in range(len(self.header_column)):
            table.append([])
            for j in range(len(self.header_line)):
                table[i].append(self.result_values[self.index_chain_for_iteration[counter]])
                counter += 1
        return table

    def get_variables_after_merge(self) -> list[list[str]]:
        fields: list[list[tuple]] = self.form_final_normal_form_fields()
        value = '1' if self.form_to_minimize == 'SDNF' else '0'
        variables: list[list[str]] = []
        for i in range(len(fields)):
            initial_values: list[str] = [self.header_column[fields[i][0][0]], self.header_line[fields[i][0][1]]]
            changes: list[bool] = [False] * len(self.variables)
            for cell in fields[i]:
                if self.header_line[cell[1]] != initial_values[1]:
                    changes[1] = True
                elif self.header_column[cell[0]] != initial_values[0]:
                    changes[0] = True
            final_variables_from_field: list[str] = []
            for j in range(len(changes)):
                if not changes[j]:
                    final_variables_from_field.append(self.variables[j] if initial_values[j] == value
                                                      else '(!' + self.variables[j] + ')')
            variables.append(final_variables_from_field)
        return variables

    def print_table(self):
        line_to_print = ' ' + self.variables[0] + '\\' + self.variables[1]
        for i in self.header_line:
            line_to_print += '   ' + i
        print(line_to_print)

        line_to_print = '-' * len(line_to_print)
        print(line_to_print)

        for i in range(len(self.header_line)):
            line_to_print = '  ' + self.header_column[i] + ' '
            for j in range(len(self.header_line)):
                line_to_print += ' | ' + str(self.map[i][j])
            print(line_to_print)


# Debug or hand usage mode
#
# expression = BooleanExpression('(a~((!a)|b))')
#
# karnaugh_method_SDNF = Karnaugh2(expression, 'SDNF')
# karnaugh_method_SDNF.print_table()
# print(karnaugh_method_SDNF.merged_form() + '\n')
#
# karnaugh_method_SKNF = Karnaugh2(expression, 'SKNF')
# karnaugh_method_SKNF.print_table()
# print(karnaugh_method_SDNF.merged_form())
