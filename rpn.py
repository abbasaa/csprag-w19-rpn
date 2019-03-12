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
            tokenatt = colored.fg("blue") + colored.attr("bold")
            if (token == '-'): 
                tokenatt = colored.fg("red") + colored.attr("bold")

            if (token == '*'): 
                tokenatt = colored.fg("medium_purple") + colored.attr("bold")
            
            if (token == '/'): 
                tokenatt = colored.fg("sky_blue_1") + colored.attr("bold")  

            if (token == '^'): 
                tokenatt = colored.fg("light_pink_4") + colored.attr("bold")

            if (token == '%'): 
                tokenatt = colored.fg("dark_violet_1b") + colored.attr("bold")  
            
            print(stylize(arg1, colored.fg("royal_blue_1")) + " " + stylize(token, tokenatt) + " " + stylize(arg2, colored.fg("light_red")))
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
