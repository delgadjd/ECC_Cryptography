# This is a series of functions that were implemented during Fall 2022 in
# MATH 3320: Error-Correcting Codes and Cryptography at Vanderbilt University
import math

from sympy import N

def error_pattern(codeword1, codeword2):
    if len(codeword1) != len(codeword2):
        print("Codewords must be of the same length to generate error pattern")
        return
    
    print("Error pattern: ", end="")

    for i in range(len(codeword1)):
        print(int(codeword1[i] != codeword2[i]), end="")


def information_rate():
    pass



def hamming_bound(n , d):
    t = math.floor((d - 1) / 2)
    numerator = math.pow(2,n)
    denominator = 0
    for i in range(0 , t + 1):
        denominator = denominator + xChooseY(n, i)
    bound = round(numerator / denominator)
    return prevPowerOf2(bound)

def factorial(num):
    if num == 0 or num == 1 :
        return 1
    else:
        return num * factorial(num - 1)

def xChooseY(x, y):
    return factorial(x) / (factorial(y) * factorial(x - y))

def prevPowerOf2(n):
    while (n & n - 1):
        n = n & n - 1       # unset rightmost bit
 
    # `n` is now a power of two (less than or equal to `n`)
    return n

print(hamming_bound(8,3))