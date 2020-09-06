
import math
import os
import random
import re
import sys


# def generate_xor_array(r, i):

#     arr    = []
#     arr[0] = 0
#     #i = 1 
#     if i > r:
#         return arr
#     arr[i] = arr[i-1] ^ i
#     xor_array = genrate_xor_array(r, i++)

def generate_xor_array(r):

    arr = [0]  * (r+1)
    # for i in range (r):
    #     arr[i] = 0

    #arr[0] = 0
    i = 1
    #while (i < r):
    for _ in range (r):
        arr[i] = arr[i-1] ^ i
        i = i+1
    return arr
   
# Complete the xorSequence function below.
def xorSequence(l, r):

    print (l, r)
    A = generate_xor_array(r)
    print (A)
    xor_result = 0
    while (l < r):
        print (A[l], A[l+1])
        result = A[l] ^ A[l+1]
        xor_result = xor_result ^ result
        l +=1
    # for i in range (diff):
    #     xor_result = xor_result ^ A[l]
    #     l +=1
    return xor_result


    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    if q >= 1 and q <= 10**5: 

        for q_itr in range(q):
            lr = input().split()

            l = int(lr[0])

            r = int(lr[1])

            result = xorSequence(l, r)
            print (result)

            # fptr.write(str(result) + '\n')

    # fptr.close()
