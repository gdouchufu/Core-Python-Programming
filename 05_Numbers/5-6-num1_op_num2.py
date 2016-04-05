#!/usr/bin/env python
import decimal

def num1_op_num2(op_str):
    arr = op_str.split()
    op = arr[1]
    num1 = decimal.Decimal(arr[0])
    num2 = decimal.Decimal(arr[2])

    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    elif op == '%':
        return num1 % num2
    elif op == '**':
        return num1 ** num2
    else:
        raise ValueError("op don't exist")

print num1_op_num2("3 * 4")
print num1_op_num2("11 % 7")
print num1_op_num2("5 ** 2")