#This script generates a running sequence of the first n prime numbers.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def check(num): #checks if prime(True), else (False)
    for i in range(2,num):
        if num == 2:
            return True
        elif num % i > 0:
            continue
        else:
            return False
    return True

def next_prime():
    num = 2
    while True:
        if check(num) == True:    
            yield num
            num +=1
        else:
            num += 1

primes = next_prime()

for i in range(9):
    print(next(primes))


