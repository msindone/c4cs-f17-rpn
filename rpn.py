#!/usr/bin/python
import readline
import operator
from colored import fg,bg,attr

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
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
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        funct = input("rpn calc> ")
        result = calculate(funct)
        color = bg('red') + fg('white')
        reset = attr('reset')
        print(color + funct + reset)
        print "Result: " + str(result)

if __name__ == '__main__':
    main()
