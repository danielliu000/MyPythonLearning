def isPalindrome(x):

    reversed_x = str(x)[::-1]
    if reversed_x == str(x):
        return True
    else:
        return False
