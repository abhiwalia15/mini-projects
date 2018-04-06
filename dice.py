'''The Goal: Like the title suggests, this project involves writing a program
that simulates rolling dice. When the program runs, it will randomly choose
a number between 1 and 6. (Or whatever other integer you prefer 
 — the number of sides on the die is up to you.) The program will
print what that number is. It should then ask you if you’d like 
to roll again. For this project, you’ll need to set the min and 
max number that your dice can produce. For the average die, that
means a minimum of 1 and a maximum of 6. You’ll also want a function
that randomly grabs a number within that range and prints it.'''

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
