import math
import random

n = int(input())
x = float(input())
sum = 0
r = random

for i in range(n):
    sum2 = math.sin(x)
    for __ in range(i):
        sum2 = math.sin(sum2)
    sum += sum2
print(sum)