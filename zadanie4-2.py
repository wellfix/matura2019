plik = open("liczby.txt").read().split()
import math

for x in plik:
    sum = 0
    for z in x:
        y = int(z)
        sum = sum + math.factorial(y)
        if sum == int(x):
            print(sum)