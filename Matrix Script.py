#!/bin/python3

import math
import os
import random
import re
import sys

N,M = list(map(int,input().split()))

rows = [input() for i in range(N)]
text = ''.join([row[i] for i in range(M)for row in rows])

text = re.sub(r'(?<=\w)([^\w]+)(?=\w)',' ',text)
print(text)
