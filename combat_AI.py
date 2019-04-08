import random, DnD, types


class combat_stats:



	def __init__(self):
		print("in init")
	

	def getOdds(self,enemies,friendlies):

		friendList = []
		enemyList = []
		count = 0		

		
		for i in range(enemies):
			Type = str(input("Type of enemies: "))				
			enemyList.insert(i,Type)

		for j in range(friendlies):
			Type = str(input("Type of Friendlies: "))         
			friendList.insert(j,Type)

		for q in range(enemies):

			Friendly= DnD.Creature(friendList[q])
			Enemy = DnD.Creature(enemyList[q])
			rate=DnD.Encounter(Friendly,Enemy).predict()
#			print(rate[1])  
#			print(rate[3])
#			print(rate)
			if(rate[1] > rate[3]):
				count += 1
				print("Count")
				print(count)			
		
			
			
	
