import random as rd

def random_sol():
    sol = [0] + rd.sample((range(1,1000)), 999) # random solution from 0 -> 999 , first citi is 0
    return sol 

print(random_sol())
