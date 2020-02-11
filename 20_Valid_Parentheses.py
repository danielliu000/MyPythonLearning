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
'''
brackets_pair = {')': '(', ']': '[', '}': '{'}
left_bkt = ['(', '{', '[']


def isValid(s):

    stack = []

    for i in s:
        if i in left_bkt:
            stack.append(i)
        elif i in right_bkt:
            if not stack or stack[-1] != brackets_pair[i]:
                return False
            stack.pop()
        else:
            return False
    return False if not stack else True

'''
a = isValid('()')
print(a)
