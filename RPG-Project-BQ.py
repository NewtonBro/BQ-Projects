print("\n'Beast Of The Indus' - A Text Based RPG by Fardan, Isharab and Shabeeb.\n")

#player's bio data

name = input("Enter a name for your character: ")
HP = 100
Inventory = { 'weapon':'dagger', 'armour':'regular vest', 'consumable':['water bottle'], 'tools':['rope']}

#game intialization prompt

def press_any_key(): #A function asking user to input anything and runs following code after enter key is pressed
    input('\n<Press any key and enter to continue>\n')
press_any_key() #calling the declared function

#game starts after user input

print(f"\n'Assalamualaikum {name}! welcome to Kot Mitthan, a little village amidst the Indus Valley, what brings you here?' a guard standing in front of the town gate asks. \n 1 - I'm here to meet a friend\n 2 - Just passing by\n")

#Decision Making Mechanism, Inspired by telltale games

while True:
	Decision1 = input("Choose an option, dialogue 1 or 2? \n")

	if Decision1 == '1':
		print(f"\n{name}: 'I am here to meet a friend of mine.'\nThe Guard: 'Alright then, you may enter. Enjoy your time while you're here!")
		break
	elif Decision1 == '2':
	 	print(f"\n{name}: 'Just passing by.'\nThe Guard: 'Alright, Enter with caution and please, avoid causing any mischief. other than that, have a good time!'")
	 	break
	else:
		print("Invalid Input")
		continue

print("\nYou enter the village. It is night time and the streets are empty, what do you want to do?\n 1 - Roam around for a bit\n 2 - Go to your friend's house")

while True:
	Decision2 = input("\nChoose your option, action 1 or 2? \n")

	if Decision2 == '1':
		print("\nYou roam on the village streets. While doing so, you spot a man whose clothes are dirty and ripped. What do you do?\n 1 - Approach him\n 2 - Leave him alone and visit your friend instead\n")
		while True:
			Decision2b = input("Choose your next action, 1 or 2?\n")
			if Decision2b == '1':
				print("You approach the poor man who is facing the opposite side. When you get close enough, it turns out he's a crackhead and turns around to stab you, killing you with his knife.\n \nGAME OVER")
				exit()
			elif Decision2b == '2':
				print("You don't take the risk and just visit your friend instead")
				break
			else:
				print("Invalid Input")
				continue
		print("You have arrived at you friend's house")
		break
	elif Decision2 == '2':
			print("You arrive at your friend's house.")
			break
	else:
		print('Invalid Input')
		continue

#Arrival at Mehmood's House, Dialogue between Mehmood and user by using simple print fuction.

print(f"'Assalamualikum, my dear brother {name}! It is truly a pleasant surprise to see you here! come inside, come inside.' says your friend mehmood, as his face shines with pure happiness upon your arrival'")
print("\nAfter answering his salam and thanking him for the warm welcome, you walk in with mehmood into his house, small - made out of mud bricks but beautiful in a way, and sit down with mehmood on wooden chairs. Mehmood asks his son to go bring you a glass of fresh lassi.")
print("\n'What brings me here is a rumor about your village, spreading like wildfire' you speak after clearing your throat")
print("\n'You must be talking about the rumor about the bakunawa, and as I know about your myth-bunking nature, let me just tell you before hand that this beast is no myth' clarifies mehmood 'The rumor has been spreading about a fisherman and his brother who were swallowed by the bakunawa, I was sure that it will attract you, and here you are. Looking forward to finding the truth about it. Now let me tell you something, I have seen this happen right in front of me with my own eyes. Do you still doubt its existance?'")
print("\n'No, not after you have said it. Alright then, killing the beast is my new goal' you speak as you are shocked by your friend's revelation")
print("\nMehmood: 'I understand your passion, but beware, this demon is no joke. The bakunawa is an eel-like beast that is larger than three ferries combined. It has drowned over 19 ships. If you wish to proceed, go visit the old fisherman Mushtaque Baba near the river bank after fajr, he knows a lot more than I do'")
press_any_key()
print("\nThe dawn breaks and you go outside to continue your quest. Mehmood offers you a mango.\nA mango has been added to your inventory\n What do you want to do?\n 1 - Go to see Mushtaque baba to inquire him about the bakunawa\n 2 - Visit the well near shorkot fort")

# Appending an item into the list "consumable" nested inside the dictionary "inventory"

Inventory['consumable'].append('mango')

while True:
	Decision3 = input("What do you wish to do? choose either 1 or 2\n")
	if Decision3 == '2':
		print("You walk towards the shorkot fort as the sun comes out. When you reach the ancient well, you observe the villagers are looking inside. You approach them and ask them what's going on. One of them responds: 'The bakunawa's egg lies inside. If we don't feed it, he'll flood our village like he did last year!'\nYou decide to use you mango so the villager can enjoy his")
		Inventory['consumable'].remove('mango')
		print("\nyou now head towards the river bank")
		break
	elif Decision3 == '1':
		print("\nYou decide to go meet Baba Mushtaque at the river bank as soon as possible")
		break
	else:
		print('Invalid Input')
		continue

#Bakunawa Lore Revalation through a converstion with a character

print("\n---Entering the river bank---\n")
press_any_key()
print("When you finally arrive at the bank of the Indus, you spot a thin figure standing peacefully next to a ship dock.\n\nHe is looking over the horizon line. You approach him and after greeting him, you gently ask him if he wishes to answer a few questions of yours.\n\nThe old man hesitates at first but upon insisting, he says 'alright young man, if you really are that curious then let me tell you about this bakunawa. Legend says he once drowned a mughal ship, and the treasure inside corrupted him, making him crave for more. Ever since then, he has been haunting the waters of Indus. By now he has drowned 19 ships. He has brass scales and sharp teeth, each tooth indicating a vessel that became his victim with its name engraved on it. The only weak point any man ever noticed was it's 18th tooth which it gained after drowning a british ship during the occupation. Mostly it is spotted at the trimmu barrage near which a british steamboat wreckage lies. If you really wish to face it, keep this harpoon with you. It's sound paralyzes it.'")
Inventory['tools'].append('harpoon')
print("\nA harpoon has been added to your inventory")
press_any_key()

#Boss Fight Sequence

print("\nYou now advance towards the ship wreckage to encounter this beast.")

print("\n---Entering Trimmu Barrage---\n")

print("You reach the barrage and spot a ship wreckage, not too far away lies a broken bridge. It has something shiny hanging below it through a rope. you decide to investige. When you climb up the broken bridge, you realize the hanging object is a brass bell, and as the old man had sad, the beast was made up of brass scales. You decide to ring the bell...")

print("The River Begins To Vibrate Like A Shivering Man Lost In Snow.....\n\n--§+-> BAKUNAWA RISES FROM THE RIVER <-+§--")

bakuHP = 130 #storing values for the monster's health and him being paralyzed in variables for using later
bakuPara = 0

#Turn-based combat system inspired by pokemon and final fantasy

while HP > 0 and bakuHP > 0:
	print(f"\nYour HP: {HP} || Bakunawa's HP: {bakuHP}\nChoose your attack:\n")

	print(" 1 - Attack with dagger (-30 HP)\n 2 - Tie his tooth (special weakness)\n 3 - Play the Harpoon (paralyzed)")
	action = input("Select an option from 1 to 3: ")

	if action == '1':
		bakuHP -= 30
		print(f"{name} used his dagger to attack (-30 HP ~ Bakunawa)")
	elif action == '2':
		bakuHP -=100
		print(f"{name} after catching bakunawa's weakness, {name} has caused great damage to bakunawa! (-100 HP ~ Bakunawa")
	elif action == '3':
		bakuPara += 1
		print(f"Using Mushtaque Baba's Harpoon, you've paralyzed the bakunawa.")
	else:
		print("Invalid Argument, You're in danger now")
		
	if bakuHP  > 0 and bakuPara <1:
		HP -= 30
		print(f"The Brass Plates cut through your skin! (-30 damge ~ {name})")
	elif bakuPara > 0:
		print("The harpoon's sound has paralyzed The Bakunawa!")
		bakuPara -= 1
		
if HP < 0:
	print("\nGAME OVER")
	exit()
else:
	print("\nThe Bakunawa's life has come to an end, the people of the village shall live peacfully.\n\n•••••THE END•••••")
