import re

addressToVerify = input("Enter Email : ").lower()
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

if match == None:
	print('Bad Syntax')
else:
	print('Valid Email Address')
	
input()