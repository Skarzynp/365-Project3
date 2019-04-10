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
		self.surprise = False
		self.detected = False
		self.pos_v_count = 1
		self.best_v_count = 1
		self.tot_count = 1
		self.rate = []

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
				enemyList.insert(i, "archmage")
				friendList.insert(i, "bandit")

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
			#TODO upgrade to mod if possible to avoid the overrun risk and get more data
			Friendly= DnD.Creature(friendList[q]) #FIXME lists must be the same length or else this may fail!
			Enemy = DnD.Creature(enemyList[q])
			rate=DnD.Encounter(Friendly,Enemy).predict()
			if (rate[1] > rate[3]):
				count += 1
		self.pos_v_count = count

		for r in itertools.product(friendList, enemyList):
			Friendly = DnD.Creature(r[0])
			Enemy = DnD.Creature(r[1])
			rate = DnD.Encounter(Friendly, Enemy).predict()
			if (rate[1] > rate[3]):
				best_count += 1
			self.tot_count += 1
		self.best_v_count = best_count

		#Display success rates
		print(f"Ally Alignment: {rate[0]}")
		print(f"Expected Ally Success Rate: {rate[1]}")
		print(f"\nEnemy Alignment: {rate[2]}")
		print(f"Expected Enemy Success Rate: {rate[3]}")
		print(rate) #error checking
		self.rate = rate #FIXME does this work as expected
		print(f"\nAnticipated wins based on current orientation: {self.pos_v_count}\n")
		print(f"\nPossible amount of favoriable encounters: {self.best_v_count}\n")

	def getUserInput(self):
		### TODO add scaffold for testing
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

		detected = str(input("Has the AI been detected by allied forces? (y/n)"))
		if (self.detected == 'y' or self.detected == 'Y'):
			self.surprise = False
			self.detected = True

	def think(self):
		#decision will depend on all these factors:
		#surprise
		#distance
		#aggression
		#win count
		#best count
		#rate

		# prepare calculations for win ratios
		#win_rate = self.pos_v_count/self.tot_count
		#best_rate = self.best_v_count/self.tot_count depricated
		win_rate = self.best_v_count/self.tot_count

		#error checking
		print(f"Total battles considered: {self.tot_count}")
		print(win_rate)

		###Agro Level Fanatical
		if (self.agroCount == 4):
			print("Charge")

		###Agro Level Timid
		elif (self.agroCount == 0):
			if (self.detected == False):
				if (self.distance > 2):
					print("Retreat")
				elif (self.distance < 2):
					if (win_rate > .9):
						print("Retreat")
					else:
						print("Hide")
				else:
					chance = random.randint(0,2)
					if (chance == 1):
						print("Retreat")
					else:
						print("Hide")
			else:
				if (self.distance > 2):
					print("Flee")
				elif (self.distance < 2):
					print("Surrender")
				else:
					chance = random.randint(0, 2)
					if (win_rate > .9):
						print("Flee")
					elif (chance == 1):
						print("Flee")
					else:
						print("Hide")

		###Agro Level Agressive
		elif (self.agroCount == 3):
			if (win_rate > .75):
				print("Attack")
			elif (win_rate > .5):
				print("Attack")
			elif (win_rate > .25):
				if (self.detected == False):
					if (self.distance > 2):
						print("Retreat")
					else:
						print("Fight")
				else:
					if (self.distance > 1):
						print("Retreat")
					else:
						print("Fight")
			else:
				if (self.detected == False):
					if (self.distance > 1):
						print("Retreat")
					elif (self.distance <= 1):
						print("Hide")
				else:
					if (self.distance == 0):
						print("Attack")
					else:
						print("Retreat")

		### Argo level Neutral
		elif (self.agroCount == 2):
			if (win_rate > .75):
				if (self.distance == 4):
					chance = random.randint(0, 2)
					if (chance == 1):
						print("Attack")
					else:
						print("Wait")
				elif (self.distance < 3):
					print("Attack")
				else:
					print("Prep ambush and attack when close")
			elif (win_rate > .5):
				if (self.detected == False):
					if (self.distance > 1):
						print("Call for Reinforcements/Set Up Ambush")
					else:
						print("Attack")
				else:
					if (self.distance == 4):
						print("Call for Reinforcements/Set Up Ambush")
					elif (self.distance == 3):
						chance = random.randint(0, 2)
						if (chance == 1):
							print("Attack - pot shots")
						else:
							print("Hide")
					elif (self.distance < 3):
						print("Attack")
			elif (win_rate > .25):
				if (self.detected == False):
					if (self.distance > 2):
						print("Retreat")
					elif (self.distance >= 1):
						print("Hide (and prepare ambush if detected)")
					else:
						print("Fight")
				else:
					if (self.distance > 1):
						print("Retreat")
					else:
						print("Fight to withdraw")
			else:
				if (self.detected == False):
					if (self.distance > 1):
						print("Retreat")
					elif (self.distance <= 1):
						print("Hide")
				else:
					if (self.distance == 0):
						print("Surrender")
					elif (self.distance == 1):
						print("Withdraw")
					else:
						print("Retreat")

		###Agro Level Passive
		elif (self.agroCount == 1):
			if (win_rate > .75):
				if (self.distance > 2):
					chance = random.randint(0, 3)
					if (chance == 1):
						print("Attack")
					elif (chance == 2):
						print("Negotiate")
					else:
						print("Retreat")
				elif(self.distance == 0):
					chance = random.randint(0, 2)
					if (chance == 1):
						print("Attack")
					else:
						print("Negotiate")
				elif(self.distance == 2):
					if(self.detected == False):
						print("Retreat")
					else:
						print("Fight")
				#self.distance == 1
				else:
					if (self.detected == False):
						chance = random.randint(0, 3)
						if (chance == 1):
							print("Attack")
						elif (chance == 2):
							print("Hide")
						else:
							print("Retreat")
					else:
						chance = random.randint(0, 3)
						if (chance == 1):
							print("Attack")
						elif (chance == 2):
							print("Negotiate")
						else:
							print("Retreat")
			elif (win_rate > .5):
				if (self.detected == False):
					if (self.distance > 1):
						print("Retreat")
					elif (self.distance == 1):
						print("Call for Reinforcements/Set Up Ambush")
					else:
						chance = random.randint(0, 2)
						if (chance == 1):
							print("Attack")
						else:
							print("Negotiate")
				else:
					if (self.distance == 4):
						print("Retreat")
					elif (self.distance == 3 or self.distance == 2):
						chance = random.randint(0, 3)
						if (chance == 1):
							print("Attack - pot shots")
						elif (chance == 2):
							print("Hide")
						else:
							print("Retreat")
					elif (self.distance > 0):
						print("Negotiate")
					else:
						print("Fight to withdraw")
			elif (win_rate > .25):
				if (self.detected == False):
					if (self.distance > 2):
						print("Retreat")
					elif (self.distance >= 1):
						print("Hide")
					else:
						print("Hide and Withdraw if detected")
				else:
					if (self.distance > 1):
						print("Retreat")
					else:
						print("Fight to withdraw")
			else:
				if (self.detected == False):
					if (self.distance > 1):
						print("Retreat")
					elif (self.distance <= 1):
						print("Hide")
				else:
					if (self.distance == 0):
						print("Surrender")
					elif (self.distance == 1 or self.distance == 2):
						print("Flee")
					else:
						print("Retreat")






	
