n=3
a=[[9,2,3],[4,5,6],[7,8,5]]

left=right=0

for i in range(n):

    left+=a[i][i]
    right+=a[i][n-1-i]
print(left)
print(right)
print(abs(left-right))
import os
import math
import random
import re
import sys

for i in range(1, n+1):

    s='#'*i
    #print(s,rjust(n))

b=[3,4,5,6,7,45,66,75,5,-2,-6]
print(sum(b)-max(b), sum(b)-min(b))

candle =[4,4,2,3,6,4,3,7,7,7,7]

length= len(candle)
maximum=0
count =0

for i in range(length):

    if (candle[i]>maximum):
        maximum = candle[i]
        count =1
    elif(candle[i]==maximum):
        count+=1

print(count)

print(candle.count(max(candle)))


s = '07:05:19AM'

maridian = s[-2:]
print(maridian)
print(s[:2])

if(maridian == 'AM' and s[:2]!='12'):
    s= str (12+int(s[:2])) + s[2:]

