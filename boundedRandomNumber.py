
# FILE NAME - boundedRandomNumber.py

# NAME - Md Wara
# DATE - 02/17/2023
# DESCRIPTION - # generates bounded random number  

import random
def main():
    boundedRandom()

def boundedRandom():
 
 seed = int(input("Enter a seed for the random number generation: "))
 random.seed(seed)
 boundedrandomNum = random.randint(1,10) 
 print()
 print(int (boundedrandomNum) )

main()

