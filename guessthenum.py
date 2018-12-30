#https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

import random

def func():
	n = random.randrange(100)
	def guess():
		m =int(input("guess the number"))
		if n==m:
			print ("correct guess. yipeee")
		elif n>m:
			print ("guess higher ")
			guess()
		elif n<m:
			print ("guess lower")
			guess()
	guess()
func()

