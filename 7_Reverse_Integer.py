'''Given a 32-bit signed integer, reverse digits of an integer.'''

class Solution:
    def reverse(self, x: int) -> int:

        import math

        if -math.pow(2,31) < x < math.pow(2,31)-1:
                if x > 0:
                    result = int(str(x).rstrip('0')[::-1])
                    if result < math.pow(2,31)-1:
                        return result
                    else:
                        return 0

                if x < 0:
                    result = 0-int(str(-x).rstrip('0')[::-1])
                    if result > -math.pow(2,31):
                        return result
                    else:
                        return 0

                if x ==0:
                    return 0

        else:
            return 0
