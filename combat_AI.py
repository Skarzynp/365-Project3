import random, DnD, types
import itertools

class combat_stats:

	# instance variables
	AgroLvl = []
	distClass = []

	def __init__(self):
		print("----------------------------------")

		# better if static?
		self.AgroLvl = {
			0: "Timid",
			1: "Passive",
			2: "Neutral",
			3: "Agressive",
			4: "Fanatical"
		}
		self.distClass = {
			0: "Adjacent",
			1: "Close",
			2: "Medium",
			3: "Long",
			4: "Out of Range"
		}
		# associated with ArgoLvl dictionary
		self.agroCount = 0;
		# associated with distClass dictionary
		self.distance = 2;
		#Does the AI have the suprise round?
		self.surprise = False;

	def getOdds(self):

		friendList = []
		enemyList = []
		count = 0
		best_count = 0

		use_list = str(input("Use default lists? (y/n)"));
		# If default list selected, preload list
		if (use_list == 'y' or use_list == 'Y'):
			#use_list = str(input("Which enemy list? (y/n)"));

			#enemyList = [bandit, bandit, bandit]
			#friendList = [archmage, archmage, archmage]
			for i in range(4):
				enemyList.insert(i, "bandit")
				friendList.insert(i, "archmage")

			#print the lists, so what is in the default is apparent
			print(f"Enemy Force: {enemyList}")
			print(f"Friendly Force: {friendList}")
		#Get user input if not using default or preset list
		else:
			try:
				enemies = int(input("How many enemies: "))
			except ValueError:
				print("Not a Number")

			try:
				friendlies = int(input("How many friendlies: "))
			except ValueError:
				print("Not a Number")

			for i in range(enemies):
				Type = str(input("Type of enemies: "))
				enemyList.insert(i,Type)

			for j in range(friendlies):
				Type = str(input("Type of Friendlies: "))
				friendList.insert(j,Type)

		#Determine and display success rates in single simulated encounters
		for q in range(len(enemyList)):
			#Calculations to determine rate
			Friendly= DnD.Creature(friendList[q]) #FIXME lists must be the same length or else this may fail!
			Enemy = DnD.Creature(enemyList[q])
			rate=DnD.Encounter(Friendly,Enemy).predict()
			if (rate[1] > rate[3]):
				count += 1

		for r in itertools.product(friendList, enemyList):
			Friendly = DnD.Creature(r[0])
			Enemy = DnD.Creature(r[1])
			rate = DnD.Encounter(Friendly, Enemy).predict()
			if (rate[1] > rate[3]):
				best_count += 1

		#Display success rates
		print(f"\nEnemy Alignment: {rate[0]}")
		print(f"Expected Enemy Success Rate: {rate[1]}")
		print(f"Ally Alignment: {rate[2]}")
		print(f"Expected Ally Success Rate: {rate[3]}")
		print(rate)
		print(f"\nAnticipated wins based on current orientation: {count}\n")
		print(f"\nPossible amount of favoriable encounters: {best_count}\n")

	def getUserInput(self):
		print(self.AgroLvl)
		agroCount = int(input("Enter aggression level of AI: \n (from 0 to 4, 0 is low) "))
		print(f"\n{agroCount} {self.AgroLvl[agroCount]}\n")
		self.agroCount = agroCount

		# error checking
		#print(self.agroCount)

		print(self.distClass)
		distance = int(input("Enter intitial distance of enemy: \n (from 0 to 4, 0 is low) "))
		print(f"\n{distance} {self.distClass[distance]}\n")
		self.distance = distance

		# error checking
		#print(self.distance)
	
