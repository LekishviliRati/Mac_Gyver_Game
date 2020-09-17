from back_end import Map, Character
from configuration import *

player = Character()
myMap = Map(player)
end = myMap.end_position
# # Censé fonctionner
# myMap.setMovement("z")
# myMap.setMovement("s")
# myMap.setMovement("q")
# myMap.setMovement("d")
# #
# # Ne fonctionne pas
# myMap.setMovement("k")
# myMap.setMovement("v")
# myMap.setMovement("h")
# myMap.setMovement("l")

x = end[0]
y = end[1]

#while myMap.maze[14][8] != "S":
while myMap.maze[x][y] != letterOfCharacter:
    letter = input("Entrez une direction: ")
    myMap.setMovement(letter)
else:
    print("FIN")
