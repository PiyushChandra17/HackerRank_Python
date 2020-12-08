#!/bin/python3

import math
import os
import random
import re
import sys

N,M = map(int,input().split())
rows =[list(map(int,input().split())) for i in range(N)]
k = int(input())
rows = sorted(rows,key=lambda x:x[k])

for i in rows:
    print(*i)
