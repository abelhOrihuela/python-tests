#!/bin/python

import math
import os
import random
import re
import sys

def is_leap(year):
    leap = False
    
    if year%4 > 0:
        leap =True

if __name__ == '__main__':
    year = int(input("Input: "))
    is_leap(year)
