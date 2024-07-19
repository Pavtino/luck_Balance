#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    unim=[x[0] for x in contests if x[1]==0]# unimportant contest list
  
    im=[x[0] for x in contests if x[1]==1]#important contest list
    im.sort(reverse=True)
    im1=im[0:k]#fisrt k important contest
    im2=im[k:]# other important contest that can be lose

    result=sum(im1)+sum(unim)-sum(im2)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()

