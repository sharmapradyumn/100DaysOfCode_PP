#!/bin/python3

# Problem Url: https://www.hackerrank.com/challenges/py-if-else/problem
import sys
#only one library is essential

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
    print("Weird")
    else:
        if n >= 2 and n <= 5:
            print ("Not Weird")
        elif n >= 6 and n <= 20:
            print ("Weird")
        elif n > 20:
            print ("Not Weird")
