from configuration import *
from back_end import Character
from random import randint

class Map:

    def __init__(self, player):
        self.maze = []
        self.isPlayable = True
        self.character = player
        self.read_maze_txt()
        self.find_player_position()
        self.set_objects()
        self.display_map()
        self.objects = self.character.objects
        #AJOUT
        self.end_position = (0, 0)
        self.find_end_position()


    def read_maze_txt(self):
        two_dimensions_list = []
        with open(configFile, "r") as file:
            txt_reading = file.read().splitlines()
            for line in txt_reading:
                list_letter = [i for i in line]
                two_dimensions_list.append(list_letter)
            self.maze = two_dimensions_list
            #print("Le lab est stocké")

    def display_map(self):
        for x in range(maxX):
            print(self.maze[x])

    def find_player_position(self):
        for x in range(maxX):
            for y in range(maxY):
                if self.maze[x][y] is letterOfCharacter:
                    #print("Le personage est en position", x, y)
                    self.character.setCoordinates(x, y)
    # AJOUT
    def find_end_position(self):
        for x in range(maxX):
            for y in range(maxY):
                if self.maze[x][y] is letterForEnding:
                    self.end_position = (x, y)

    def set_objects(self):
        listOfFreePositions = []
        numberOfObject = 1

        for x in range(maxX):
            for y in range(maxY):
                if self.maze[x][y] is letterForSpace:
                    freePosition = (x, y)
                    listOfFreePositions.append(freePosition)
        totalFreeSpaces = len(listOfFreePositions) -1
        if totalFreeSpaces >= maxObjects -1:
            for i in range(maxObjects):
                randomInt = randint(0, totalFreeSpaces)
                object_coordinates = listOfFreePositions[randomInt]
                listOfFreePositions.remove(object_coordinates)
                totalFreeSpaces -= 1
                x = object_coordinates[0]
                y = object_coordinates[1]
                self.maze[x][y] = numberOfObject
                numberOfObject += 1
                #self.display_map()

    def setMovement(self, inputType):
        # On part du principe que inputType c'est la lettre envoyée par l'utilisateur
        x = self.character.x
        y = self.character.y

        inputMove = {
            inputUp: {
                "x": -1,
                "y": 0
            },
            inputDown: {
                "x": +1,
                "y": 0
            },
            inputLeft: {
                "x": 0,
                "y": -1
            },
            inputRight: {
                "x": 0,
                "y": +1
            },

        }
        #print(inputMove)
        #print(inputType)
        if inputType in inputMove:
            self.doMoovement(x + inputMove[inputType]["x"], y + inputMove[inputType]["y"])
        else:
            print("Ne fonctionne pas")


    def doMoovement(self, newX, newY):
        # Cette méthode met à jour la carte et bouge le personnage
        # Indices  : self.character.moove(x, y)
        # self.maze[x][y] = letterForSpace
        # self.maze[newX][newY] = letterForCharacter
        x = self.character.x
        y = self.character.y

        if newX in range(maxX) and newY in range(maxY):
            target_position = self.maze[newX][newY]
            if target_position != letterForWalls:
                if target_position == letterForSpace:
                    #print("Target poisition", target_position)
                    # self.maze[x][y] = letterForSpace
                    # self.character.moove(newX, newY)
                    # self.maze[newX][newY] = letterOfCharacter
                    # self.find_player_position()
                    # self.display_map()
                    self.update_map(newX, newY)
                if target_position == 1 or target_position == 2 or target_position == 3:
                    # self.maze[x][y] = letterForSpace
                    # self.character.moove(newX, newY)
                    # self.maze[newX][newY] = letterOfCharacter
                    # self.find_player_position()
                    # self.display_map()
                    self.update_map(newX, newY)
                    #self.addObject() -> ne fontionne pas malgrès l'import de la classe Character depuis back_end
                    self.objects = self.objects + 1
                    print("Self.Objects = ", self.objects)
                if target_position == letterForEnding:
                    # self.maze[x][y] = letterForSpace
                    # self.character.moove(newX, newY)
                    # self.maze[newX][newY] = letterOfCharacter
                    # self.find_player_position()
                    # self.display_map()
                    self.update_map(newX, newY)
                    if self.objects == maxObjects:
                        print("Gagné !")
                    if self.objects != maxObjects:
                        print("Perdu :( ")
            else:
                print("Impossible de passer à travers un mur ! ")
        else:
            print("Ne peut pas sortir de la carte")

    def update_map(self, newX, newY):
        x = self.character.x
        y = self.character.y

        self.maze[x][y] = letterForSpace
        self.character.moove(newX, newY)
        self.maze[newX][newY] = letterOfCharacter
        self.find_player_position()
        self.display_map()