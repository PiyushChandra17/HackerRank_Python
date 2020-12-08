#!/bin/python3

import math
import os
import random
import re
import sys


from datetime import datetime as dt

for _ in range(int(input())):
    t1 = dt.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    t2 = dt.strptime(input(),'%a %d %b %Y %H:%M:%S %z')

    print(int(abs(t1-t2).total_seconds()))
