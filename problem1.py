from random import randrange

result =randrange(0, 100)



print("Enter a number 0 through 100")
firstnumber =int(raw_input("firstnumber"))
while(firstnumber != result):
	if(firstnumber < result):
		print("higher")
	if(firstnumber > result):
		print("lower")
	firstnumber =int(raw_input("firstnumber"))
	if(firstnumber == result):
		print("	correct")