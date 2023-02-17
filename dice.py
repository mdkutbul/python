

# FILE NAME - dice.py

# NAME - Md Wara
# DATE - 02/17/2023
# DESCRIPTION - rolls dice twice

import random

def main():
    rollDie()

def rollDie():
    seed = int(input("Enter a seed for the random number generation: "))

    random.seed(seed)

    rollDie1 = random.randrange(1,7)
    rollDie2 = random.randrange(1,7)
    print()
    print("Die roll one is", rollDie1)
    print("Die roll two is", rollDie2)

main()


