# import time module to calculate times 
import time 
  
# initialise lists to save the times 
forLoopTime = [] 
whileLoopTime = [] 
listComprehensionTime = [] 
starOperatorTime = [] 
  
# repeat the process for 500 times 
# and calculate average of times taken. 
for k in range(500):  
  
    # start time 
    start = time.time() 
    # declare empty list 
    a = [] 
    # run a for loop for 10000 times 
    for i in range(10000): 
        a.append(0) 
    # stop time 
    stop = time.time() 
    forLoopTime.append(stop-start) 
  
    # start time 
    start = time.time() 
    # declare an empty list 
    a = [] 
    i = 0
    # run a for loop 10000 times 
    while(i<10000): 
        a.append(0) 
        i+= 1
    stop = time.time() 
    whileLoopTime.append(stop-start) 
  
    start = time.time() 
    # list comprehension to initialize list 
    a = [0 for i in range(10000)]  
    stop = time.time() 
    listComprehensionTime.append(stop-start) 
  
  
    start = time.time() 
    # using the * operator 
    a = [0]*10000 
    stop = time.time() 
    starOperatorTime.append(stop-start) 
  
  
  
print("Average time taken by for loop: " + str(sum(forLoopTime)/100)) 
print("Average time taken by while loop: " + str(sum(whileLoopTime)/100)) 
print("Average time taken by list comprehensions: " + str(sum(listComprehensionTime)/100)) 
print("Average time taken by * operator: " + str(sum(starOperatorTime)/100))
input()
