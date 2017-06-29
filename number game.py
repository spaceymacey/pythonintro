#guessing the number game

import random

guessestaken = 0

myname = raw_input("what is your name? ")

number = random.randint(1, 100)

print "hi %s, i am thinking of a number between 1 and 100." % (myname)

while guessestaken < 10:
	guess = raw_input("guess what number i am thinking of? >>")
	guess = int(guess)
	guessestaken += 1

	if guess < number:
		print "your guess is too low."
	if guess > number:
		print "your guess is too high."
	if guess == number:
		break 

if guess == number:
	print "great job! %s, you guessed the number correctly. it took you %d tries." % (myname, guessestaken)

else:
	print "sorry, you took too many attempts. i was thinking of the number %d" % (number)