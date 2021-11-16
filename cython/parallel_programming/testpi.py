from ccalcpi import calcpi
nPoints = 50000000
pi = calcpi(nPoints)
print('OpenMP pi = ', pi, ' for ', nPoints)