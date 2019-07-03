# reverse key:value pair in a dictionary
# Code by : Syed Azam Hassan - PIAIC
d = {1:"One", 2:"Two", 3:"Three", 4:"Four"}

print(d)
d = {v: k for k, v in d.items()}
print(d)
