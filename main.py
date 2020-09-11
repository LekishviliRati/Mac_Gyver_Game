"""
this is a doctring. i'm here to explain what the following code will do.
oh, i'm multiline too!
"""
import numpy as np
import random



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


#two_dimensions_list = read_maze_txt("maze_structure.txt")
#print("This is two dimensional list", two_dimensions_list)

#print(two_dimensions_list[0][0])


def find_mg_position(search_area):
	# Find Mac Gyver position represented by S in our two dimensional list 
	a = search_area
	x = [line for line in a if "S" in line][0]
	#NOTE PERSO :
	# Dénition de la variable x pour chercher la position de "S" sur l'axe des abscisses, sur chaque ligne du tableau
	#[0] est le paramètre d'initialisation, à remplacer par la valeur x trouvée pour "S"
	position = (a.index(x), x.index("S"))
	return position
	#NOTE PERSO
	# a.index(x): Identification de la position de "S" sur l'axe des abcsisses grace à la fonction .index()
	# x.index("S") : Identification de la position de "S" sur l'axe des ordonnées avec fonction .index()

#mac_gyver_position = find_mg_position(two_dimensions_list)
#print("Mac Gyver Position is :", mac_gyver_position)


def count_free_spaces(search_area):
	""" This fonction will return sum of free spaces inside a given maze"""
	a = search_area
	total_of_free_spaces = 0
	empty_space = "R"
	
	for line in a:
		# NOTE PERSO : pour une liste dans la liste de listes 
		for unit_value in line:
			# NOTE PERSO : pour une une valeur dans une liste
			if empty_space in unit_value: 
				# NOTE PERSO : si cette valeur est égal à "R"
				total_of_free_spaces = total_of_free_spaces + 1
	return total_of_free_spaces


#free_spaces = count_free_spaces(two_dimensions_list)
#print("Inside this list, there is", free_spaces, "empty spaces")


def free_spaces_list(search_area):
	# This fonctionne will list free cases positions inside a list

	a = search_area
	r = "R"
	array = np.array(a)
	free_spaces_array = np.argwhere(array == r)

	return free_spaces_array


#free_spaces_positions = free_spaces_list(two_dimensions_list)
#print("Free spaces Positions are :", free_spaces_positions)

#-------------------------------------------------------------------------------#
# Essayé de retourner une liste de positions (en liste pas en tuple)
#-------------------------------------------------------------------------------#

# --> Dans cette fonction j'ai les 121 espaces libre mais je n'ai su trouvé l'indice 
# autrement que par la fonction index() qui malheureusement renvoie un tuple

# def free_spaces_list(search_area):

# 	a = search_area
# 	x = 0
# 	y = 0
# 	free_spaces_list = []
# 	empty = "R"

# 	for row in a:
# 		x = row
# 		for col in row:
# 			y = col
# 			if empty in col:
# 				print(empty)
# 				free_spaces_list.append(empty)
# 	print(free_spaces_list)


# print(free_spaces_list(two_dimensions_list))

#-------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------#
# Essayé de retourner une liste de positions (en liste pas en tuple)
# Problème me retourne seulement la position x, y de la première valeur trouvée
#-------------------------------------------------------------------------------#
# 	a = search_area
# 	free_spaces_list = []

# 	x = [line for line in a if "R" in line][0]
# 	position = [a.index(x), x.index("R")]

# 	free_spaces_list.append(position)

# 	return free_spaces_list

# #fs_list = free_spaces_list(two_dimensions_list) 
# #print("Free spaces list: ", fs_list)

#-------------------------------------------------------------------------------#



def random_choice_in_free_spaces_list(search_area):
	#This fonctionne will list free cases positions inside a list

	s = free_spaces_list(two_dimensions_list)
	# Save in a variable all free spaces available

	if free_spaces > 3:
		# If there is more than 3 free spaces
		#print("yes there is more than 3 empty spaces")
		# Check if we are in our condition
		random_choice = random.choice(s)
		# random choice inside free spaces list
		return random_choice

#free_spaces = "Random choice is : ", random_choice_in_free_spaces_list(two_dimensions_list)
#print(free_spaces)


def insert_objects_in_maze(search_area):

	a = search_area

	aiguille_position = random_choice_in_free_spaces_list(two_dimensions_list)
	tube_position = random_choice_in_free_spaces_list(two_dimensions_list)
	ether_position  = random_choice_in_free_spaces_list(two_dimensions_list)

	print( "aiguille", aiguille_position, "tube: ", tube_position, "ether: ", ether_position)

	
	x_aiguille = aiguille_position[0]
	y_aiguille = aiguille_position[1]
	a[x_aiguille][y_aiguille] = "1"

	x_tube = tube_position[0]
	y_tube = tube_position[1]
	a[x_tube][y_tube] = "2"

	x_ether = ether_position[0]
	y_ether = ether_position[1]
	a[x_ether][y_ether] = "3"


	return a


#object_added_maze = insert_objects_in_maze(two_dimensions_list)
#print("Obeject added maze : ", object_added_maze)

def objects_collection(obj):
	collected_objects_list = [] 
	added_object = obj

	total_objects = collected_objects_list.append(added_object)

	return total_objects



def move_right(search_area):
	a = search_area
	mg_initial_positions = find_mg_position(a)
	mg_position_x = mg_initial_positions[0]
	mg_position_y = mg_initial_positions[1]


	if mg_position_y+1 in range(15):
		target_position = a[mg_position_x][mg_position_y+1]
		if target_position == "R":
			mg_position_y = mg_position_y +1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x][mg_position_y-1] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			return new_mg_position
		if target_position == "W":
			print("Vous ne pouvez traverser les murs ! ")
		if target_position == "1":
			mg_position_y = mg_position_y +1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x][mg_position_y-1] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			found_objects[0] = "AIGUILLE"
			print(found_objects)
			return new_mg_position
		if target_position == "2":
			mg_position_y = mg_position_y +1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x][mg_position_y-1] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			found_objects[1] = "TUBE"
			print(found_objects)
			return new_mg_position
		if target_position == "3":
			mg_position_y = mg_position_y +1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x][mg_position_y-1] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			found_objects[2] = "ETHER"
			print(found_objects)
			return new_mg_position
		if target_position == "E":
			mg_position_y = mg_position_y -1
			if found_objects == weapon:
				a[mg_position_x][mg_position_y] = "S"
				a[mg_position_x][mg_position_y+1] = "R"
				#NOTE PERSO : permet de déplacer S vers la gauche et replacer la case qui contenait S par R. 			
				new_mg_position = find_mg_position(two_dimensions_list)
				print(a)
				print("Tous les objets ont été récoltés, vous avez GAGNÉ")
				return new_mg_position
			elif found_objects != weapon:
				a[mg_position_x][mg_position_y] = "S"
				a[mg_position_x][mg_position_y+1] = "R"
				new_mg_position = find_mg_position(two_dimensions_list)
				print(a)
				print("Vous avez perdu, le gardien vous a capturé")
				return new_mg_position								
	else:
		print("Mg cannot leave the maze")
	return a

###############################################################################################

# !!!! Problème avec ce code : quand MG a comme target_position y > 14 le jeux plante !!!!

###############################################################################################
	# if target_position == "R":
	# 	mg_position_y = mg_position_y +1
	# 	if mg_position_y in range(15):
	# 		# MG stays in maze, can't go out of it by left side
	# 		a[mg_position_x][mg_position_y] = "S"
	# 		a[mg_position_x][mg_position_y-1] = "R"
	# 		#NOTE PERSO : permet de déplacer S vers la gauche et replacer la case qui contenait S par R. 
	# 		new_mg_position = find_mg_position(two_dimensions_list)
	# 		print(a)
	# 		return new_mg_position
	# 	else : 
	# 		print("Mg cannot leave the maze")
	# 	return a

###############################################################################################

	# if target_position == "W":
	# 	return "Vous ne pouvez passer, car il y a un mur"

###############################################################################################

	# if target_position == "1":
	# 	mg_position_y = mg_position_y +1
	# 	if mg_position_y in range(15):
	# 		# MG stays in maze, can't go out of it by right side
	# 		a[mg_position_x][mg_position_y] = "S"
	# 		a[mg_position_x][mg_position_y-1] = "R"
	# 		#NOTE PERSO : permet de déplacer S vers la droite et replacer la case qui contenait S par R.
	# 		new_mg_position = find_mg_position(two_dimensions_list)
	# 		print(a)
	# 		found_objects[0] = "AIGUILLE"
	# 		print(found_objects)
	# 		return new_mg_position
	# 	else :
	# 		print("Mg cannot leave the maze")	

	# if target_position == "2":
	# 	mg_position_y = mg_position_y +1
	# 	if mg_position_y in range(15):
	# 		# MG stays in maze, can't go out of it by right side
	# 		a[mg_position_x][mg_position_y] = "S"
	# 		a[mg_position_x][mg_position_y-1] = "R"
	# 		#NOTE PERSO : permet de déplacer S vers la droite et replacer la case qui contenait S par R.
	# 		new_mg_position = find_mg_position(two_dimensions_list)
	# 		print(a)
	# 		found_objects[1] = "TUBE"
	# 		print(found_objects)			
	# 		return new_mg_position
	# 	else :
	# 		print("Mg cannot leave the maze")	

	# if target_position == "3":
	# 	mg_position_y = mg_position_y +1
	# 	if mg_position_y in range(15):
	# 		# MG stays in maze, can't go out of it by right side
	# 		a[mg_position_x][mg_position_y] = "S"
	# 		a[mg_position_x][mg_position_y-1] = "R"
	# 		#NOTE PERSO : permet de déplacer S vers la droite et replacer la case qui contenait S par R.
	# 		new_mg_position = find_mg_position(two_dimensions_list)
	# 		print(a)
	# 		found_objects[2] = "ETHER"
	# 		print(found_objects)
	# 		return new_mg_position
	# 	else :
	# 		print("Mg cannot leave the maze")	

#print(move_right(two_dimensions_list, mac_gyver_position))
#print(move_right(two_dimensions_list, mac_gyver_position))
###############################################################################################

def move_left(search_area):
	a = search_area
	mg_initial_positions = find_mg_position(a)
	mg_position_x = mg_initial_positions[0]
	mg_position_y = mg_initial_positions[1]
	

	if mg_position_y-1 in range(15):
		target_position = a[mg_position_x][mg_position_y-1]
		if target_position == "R":
			mg_position_y = mg_position_y -1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x][mg_position_y+1] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			return new_mg_position
		if target_position == "W":
			print("Vous ne pouvez traverser les murs ! ")
		if target_position == "1":
			mg_position_y = mg_position_y -1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x][mg_position_y+1] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			found_objects[0] = "AIGUILLE"
			print(found_objects)
			return new_mg_position
		if target_position == "2":
			mg_position_y = mg_position_y -1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x][mg_position_y+1] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			found_objects[1] = "TUBE"
			print(found_objects)
			return new_mg_position
		if target_position == "3":
			mg_position_y = mg_position_y -1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x][mg_position_y+1] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			found_objects[2] = "ETHER"
			print(found_objects)
			return new_mg_position
		if target_position == "E":
			mg_position_y = mg_position_y -1
			if found_objects == weapon:
				a[mg_position_x][mg_position_y] = "S"
				a[mg_position_x][mg_position_y+1] = "R"
				#NOTE PERSO : permet de déplacer S vers la gauche et replacer la case qui contenait S par R. 			
				new_mg_position = find_mg_position(two_dimensions_list)
				print(a)
				print("Tous les objets ont été récoltés, vous avez GAGNÉ")
				return new_mg_position
			elif found_objects != weapon:
				a[mg_position_x][mg_position_y] = "S"
				a[mg_position_x][mg_position_y+1] = "R"
				new_mg_position = find_mg_position(two_dimensions_list)
				print(a)
				print("Vous avez perdu, le gardien vous a capturé")
				return new_mg_position
	else:
		print("Mg cannot leave the maze")
	return a

###############################################################################################
	# if target_position == "E":
	# 	mg_position_y = mg_position_y -1
	# 	if mg_position_y in range(15):
	# 		if found_objects == weapon:
	# 			a[mg_position_x][mg_position_y] = "S"
	# 			a[mg_position_x][mg_position_y+1] = "R"
	# 			#NOTE PERSO : permet de déplacer S vers la gauche et replacer la case qui contenait S par R. 			
	# 			new_mg_position = find_mg_position(two_dimensions_list)
	# 			print(a)
	# 			print("Tous les objets ont été récoltés, vous avez GAGNÉ")
	# 			return new_mg_position
	# 		elif found_objects != weapon:
	# 			a[mg_position_x][mg_position_y] = "S"
	# 			a[mg_position_x][mg_position_y+1] = "R"
	# 			new_mg_position = find_mg_position(two_dimensions_list)
	# 			print(a)
	# 			print("Vous avez perdu, le gardien vous a capturé")
	# 			return new_mg_position

###############################################################################################

def move_up(search_area):
	a = search_area
	mg_initial_positions = find_mg_position(a)
	mg_position_x = mg_initial_positions[0]
	mg_position_y = mg_initial_positions[1]

	if mg_position_x-1 in range(15):
		target_position = a[mg_position_x-1][mg_position_y]
		if target_position == "R":
			mg_position_x = mg_position_x -1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x+1][mg_position_y] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			return new_mg_position
		if target_position == "W":
			print("Vous ne pouvez traverser les murs ! ")
		if target_position == "1":
			mg_position_x = mg_position_x -1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x+1][mg_position_y] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			found_objects[0] = "AIGUILLE"
			print(found_objects)
			return new_mg_position
		if target_position == "2":
			mg_position_x = mg_position_x -1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x+1][mg_position_y] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			found_objects[1] = "TUBE"
			print(found_objects)
			return new_mg_position
		if target_position == "3":
			mg_position_x = mg_position_x -1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x+1][mg_position_y] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			found_objects[2] = "ETHER"
			print(found_objects)
			return new_mg_position
		if target_position == "E":
			mg_position_x = mg_position_x -1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x+1][mg_position_y] = "R"
			if found_objects == weapon:
				new_mg_position = find_mg_position(two_dimensions_list)			
				print(a)
				print("Tous les objets ont été récoltés, vous avez GAGNÉ")
				return new_mg_position
			elif found_objects != weapon:
				new_mg_position = find_mg_position(two_dimensions_list)
				print(a)
				print("Vous avez perdu, le gardien vous a capturé")
				return new_mg_position
	else:
		print("Mg cannot leave the maze")
	return a	



def move_down(search_area):
	a = search_area
	mg_initial_positions = find_mg_position(a)
	mg_position_x = mg_initial_positions[0]
	mg_position_y = mg_initial_positions[1]
	
	if mg_position_x+1 in range(15):
		target_position = a[mg_position_x+1][mg_position_y]
		if target_position == "R":
			mg_position_x = mg_position_x +1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x-1][mg_position_y] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			return new_mg_position
		if target_position == "W":
			print("Vous ne pouvez traverser les murs ! ")
		if target_position == "1":
			mg_position_x = mg_position_x +1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x-1][mg_position_y] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			found_objects[0] = "AIGUILLE"
			print(found_objects)
			return new_mg_position
		if target_position == "2":
			mg_position_x = mg_position_x +1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x-1][mg_position_y] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			found_objects[1] = "TUBE"
			print(found_objects)
			return new_mg_position
		if target_position == "3":
			mg_position_x = mg_position_x +1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x-1][mg_position_y] = "R"
			new_mg_position = find_mg_position(two_dimensions_list)
			print(a)
			found_objects[2] = "ETHER"
			print(found_objects)
			return new_mg_position
		if target_position == "E":
			mg_position_x = mg_position_x +1
			a[mg_position_x][mg_position_y] = "S"
			a[mg_position_x-1][mg_position_y] = "R"
			if found_objects == weapon:
				new_mg_position = find_mg_position(two_dimensions_list)			
				print(a)
				print("Tous les objets ont été récoltés, vous avez GAGNÉ")
				return new_mg_position
			elif found_objects != weapon:
				new_mg_position = find_mg_position(two_dimensions_list)
				print(a)
				print("Vous avez perdu, le gardien vous a capturé")
				return new_mg_position
	else:
		print("Mg cannot leave the maze")
	return a	





###################### GAME ######################

mg_new_positions = (0, 0)
end_positions = (14, 8)
two_dimensions_list = read_maze_txt("maze_structure.txt")
mac_gyver_position = find_mg_position(two_dimensions_list)
free_spaces = count_free_spaces(two_dimensions_list)
free_spaces_positions = free_spaces_list(two_dimensions_list)
object_added_maze = insert_objects_in_maze(two_dimensions_list)
found_objects = [" ", " ", " "]
weapon = ['AIGUILLE', 'TUBE', 'ETHER']


print(object_added_maze)
print("found_objects: ", found_objects)


while mg_new_positions != end_positions:
	direction = input("Indiquez une direction: ")
	if direction == "r":
 		mg_new_positions = move_right(two_dimensions_list)

	if direction == "l":
 		mg_new_positions = move_left(two_dimensions_list)

	if direction == "u":
 		mg_new_positions = move_up(two_dimensions_list)

	if direction == "d":
 		mg_new_positions = move_down(two_dimensions_list)

	if direction == "e":
		# STOP playing
		break


print("FIN !")


###################### GAME ######################


















