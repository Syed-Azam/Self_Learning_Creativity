def azam(a):
   l=len(a)
   # First we will create a map
   b=[True]
   for n in range(1,l-1):
       if a[n-1] == a[n]-1 and a[n+1] == a[n]+1:
           b.append(False)
       else:
           b.append(True)
   b.append(True)
   # Now we will Generate a String using Map
   s=str(a[0])
   for n in range(1,l-1):
       if b[n-1] and b[n]:
           s += ','
       if b[n]:
           s += str(a[n])
       if b[n-1] and not b[n]:
           s += '-'
   s += str(a[-1])
   return(s)

def inam(lst):
 idx = 1
 elems = []
 consecutive_elems = [str(lst[0])]
 idx_in_nex_lst = 0
 for i in range(1, len(lst)):
   if lst[i - 1] + 1 == lst[i]:
     consecutive_elems.append(str(lst[i]))
   else:
     if consecutive_elems:
       if len(consecutive_elems) > 2:
         elems.append(consecutive_elems[0] + '-' + consecutive_elems[len(consecutive_elems) - 1])
       else:
         elems = elems + consecutive_elems
     consecutive_elems = [str(lst[i])]
   if i == len(lst) - 1:
     if consecutive_elems:
         if len(consecutive_elems) > 2:
           elems.append(consecutive_elems[0] + '-' + consecutive_elems[len(consecutive_elems) - 1])
         else:
           elems = elems + consecutive_elems
 return ','.join(elems)

def faizan(lst):
    strng = ""
    not_rang=0
    rang_cont = "n"
    first = "y"
    for i in range(0,len(lst)-2):
        if lst[i+2] - lst[i+1] == 1 and lst[i+1] - lst[i] ==1:
            first = "n"
            not_rang = 0
            if rang_cont == "n":
                r_start = lst[i]
                r_end = lst[i+2]
                rang_cont = "y"
            else:
                r_end = lst[i+2]
            if i < len(lst)-3:
                if lst[i+3]-lst[i+2] != 1:
                    strng += str(r_start) + "-" + str(r_end) + ","
                    rang_cont = "n"
            else:
                strng += str(r_start) + "-" + str(r_end)
        else:
            if first == "y":
                strng += str(lst[i]) + ","          
            else:
                not_rang += 1
                if not_rang > 2:
                    strng += str(lst[i]) + ","
            if i == len(lst)-3 and lst[-4] - lst[-3] == 1 and lst[-3] - lst[-2] == 1:
                string += str(lst[-1])
            elif i == len(lst)-3:
                strng += str(lst[-2]) + "," + str(lst[-1])   
    return(strng)

from time import time
k = [1,1,2,3,4,4]

print(azam(k))
print(inam(k))
print(faizan(k))

t = time()
for n in range(100000):
	inam(k)
print(time()-t)

t = time()
for n in range(100000):
	azam(k)
print(time()-t)

t = time()
for n in range(100000):
	faizan(k)
print(time()-t)

input()
