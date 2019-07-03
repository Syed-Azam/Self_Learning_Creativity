# Number Guessing Game - Syed Azam Hassan
from time import sleep # to shows numbers for few milliseconds
from os import system # to use clear screen
from random import randint # to generate random numbers
numbers = [str(randint(1,4)) for n in range(4)]
for n in range(4):
    system("cls")
    print (' '*n+str(numbers[n]), end='')
    print ("\a")
    sleep(0.4)
system("cls")
g = input("Guess the numbers : ")
if g == ''.join(numbers):
    print("You Win!!!!")
else:
    print("You Lose!!!!")
    print("It was : "+''.join(numbers))


    

