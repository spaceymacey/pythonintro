
from sys import exit

key = False

print "you wake up on the floor of a small, blank white room with absolutely nothing in it except for a countdown timer for one hour. you are wearing blank white clothing with empty pockets. you have no memory of how you got here, but your instincts say you want to escape this place before that timer hits 0..."

# declare a function called start

def start():
	
	print "you see two white doors, one on your left and one on your right. "
	choice = raw_input("which door do you take? (type: left or right) >> ")

	#write a conditional through the doors

	if choice == "left":
		yellow_room()
	elif choice == "right":
		red_room()
	else:
		print "please pick a room, if you stay here too long, you will run out of time."
		start()

def yellow_room():
	print "you find yourself in a room painted yellow. there is a yellow desk and chair in the corner of the room. there is a window across the room."

	# make a while loop that repeats forever unless we die/make the correct choice

	while True:
		choice = raw_input("what do you do? (type: go back to white room, escape through window, or sit in chair >> ")
		if choice == "escape through window":
			dead("you fall out the window to your death. game over.")
		elif choice == "go back to white room":
			start()
		elif choice == "sit in chair":
			print "you notice there is a drawer below the desk. you open the drawer and see two items, a cell phone and a key."
			choice = raw_input("do you pick up the cell phone or the key? (type: phone or key) >> ")
			if choice == "phone":
				dead("as you turn on the cell phone, you get electrocuted and die. game over.")
			elif choice == "key":
				print "great, you now have a key! this might be useful later..."
				key = True
		else:
			print "please make a choice, if you stay here too long, you will run out of time."
			yellow_room()

def red_room():
	print "you find yourself in a red painted room with kitchenware. you look around the room noticing that something yummy smelling boiling in a pot on the stove. you also see a cabinet nearby."
	
	while True:
		choice = raw_input("what do you do? (type: go back to white room, look in pot, or look in cabinet) >> ")
		if choice == "look in pot":
			print "inside the pot is some ready vegetable soup!"
			choice = raw_input("would you like to drink some soup? (type: drink soup or close pot) >> ")
			if choice == "drink soup":
				dead("the soup turned out to be poisonous! game over.")
			elif choice == "close pot":
				print "no soup it is!"
		elif choice == "look in cabinet" and key:
			print "the cabinet is locked, but you have the key! you open the door and it turns out to be the exit. congratulations! you have escaped!"
			exit(0)
		elif choice == "look in cabinet" and not key:
			print "the cabinet is locked... hmmm, wonder if there is a key..."
		elif choice == "go back to white room":
			start()
		else:
			print "please make a choice, if you stay here too long, you will run out of time."
			red_room()

	exit(0)

def dead(msg):
	print msg
	choice = raw_input("play again? type yes >> ")
	if choice == "yes":
		start()
	if choice == "no":
		exit(0)

start()

