import os

def helpcommand():
	print("""
------------HELP------------
  inspect - Inspect things	
   go - To go somewhere
----------------------------
		""")
	startscene()

def startscene():
	print("""
You woke up in a empty room, you see four doors, each of them lead to respectively
to north, south, east and west
You have nothing on you and can't escape
Good luck
(Type HELP for command list)
""")
	action = input("What do you do? > ")
	if action == "help" or action == "HELP" or action == "Help":
		os.system("cls")
		helpcommand()
	elif action == "go south":
		os.system("cls")
		print("""
You're in a room with a chair, you have a bad feeling about the room and feel uncomfortable,
there is something on the chair
			""")
		southaction = input("What do you do? > ")
		if southaction == "inspect chair":
			os.system("cls")
			print("""
You a sheet of paper with "5798" wrote on it,
it's burned but still readable
				""")
		actionpaper = input("What do you do? > ")
		if actionpaper == "go back":
				os.system("cls")
				startscene()
		elif southaction == "go back":
			os.system("cls")
			startscene()

	if action == "go north":
		os.system("cls")
		print("""
You are in a empty room, one of the wall seems a bit loose
			""")
		northaction = input("What do you do? > ")
		if northaction == "inspect wall":
			os.system("cls")
			print("""
Oh ! You fell into a spike trap !
				""")
			exit("Game Over")
		if northaction == "go back":
			os.system("cls")
			startscene()
	if action == "go west":
		os.system("cls")
		west()
	if action == "go east":
		print("""

There is nothing here, you try to go back to the main room but someone broke you're neck,
Bad Luck...
			""")
		exit("Game Over")
	if action == "quit":
			exit("Game ended")
	else:
		startscene()

def west():
	print("""
You are in a room with a chest in the center of the room there is also a keypad on
the left wall, a red key on the floor
		""")
	actionwest = input("What do you do? > ")
	if actionwest == "inspect chest":
		os.system("cls")
		print("""
The chest require a code
			""")
		chestcode = "5798"
		chestawnser = int(input("What's the code? >"))
		if chestawnser == chestcode:
			os.system("cls")
			print("""
The chest was filled with spiders, you choke on one and died
				""")
			exit("Game Over")
		else:
			os.system("cls")
			print("""
Incorrect code
			""")
			west()
	elif actionwest == "inspect keypad":
			os.system("cls")
			print("""
The keypad require a code
				""")
			keypadawnser = int(input("What's the code? >"))
			if keypadawnser == 5798:
				print("""
The wall oppened and you are now free,
*-*Congratulation*-*
				""")
				exit("The End")
			else:
				os.system("cls")
				print("""
incorrect code
				""")
				west()
	elif actionwest == "inpspect key":
		exit("The key was an illusion and you die in the matrix")
		startscene()
	elif actionwest == "go back":
		os.system("cls")
		startscene()
	elif actionwest == "quit":
		exit("Game ended")

startscene()