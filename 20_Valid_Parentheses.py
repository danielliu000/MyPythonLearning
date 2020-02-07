def isValid(strs):

    brackets = {
        '(': 1, ')': -1,
                '[': 2, ']': -2,
                '{': 3, '}': -3
    }

    temp = []

    if strs == '':
        return True

    for i in strs:
        value = brackets.get(i)

        if value is None:
            return False

        if value > 0:
            temp.append(value)
        else:

            if not temp:
                return False

            if value + temp[-1] != 0:
                return False

            temp.pop()
    return False if temp else True


a = isValid('()')
print(a)
