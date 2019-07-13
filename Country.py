# Countries Information Quiz
# Coded by : Syed Azam Hassan
import csv
from random import randint
from random import sample
head = ["Country Name", "Capital", "Currency", "Official Language", "Head of Govt."]
def box(s):
    l = len(s)
    print("┌"+"─"*l+"┐")
    print("│"+s+"│")
    print("└"+"─"*l+"┘")
box(" Countries Information Quiz ")
print()
with open("countries.csv", encoding="utf-8") as c:
    a = list(csv.reader(c))
r = randint(1, len(a))
t = randint(1,4)
q = " Who" if t == 4 else " What"
op = [a[r][t], a[randint(1, len(a))][t], a[randint(1, len(a))][t], a[randint(1, len(a))][t]]
opr = sample(op, 4)
for n in range(4):
    print(f" [{n+1}] {opr[n]}")
print()
print(q, "is", head[t], "of", a[r][0], end='')
i = input(' [1/2/3/4] ? ')
if not (i == "1" or i == "2" or i == "3" or i == "4"):
    print("\n Invalid Input")
    quit()
i = int(i)
print()
print(" Wow! You got it!" if opr[i-1] == a[r][t] else " Ops! I'm Sorry")
box(' '+head[t]+" of "+'"'+a[r][0]+'"'+" is "+'"'+a[r][t]+'" ')
input()