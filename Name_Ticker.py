# A Fun Ticker Program Created by Me
from time import sleep
from os import system
# print ("\a\a") # bell 2 times
s = input("Enter Your Name : ")
s = s + " " * (79 - len(s))
l = len(s)
while 1:
    for k in range(l):
        system("cls")
        print(s[k:l]+s[0:k])
        sleep(0.05)