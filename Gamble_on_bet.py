import random

print("""			GAMBLE NOW		
		you are credited with 100$
	for each play amount will be debited by 10$
	you will lose if balance hits less than 10$""")

bet = input("bet on a number")

def rollcase():
	roll = random.randrange(1,6,1) #random 
	print("you got ",roll)

	if roll == bet: #for every roll,particular "add" is added into the balance amount
		add = 100
	else:
		add = 0
	return add 
		
amount = 100 #given amount 
i = 10 #no of chances 

while i >0:
	if amount >= 10: #before balance hits 0
		won_amount = rollcase() 
		amount = amount + won_amount - 10 #for each chance,10$ is debited
	else:
		print("oops you are on low balance")
	i = i - 1 #decrementing the chances
	
print("			GAME OVER")
print("		your amount ",amount)



	
