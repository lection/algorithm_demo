def decode_string_1(s):
    length = len(s)

    def sub_fn(i):
        times = 0
        r = ''
        while i < length:
            w = s[i]
            i = i + 1
            if w == '[':
                sr, i = sub_fn(i)
                r += (times if times != 0 else 1) * sr
                times = 0
            elif w == ']':
                return r, i
            elif str.isnumeric(w):
                times = times * 10 + int(w)
            else:
                r += w
        return r, i

    result, _ = sub_fn(0)
    return result


def decode_string_2_iterator(s):
    def sub_fn(si):
        times = 0
        r = ''
        while True:
            try:
                w = next(si)
                if w == '[':
                    r += (times if times > 0 else 1) * sub_fn(si)
                    times = 0
                elif w == ']':
                    return r
                elif str.isnumeric(w):
                    times = times * 10 + int(w)
                else:
                    r += w
            except StopIteration:
                break
        return r

    return sub_fn(iter(s))


def decode_string_3_stack(s):
    stack = []
    times = 0
    r = ''
    for w in s:
        if w == '[':
            stack.append((times, r))
            times = 0
            r = ''
        elif w == ']':
            frame = stack.pop()
            times = frame[0]
            r = frame[1] + (times if times > 0 else 1) * r
            times = 0
        elif str.isnumeric(w):
            times = times * 10 + int(w)
        else:
            r += w
    return r


def exec_test(fn, s, result):
    r = fn(s)
    print(s, r, result == r)


def test(fn):
    exec_test(fn, '3[a]2[bc]', 'aaabcbc')
    exec_test(fn, '3[a2[c]]', 'accaccacc')
    exec_test(fn, '2[abc]3[cd]ef', 'abcabccdcdcdef')
    exec_test(fn, '2[abc]11[c]ef', 'abcabccccccccccccef')


test(decode_string_1)
test(decode_string_2_iterator)
test(decode_string_3_stack)
