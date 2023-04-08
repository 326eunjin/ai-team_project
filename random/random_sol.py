import random as rd


def random_sol():
    # random solution from 0 -> 999 , first citi is 0
    sol = [0] + rd.sample((range(1, 1000)), 999)
    f = open('random_solution.csv', 'w')
    # write each element of sol to the csv file
    for i in sol:
        f.write(str(i) + '\n')

    return sol


random_sol()
