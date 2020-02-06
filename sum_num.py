#coding=UTF-8

__author__ = "Daniel"
__author_email = "danielliu2000@hotmail.com"


import sys

def Sum2num(a,b):
   """
   Given two numbers add them and return a value
   """
   sum = a + b
   return sum


if __name__ == "__main__":

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except (IndexError, ValueError) as e:
        print("You must give two valuse as parameters ")
        print("Example: python SUm2Num.py 3 6")
        sys.exit(1)

    result = Sum2num(num1,num2)
    print(result)
