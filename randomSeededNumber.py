
# FILE NAME - randomSeededNumber.py

# NAME - Md Wara
# DATE - 02/16/2023
# DESCRIPTION - generates seeded random numbers

import random


def main():
    generateSeededRandomNumber()

def generateSeededRandomNumber():
 seed = int(input("Enter a seed for the random number generation: "))
 random.seed(seed)
 randomNum = random.random()
 print(randomNum)
main()



