
from combat_AI import combat_stats
import DnD


print("AI Script")
c = combat_stats()

try:
	enemies = int(input("How many enemies: "))
except ValueError:
	print("Not a Number")

try:
	friendlies = int(input("How many friendlies: "))
except ValueError:
	print("Not a Number")


c.getOdds(enemies,friendlies)


