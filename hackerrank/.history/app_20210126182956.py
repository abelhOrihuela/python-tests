#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    range_2_5 = range(2, 5)
    
    if n%2 > 0:
        print("Weird")
    elif n in range_2_5:
        print("Not weird")