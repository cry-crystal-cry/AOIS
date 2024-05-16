from BooleanExpression import BooleanExpression

expression = input('Введите логическое выражение(для операторов используются символы "!", "&", "|", ">", "~"):\n')
logical_expression = BooleanExpression(expression)

print('Таблица истинности:')
truth_table = logical_expression.truth_table()
for i in truth_table:
    print(i)

print('СДНФ:')
print(logical_expression.build_SDNF())

print('СКНФ:')
print(logical_expression.build_SKNF())

print('Числовые формы:')
SDNF, SKNF = logical_expression.build_numeric_forms()
print(SDNF)
print(SKNF)

print('Индексная форма:')
print(logical_expression.build_index_form())