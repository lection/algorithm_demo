from list.pre_expression import pre_exec


def test(ex_str, value):
    result = pre_exec(ex_str)
    print(ex_str, '=', result, result == value)


test('1+2 + 32 * 5 + 3 * (1+26)', 244)
test('1+(2 + 32) * 5 + 3 * (1+26)', 252)
test('12 - 6', 6)
test('1+(2 + 32) - 5 + 3 * (1+26)', 111)
test('1+(2 + 32) / 5 + 3 * (1+26)', 88.8)
