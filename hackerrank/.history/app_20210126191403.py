#!/bin/python

import math
import os
import random
import re
import sys

def is_leap(year):
    leap = False

    if year < 10**5:
        leap = False
    
    if year%4 > 0:
        leap = True

    if year%1000 == 0:
        leap = False

    if year%400 == 0:
        leap = True

    return leap

if __name__ == '__main__':
    year = int(input("Input: "))
    print(is_leap(year) = True)
