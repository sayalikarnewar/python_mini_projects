#https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
import random
n=1
def guess():
	global n
	n = random.randrange(1,100,1)
	user_input=int(input("your input"))

for i in range(100):
	global n
	if (n-user_input)==i:
		print("digits far",i)
		guess()

#	print("upto 10 digits far")
#	guess()
#	print("upto 20 digits far")
#	guess()
