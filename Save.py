import StageClass
#Author: Andrew Somerville
def save(stage):
    'Allows for the current game to be saved for a later time.\
     The convinience of this function fills you with determination.'
    saveFile = open('save.txt', 'w+')#Creates the file to be saved in.
    saveFile.write(str(stage.gridSize) + '\n')#the grid size is put in 1st line
    #Grid is saved with every x axis on its own line.
    for xAxis in range(len(stage.grid)):
        for yAxis in range(len(stage.grid[xAxis])):
            saveFile.write(str(stage.grid[xAxis][yAxis]))
        saveFile.write('\n')   
    #Amount of moves remaining and the total move count are saved in the last
    #two lines
    saveFile.write(str(stage.movesRemaining) + '\n' + str(stage.totalSlides))
    saveFile.close()
    
    

def load():
    'Allows for a game contained in text to be played.'
    saveFile = open('save.txt', 'r')#opens the file to read it. 
    #Reads the file line by line in the order that the info would be saved in.
    gridSize = ((saveFile.readline()).replace('\n', ''))
    stage = StageClass.Stage(int(gridSize))
    grid = []
    for line in range(int(gridSize)):
        xAxis = list((saveFile.readline()).replace('\n', ''))
        grid.append(xAxis)
    stage.grid = grid
    stage.movesRemaining = int((saveFile.readline()).replace('\n', ''))
    stage.totalSlides = int((saveFile.readline()).replace('\n', ''))
    saveFile.close()
    return stage
    
    
    
        
    
