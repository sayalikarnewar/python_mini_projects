import random
print("""			GAMBLE NOW		
		you are credited with 100$
	for each play amount will be debited by 10$
	you will lose if balance hits less than 10$""")


def rollcase():

	roll = random.randrange(1,6,1) #random dice roll
	print("you got ",roll)

	if roll == 1: #for every roll,particular "add" is added into the balance amount
		add = 0
	if roll == 2:
		add = 20
	if roll == 3:
		add = 0
	if roll == 4:
		add = 10
	if roll == 5:
		add = 0
	if roll == 6:
		add = 60
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



	
