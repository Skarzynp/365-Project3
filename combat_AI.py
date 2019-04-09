import random, DnD, types


class combat_stats:

	def __init__(self):
		print("in init")

		# better if static?
		AgroLvl = {
			0: "Timid",
			1: "Passive",
			2: "Neutral",
			3: "Agressive",
			4: "Fanatical"
		}
		distClass = {
			0: "Adjacent",
			1: "Close",
			2: "Medium",
			3: "Long",
			4: "Out of Range"
		}
		# associated with ArgoLvl dictionary
		agroCount = 0;
		# associated with distClass dictionary
		distance = 2;
		#Does the AI have the suprise round?
		surprise = False;

	def getOdds(self):

		friendList = []
		enemyList = []
		count = 0

		use_list = str(input("Use default lists? (y/n)"));
		# If default list selected, preload list
		if (use_list == 'y' or use_list == 'Y'):
			#use_list = str(input("Which enemy list? (y/n)"));

			#enemyList = [bandit, bandit, bandit]
			#friendList = [archmage, archmage, archmage]
			for i in range(3):
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

			#Display success rates
			print(f"\nEnemy Alignment: {rate[0]}")
			print(f"Expected Enemy Success Rate: {rate[1]}")
			print(f"Ally Alignment: {rate[2]}")
			print(f"Expected Ally Success Rate: {rate[3]}")
			print(rate)
			print(f"\nSimulated Victory Count: {count}")

	def getUserInput(self):
		print(self.AgroLvl)
		agroCount = str(input("Enter aggression level of AI: \n (from 0 to 4, 0 is low) \n"))
		print(agroCount + self.AgroLvl[agroCount])
		self.agroCount = agroCount

		# error checking
		print(self.agroCount)

		print(self.distClass)
		distance = str(input("Enter intitial distance of enemy: \n (from 0 to 4, 0 is low) \n"))
		print(distance + self.distClass[distance])
		self.distance = distance

		# error checking
		print(self.distance)
