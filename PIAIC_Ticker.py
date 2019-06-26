# A PIAIC Ticker Program Created by Me
# Press Ctrl+C to Exit.
from time import sleep
from os import system
print ("\a\a") # bell 2 times
s1 = " ██████╗  ██╗  █████╗  ██╗  ██████╗                                            "
s2 = " ██╔══██╗ ██║ ██╔══██╗ ██║ ██╔════╝                                            "
s3 = " ██████╔╝ ██║ ███████║ ██║ ██║                                                 "
s4 = " ██╔═══╝  ██║ ██╔══██║ ██║ ██║                                                 "
s5 = " ██║      ██║ ██║  ██║ ██║ ╚██████╗                                            "
s6 = " ╚═╝      ╚═╝ ╚═╝  ╚═╝ ╚═╝  ╚═════╝                                            "
l = len(s1)
system("color 1")
while 1:
    for k in range(l):
        system("cls")
        print("\n\n\n\n")
        print(s1[k:l] + s1[0:k])
        print(s2[k:l] + s2[0:k])
        print(s3[k:l] + s3[0:k])
        print(s4[k:l] + s4[0:k])
        print(s5[k:l] + s5[0:k])
        print(s6[k:l] + s6[0:k])
        sleep(0.05)