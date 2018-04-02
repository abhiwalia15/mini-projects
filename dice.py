import random

def roll(sides=6):
	num_rolled = random.randint(1,sides)
	return num_rolled
	
def main():
	sides = 6
	rolling = True
	while rolling:
		roll_again = input("Ready to ROLL? ENTER=roll Q=qiut\n")
		if roll_again != 'q':
			num_rolled = roll(sides)
			print("you rolled a "+str(num_rolled))
		else:
			rolling = False
			
	print("THANKS FOR PLAYING :D")
	
main()
