#!/usr/bin/python3
# Maximiliano Proaño Bernal
# 03/12/19
# Python 3.7.3
# Números "raros"

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n//2 != n/2:
    print("Weird")
elif n//2 == n/2 and 2 <= n <= 5:
    print("Not Weird")
elif n//2 == n/2 and 6 <= n <= 20:
    print("Weird")
elif n//2 == n/2 and 20 < n:
    print("Not Weird")
