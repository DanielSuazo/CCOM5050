from math import log

i = 2

while ((100 * log(i, 2)) > (2*i*i)):
  i += 1
print(i-1)