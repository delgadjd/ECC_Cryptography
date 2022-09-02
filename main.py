# This is a series of functions that were implemented during Fall 2022 in
# MATH 3320: Error-Correcting Codes and Cryptography at Vanderbilt University

def error_pattern(codeword1, codeword2):
    if len(codeword1) != len(codeword2):
        print("Codewords must be of the same length to generate error pattern")
        return
    
    print("Error pattern: ", end="")
    
    for i in range(len(codeword1)):
        print(int(codeword1[i] != codeword2[i]), end="")


def information_rate():
    pass



error_pattern("001", "101")