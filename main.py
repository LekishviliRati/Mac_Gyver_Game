"""
this is a doctring. i'm here to explain what the following code will do.
oh, i'm multiline too!
"""

# OPEN .TXT FILE 

def read_maze_txt(maze):
	two_dimensions_list = []
	#create an empty list
	with open(maze, "r") as file:
	# NOTE PERSO : with open(filename, mode) 'r' for onmly read the file, 'w' for only write writting, for appending
		txt_reading = file.read().splitlines()
		#cut file by line
		for line in txt_reading:
		#Create a 2 dimensions table by cutting lines by letters
			list_letter = [i for i in line]
			#Modifié : two_dimensions_list = two_dimensions_list + [list_letter]
			two_dimensions_list.append(list_letter)
		return two_dimensions_list

two_dimensions_list = read_maze_txt("maze_structure.txt")
print(two_dimensions_list)

#print(two_dimensions_list[14][8])


def find_mg_position(search_area):
	# Find Mac Gyver position represented by S in our two dimensional list 
	a = search_area
	x = [line for line in a if "S" in line][0]
	#NOTE PERSO : 
	# Dénition de la variable x pour chercher la position de "S" sur l'axe des abscisses, sur chaque ligne du tableau
	#[0] est le paramètre d'initialisation, à remplacer par la valeur x trouvée pour "S"
	return (a.index(x), x.index("S"))
	#NOTE PERSO
	# a.index(x): Identification de la position de "S" sur l'axe des abcsisses grace à la fonction .index()
	# x.index("S") : Identification de la position de "S" sur l'axe des ordonnées avec fonction .index()

mac_gyver_position = find_mg_position(two_dimensions_list)
print("Mac Gyver Position is :", mac_gyver_position)
