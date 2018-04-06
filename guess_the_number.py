'''The Goal: Similar to the first project, this project also uses the 
random module in Python. The program will first randomly 
generate a number unknown to the user. The user needs to guess 
what that number is. (In other words, the user needs to be able to 
input information.) If the user’s guess is wrong, the program should 
return some sort of indication as to how wrong (e.g. The number is 
too high or too low). If the user guesses correctly, a positive
indication should appear. You’ll need functions to check if the
user input is an actual number, to see the difference between
the inputted number and the randomly generated numbers, and to
then compare the numbers.'''

import random

guess_taken = 0
num = random.randint(1,21)

name = input("ENTER YOUR NAME\n")
print("Hello "+name.title()+" , i was thinking of a number between 1 to 20\n")

while guess_taken<3:
	#input any number you want and return it
	user = input("\nTAKE A GUESS\n")
	n = int(user)
	
	guess_taken = guess_taken + 1
	
	if n == num:
		break
		
	if n < num:
		print("YOUR NUMBER IS TOO LOW\n")
	
	if n > num:
		print("YOUR NUMBER IS TOO HIGH")

if n == num:
	print("Good job " + name.title() + " you gussed the right number.\n")
	
if n != num:
	print('Nope. The number I was thinking of was ' + str(num))
