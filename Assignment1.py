from math import log

def logquad():
  i = 2

  while ((100 * log(i, 2)) > (2*i*i)):
    i += 1
  print(i-1)

def power1(x, n):
  pow = 1
  for i in range(n):
    pow *= x
  return pow

def power2(x, n):
  if n == 0:
    return 1

  y = power2(x, n//2)
  if n % 2 == 0:
    return y * y
  else:
    return x * y * y
      

def power3(x, n):
  y = 1
  z = x
  while (n != 0):
    if (n % 2 == 1):
      y *= z
    z *= z
    n = n // 2
  return y

print(power3(3,4))