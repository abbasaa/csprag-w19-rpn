#!/usr/bin/env python3

import readline
import operator
import colored
from colored import stylize

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            
            arg2 = stack.pop()
            arg1 = stack.pop()
            print(stylize(arg1, colored.fg("royal_blue_1")) + " " + stylize(token, colored.fg("magenta"))+ " " + stylize(arg2, colored.fg("light_red")))
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
