# Number Guessing Game - Syed Azam Hassan
from time import sleep # to shows numbers for few milliseconds
from os import system # to use clear screen
from random import randint # to generate random numbers
import winsound

numbers = [str(randint(1,6)) for n in range(6)]
input("I will show u 6 numbers. Press Enter to Begin.")
for n in range(6):
    system("cls")
    print (' '*n+str(numbers[n]), end='', flush=True)
    winsound.Beep(n*500+1000, 100)
    sleep(0.2)
system("cls")
g = input("Guess the numbers : ")
if g == ''.join(numbers):
    print("You Win!!!!")
else:
    print("You Lose!!!!")
    print("It was : "+''.join(numbers))
	
input()
