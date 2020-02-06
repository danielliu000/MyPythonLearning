map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def romanToInt(s):
    num, pre = 0, 1000
    for i in [map[j] for j in s]:
        num, pre = num + i - 2 * pre if i > pre else num + i, i
    return num


a = romanToInt('D')
print(a)
'''
def romanToInt(s):

    roman_nums = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    i = 0
    if len(s) == 1:
        sum = roman_nums[s]
        print(sum)
        return
    while i < len(s) - 1:
        if roman_nums[s[i]] < roman_nums[s[i + 1]]:
            sum = sum + roman_nums[s[i + 1]] - roman_nums[s[i]]
            i = i + 2
        else:
            sum += roman_nums[s[i]]
            i = i + 1

    if  roman_nums[s[-2]] < roman_nums[s[-1]]:
        return sum
    else:
        sum = sum + roman_nums[s[-1]]
        return sum


romanToInt('D')
'''
