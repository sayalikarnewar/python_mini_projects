from math import *

# function that calculates Probability. 
def Probability(sum, times) : 
	favorable, total, probability = 0.0, 36.0, 0

	# To calculate favorable outcomes 
	# in thrown of 2 dices 1 times. 
	for i in range(1,7) : 
		for j in range(1,7) : 
			if ((i + j) == sum) : 
				favorable += 1

	gcd1 = gcd(int(favorable), int(total)) 

	# Reduce to simplest Form. 
	favorable = favorable / gcd1 
	total = total / gcd1 

	# Probability of occuring sum on 2 dice N times. 
	probability = pow(total, times) 

	return int(probability) 


# Driver Code 
if __name__ == "__main__" : 

	sum, times = 7, 1

	print("1","/",Probability(sum, times)) 

