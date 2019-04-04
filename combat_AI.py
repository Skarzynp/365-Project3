import random, DnD, types


class combat_stats:



	def __init__(self):
		print("in init")
	

	def getOdds(self,enemys,friendlies):
		
		for z in range(enemys):
			for i in range(enemys):
				Enemy=DnD.Creature("Wolf",base="owlbear",alignment='evil')
			for j in range(friendlies):
				Friendly=DnD.Creature("Dog",base="commoner",alignment='good')

		
		rate=DnD.Encounter(Friendly,Enemy).predict()
		print(rate)
		


	
