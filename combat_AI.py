import random, DnD, types
import itertools

class combat_stats:



	def __init__(self):
		print("in init")
	

	def getOdds(self,enemies,friendlies):

		friendList = []
		enemyList = []
		cur_count = 0		
		best_count = 0
		
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
			if(rate[1] > rate[3]):
				cur_count =+1
		print('Anticipated wins based on current orientation:', cur_count) 	
			
												
		for r in itertools.product(friendList, enemyList):
			Friendly= DnD.Creature(r[0])
			Enemy = DnD.Creature(r[1])
			rate=DnD.Encounter(Friendly,Enemy).predict()
			if(rate[1] > rate[3]):
				best_count += 1
                                
		print('Possible amount of favoriable encounters:', best_count)												
