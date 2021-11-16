from decimal import *
getcontext().prec = 50

s = Decimal(1) #sign
pi = Decimal(3)

n = 50000000

for i in range(2, n * 2, 2):
    pi = pi + s * (Decimal(4) / (Decimal(i) * (Decimal(i) + Decimal(1)) * (Decimal(i) + Decimal(2))))
    s = -1 * s

print("Approximate value of PI:", pi, " for ",n)