# Animated Text Program Created by Me
from time import sleep
from os import system
from math import sin
# print ("\a\a") # bell 2 times
# s = input("Enter Your Name : ")
for n in range(0,380):
    x = sin(n/10)*32+32
    # system("cls")
    print(" "*int(x)+"▒█▒ KASHIF ▒█▒")
    # print(" "*int(65-x)+"▒█▒ KASHIF ▒█▒ ")
    sleep(0.04)