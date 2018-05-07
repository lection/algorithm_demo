from list.stack import Stack
import re

EX_REGEX = re.compile('(\d+\.?\d*|[\(\)\+\-\*\/])', re.I + re.M)


def pre_exec(ex_str):
    match_result = re.findall(EX_REGEX, ex_str)
    exe_list = []
    for it in match_result:
        if it.isnumeric():
            if '.' in it:
                exe_list.insert(0, float(it))
            else:
                exe_list.insert(0, int(it))
        else:
            exe_list.insert(0, it)

    _check(exe_list)
    return _exec(exe_list)


def _check(ex_list):
    pass


def _is_add(op):
    return not op or op in ('+', '-', ')')


def _exec(ex_list):
    operator_stack = Stack()
    number_stack = Stack()
    for it in ex_list:
        if isinstance(it, str):
            if it in (')', '*', '/'):
                operator_stack.push(it)
            elif _is_add(it):
                while not _is_add(operator_stack.offer()):
                    number_stack.push(operator_stack.pop())
                operator_stack.push(it)
            else:
                while True:
                    op = operator_stack.pop()
                    if op == ')':
                        break
                    number_stack.push(op)

        else:
            number_stack.push(it)

    while number_stack.offer():
        operator_stack.push(number_stack.pop())

    value_stack = Stack()
    while operator_stack.offer():
        it = operator_stack.pop()
        result = None
        if it == '+':
            result = value_stack.pop() + value_stack.pop()
        elif it == '-':
            result = value_stack.pop() - value_stack.pop()
        elif it == '*':
            result = value_stack.pop() * value_stack.pop()
        elif it == '/':
            result = value_stack.pop() / value_stack.pop()
        if result:
            value_stack.push(result)
        else:
            value_stack.push(it)

    return value_stack.pop()
