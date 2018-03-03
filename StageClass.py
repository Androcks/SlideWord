#Stage Class
#Data Grid which the player can manipulate via slide functions
#It can be created with letters initially generated
#Fills empty spaces with letters
#Author : Andrew Somerville
import randomTest
import Save
import WordFinder
class Stage():
    def __init__(self, gridSize):
        'Creates a Grid Based off a predetermined Grid Size. \
         For MVP this will be set to 6 by default.'
        self.alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        #Storing the alphabet like this is very messy and inefficient.
        #perhaps move to a Unicode Based adding system?
        # This will work for Stage Testing
        self.gridSize = int(gridSize)
        #Holds the size of the grid
        self.movesRemaining = 1   #This keeps track of the number of moves the user has left
        #Every time a slide is made, we decrement moves by 1
        #Eventually we will have to increment movesRemaining by 2 everytime a word is found
        self.totalSlides = 0 # Acts as the score for the player.
        self.foundWords = [] #Initial empty list to be used later


        #An algorithmic way to create a grid of size gridSize x gridSize
        self.grid = []
        for row in range(self.gridSize):
            self.grid.append([])
            for column in range(self.gridSize):
                self.grid[row].append('$')
        
        
        #Default "empty" grid (2d "list of lists" with $ as default).
    def getList(self):
        stageList = []
        for xAxis in self.grid:
            sublist = []
            for element in xAxis:       
                sublist.append(element)  
            stageList.append(sublist)
            
        return stageList  
    

       

    def gridDisplay(self):
        'Displays the current Grid In ASCII style graphics.'
        print()
        print(end = '')
        
        for xAxis in self.grid:
            for yAxis in xAxis:# prints segments side by side
                print(yAxis, end=' ')
            print()# finishes the line, moves on to next
        print()
        #Shows amount of moves remaining
        print(self.movesRemaining, " moves remaining")
        #Shows total amount of moves
        print(self.totalSlides, " made this game!")
        
        

    def letFill(self):
        'Fills empty space with new random letters.\
         Letters randomly assigned via RandomGen'
        for xAxis in range(len(self.grid)):#for every xaxis list in the grid
            for yAxis in range(len(self.grid[xAxis])):
                if self.grid[xAxis][yAxis] == '$':
                    #Replaces Empty Space with randomly assigned letter from
                    #semi-random generator.
                    #Now getting letters from our scrabble distribution
                    self.grid[xAxis][yAxis] = randomTest.grabALetter()
        

    def letDel(self, x, y, wordLength = 3, orient = True):
        'Deletes letters in stage replacing them with empty "$". \
    xStart & yStart are starting coords for deletion\
    wordLength is length of deletion from the left or down the starting point\
    orient is the orientation of deletion (True/False) (vertical/horizontal).'
        self.grid[x][y] = '$' #Replaces value at x,y coord with $
        #self.gridDisplay()
        print()
        #letDel functions recusively.
        #if the wordLength is not 1 (as it detracts 1 from wordLength every
        #letter), it will go to the next area of the letter, depending on
        #the orientation.
        if wordLength != 1 and orient == True:
            self.letDel(x + 1, y, wordLength - 1, orient)
        elif wordLength != 1:
            self.letDel(x, y + 1, wordLength - 1, orient)

    def letLineInsert(self, x, y, wordLength = 3, orient = True):
        'Inserts letters into space in line formation.\
    Essentially, the opposite of letDel. See letDel'
        self.grid[x][y] = randomTest.grabALetter() #Random Letters replace space
        #LetLineInsert works recursively. Same logic as LetDel
        if wordLength != 1 and orient == True:
            self.letLineInsert(x + 1, y, wordLength - 1, orient)
        elif wordLength != 1:
            self.letLineInsert(x, y + 1, wordLength - 1, orient)

    def slide(self, startx, starty, orient, move):
        'Moves letters within grid in a wrapparound style.\
    Startx & StartY implement coords of the letter to be moved.\
    orient can be string u, d, r, and l, for directions.\
    move is the amount of space the letter is to be moved.'

        
        if move < 0: # In case of a negative number, the orient is switched.
            if orient == 'r':
                orient = 'l'
            elif orient == 'r':
                orient = 'l'
            elif orient == 'u':
                orient = 'd'
            elif orient == 'd':
                orient = 'u'
            move = move * -1
            
            
        self.movesRemaining -= 1    #After each move, the user will lose a move
        self.totalSlides += 1
        # Creates A temporary list to translate new letter positions to.
        tempLine = ['$']*self.gridSize
        #if orient != 'r' or 'l' or 'u' or 'd':
            #print("Please try again, using u, d, l, or r as orient.")
        if orient == 'r':# if they want to move it right (the x direction
            for letter in range(self.gridSize):
                # check to prevent moved letter from going "off list"
                if ((letter + 1) + move) <= self.gridSize:
                    tempLine[letter + move] = self.grid[startx - 1][letter]
                    # letter is placed in tempLine "move" spaces to the right.

                # If the letter would go "off list" it is moved to the beginning,
                #wrapping around.
                else:
                    tempLine[letter - (self.gridSize - move)] = self.grid[startx - 1][letter]
                    #Letters in templine are transfered to the line in self.grid
            
            self.grid[startx - 1] = tempLine
        elif orient == 'l':# if they want to move a letter left, we just move the letters right enough
            #to make it LOOK like it moved left. We're lazy like that.
            self.movesRemaining += 1
            self.slide(startx, starty, 'r', (self.gridSize - move))

        elif orient == 'd' :# if they want to move it down (y direction)
            for letter in range(self.gridSize):
                if ((letter + 1) + move) <= self.gridSize:#Same "off line" prevention as in 'r'
                    tempLine[letter + move] = self.grid[letter][starty - 1]
                else:
                    tempLine[letter - (self.gridSize - move)] = self.grid[letter][starty - 1]
            #print(tempLine)debug
            for letter in range(self.gridSize):
                #As each letter is technically on a seperate list, it must go through each list
                #to replace the letters.
                self.grid[letter][starty - 1] = tempLine[letter]

        elif orient == 'u':# if they want to move it up (y direction)
            self.movesRemaining += 1                    #When the slide function is called recursively
            self.totalSlides -= 1   
            self.slide(startx, starty, 'd', (self.gridSize - move))# We just move it down instead.
            
        
            # They won't be the wiser.


    

         
        
        
                
        

        
    
