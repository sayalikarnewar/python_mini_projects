import random
print("""			GAMBLE NOW		
		you are credited with 100$
	for each play amount will be debited by 10$
	you will lose if balance hits less than 10$""")

def rolled():
	roll = random.randrange(1,6,1)
	print("you got ",roll)
	return roll


def rollcase(roll):

	if roll == 1:
		add = 10
	if roll == 2:
		add = -20
	if roll == 3:
		add = 0
	if roll == 4:
		add = -10
	if roll == 5:
		add = 50
	if roll == 6:
		add = 100
	return add 
		

amount = 100
for i in range(1,11):
	if amount >= 10:
		dice = rolled()
		won_amount = rollcase(dice)
		amount = amount + won_amount
	else:
		print("oops you are on low balance")
	

print("			GAME OVER")
print("your amount ",amount)



	
