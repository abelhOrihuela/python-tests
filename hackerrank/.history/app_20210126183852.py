#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Hola"))

    print(20 in range(6, 20))
    
    if n%2 > 0:
        print("Weird")
    elif n in range(2, 5):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    elif n > 20:
        print("Not Weird")