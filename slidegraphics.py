import pygame,sys, os
import random
from pygame.locals import *


import StageClass
import WordFinder
import graphicWordFinder
import Save





def getClickLoc(coordinates):   #A function that takes in a set of coordinates and returns the location of the letter we clicked on
    if coordinates[0] > hborder and coordinates[1] > vborder and coordinates[0] < screenWidth - hborder and coordinates[1] < screenHeight - vborder:           #if we clicked on a letter
        for block in range(gridSize):
            if coordinates[0] <= (hborder + letterSize*(block + 1)) and coordinates[0] > (hborder + letterSize*(block)):
                i = block + 1
            if coordinates[1] <= (vborder + letterSize*(block + 1)) and coordinates[1] > (vborder + letterSize*(block)):
                j = block + 1
        return (j,i)

def blitGrid(): #The function that actually puts stuff on the screen
    global stageList
    global saveRect
    for i, row in enumerate(stageList):     #These for loops iterate through each letter in our list of lists
        for j, element in enumerate(row):
            isani = 0                                   #A variable meant to make I's appear centred in their cell
            if stageList[i][j] == 'I':
                isani = letterSize / 5.3
            textObj = font.render(stageList[i][j], True, colors[i][j])
            screen.blit(textObj,(hborder + letterSize*j + isani ,vborder + letterSize*i))      #Place the letter on the screen
    scoreText = font2.render(str(stage.movesRemaining), True, red)                       #Rendering the "Score" font
    scoreRect = scoreText.get_rect()
    scoreRect.centerx = screenWidth - hborder
    scoreRect.centery = (screenHeight + vborder + gridSize*letterSize) / 2
    screen.blit(scoreText,scoreRect)
    
    slidesText = font2.render(str(stage.totalSlides), True, green)                       #Rendering the "Score" font
    slidesRect = slidesText.get_rect()
    slidesRect.centerx = hborder/2
    slidesRect.centery = (screenHeight + vborder + gridSize*letterSize) / 2
    screen.blit(slidesText,slidesRect)    
    
    saveText = saveFont.render("Save Game", True, saveGameColor)        #Showing the save icon
    saveRect = saveText.get_rect()
    saveRect.centery = vborder/4
    saveRect.centerx = screenWidth - hborder
    screen.blit(saveText,saveRect)
    
    helpText = saveFont.render("Help", True, helpColor)        #Showing the save icon
    helpRect = helpText.get_rect()
    helpRect.centery = vborder/4
    helpRect.centerx = hborder
    screen.blit(helpText,helpRect)    
    
    wordsFoundText = font3.render('Words Found:', True, black)      #Showing the words found font
    wordsFoundRect = wordsFoundText.get_rect()
    wordsFoundRect.centerx = screenWidth - hborder/1.5
    wordsFoundRect.centery = vborder - 40
    screen.blit(wordsFoundText, wordsFoundRect)
    
    for i,word in enumerate(reversed(stage.foundWords)):            #Showing the list of found words
        wordText = font3.render((word),True, green)
        wordRect =  wordText.get_rect()
        wordRect.centerx = screenWidth - hborder/2
        wordRect.centery = vborder + 25*i
        
        

    
        if wordRect.centery < screenHeight - vborder:       #We cut off the list if too many words are shown
            screen.blit(wordText, wordRect)
    
    
            
            
def mouseClick(pos):    #This function handles everything that needs to happen when we click the mouse (left click only)
    if pos[0] > hborder and pos[1] > vborder and pos[0] < screenWidth - hborder and pos[1] < screenHeight - vborder:   #if we clicked on a letter
        global firstClick
        global secondClick
        if firstClick == (0,0):                                       #If the user hasn't clicked a letter yet
            firstClick = getClickLoc(pos)
            colors[firstClick[0]-1][firstClick[1]-1] = red     
        elif secondClick == (0,0):                                    #If the user has clicked exactly one letter
            secondClick = getClickLoc(pos)
            colors[secondClick[0]-1][secondClick[1]-1] = red     
        else:                                              #If the user has clicked two letters
            graphicSlide()                                 #must have first and second click defined to call graphicSlide
            

def graphicSlide():     #This function determines what parameters to pass to the stage.slide() function
    global stage
    if firstClick[0] == secondClick[0]:             #If the selected letters are in the same row
        stage.slide(firstClick[0],firstClick[1],'r',secondClick[1]-firstClick[1])
        
    elif firstClick[1] == secondClick[1]:             #If the selected letters are in the same column
        stage.slide(firstClick[0],firstClick[1],'u',firstClick[0] - secondClick[0])
    
    while graphicWordFinder.graphicWordFinder(stage) == True:       #After a slide is made, we check for words
            #stage.gridDisplay()
        graphicWordFinder.graphicWordFinder(stage, False)       
        
        
         
    reset()    #We have made the slide, now we want everything reset
        
        
def reset():    #A function that reset the color grid, and the first and second clicks
    global colors
    global firstClick
    global secondClick
    global stageList
    global stage
    colors = [[letterColor for x in range(gridSize)] for y in range(gridSize)]  #Reset the color grid
    firstClick = (0,0)          #Reset the first click
    secondClick = (0,0)             #Reset the second click
    stageList = stage.getList()     #Must copy the new stage to our stageList object for iterability
    
    
def showWord(word,stage):
   
    print('showWord: ' + word)
    stage.foundWords.append(word)   #If a word is made, we add it too the foundWords list


def helpScreen():
    helpscreen = True
    while helpscreen:
    
        for event in pygame.event.get():
            if event.type == QUIT:              #So that we can exit the game by clicking the red x
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:      #We return to the game after a click
                helpscreen = False
        
        screen.blit(background,(0,0))      
        for i, scentence in enumerate(helpMessage):         #Here we display the help message
            
            currentText = smallfont.render(scentence, True, black)   
            currentRect = currentText.get_rect()
            currentRect.centerx = screen.get_rect().centerx
            currentRect.centery = 100 + (currentRect.height+5)*i
            screen.blit(currentText,currentRect)
        
            
         
        pygame.display.update()         #Update the dispay
            

def gameOverScreen():       #This screen displays after the user gets to 0 moves
    while True:
    
        for event in pygame.event.get():
            if event.type == QUIT or event.type == pygame.MOUSEBUTTONUP:              #So that we can exit the game by clicking the red x
                pygame.quit()
                sys.exit()    
           
        screen.blit(background,(0,0)) 
        currentText = font2.render('Your Score: ' + str(stage.totalSlides), True, black)        #Making the text to display
        currentRect = currentText.get_rect()
        currentRect.centerx = screen.get_rect().centerx
        currentRect.centery = screen.get_rect().centery + 100
        screen.blit(currentText,currentRect)   
        
        currentText = font2.render("Game Over!", True, black) 
        currentRect = currentText.get_rect()
        currentRect.centerx = screen.get_rect().centerx
        currentRect.centery = screen.get_rect().centery - 100
        screen.blit(currentText,currentRect)           
        pygame.display.update()
    

    
def runGame():
    global saveGameColor
    global helpColor
    while True:                         #This is our main game loop
        if stage.movesRemaining <= 0:
            gameOverScreen()
            
        saveGameColor = black
        helpColor = black
        for event in pygame.event.get():
            if event.type == QUIT:              #So that we can exit the game by clicking the red x
                pygame.quit()
                sys.exit()
                
                
            if event.type == pygame.MOUSEBUTTONUP:      #If we click the mouse
                if event.button == 1:               #If the mouse click was a left click
                    if saveRect.collidepoint(pygame.mouse.get_pos()):     #If we clicked on "save game"
                        Save.save(stage)
                        print('saving')
                    if helpRect.collidepoint(pygame.mouse.get_pos()):   #If we click on "help"
                        helpScreen()
                    mouseClick(pygame.mouse.get_pos())      #call the mouse click method on the coordinates
                else:
                    reset()             #We want a right click or any other kind of click to be an "undo" command
        if saveRect.collidepoint(pygame.mouse.get_pos()):   #Save button should turn red when we hover over it
            saveGameColor = hoverColor
        if helpRect.collidepoint(pygame.mouse.get_pos()):  #Same with the help buttong
            helpColor = hoverColor
            
    
        screen.blit(background,(0,0))       #Refresh the background image
        blitGrid()                          #Refresh the grid
        pygame.display.update()         #Update the dispay





       
def startMenu(newGameColor,loadGameColor, hoverColor, newGameRect, loadGameRect):
    global stageList
    global stage
    while True:         #This loop controls the start screen

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if newGameRect.collidepoint(pygame.mouse.get_pos()):
                    stage = StageClass.Stage(gridSize)      #Initiallizing a stage
                    stage.letFill()
                    
                    while graphicWordFinder.graphicWordFinder(stage, False) == True:#Constantly checks the generated and loaded grids to
                        #so as to avoid initial generation making words, or cheaters.
                        graphicWordFinder.graphicWordFinder(stage, False)   
                        
                        
                    stageList = stage.getList()  
                    runGame()
                if loadGameRect.collidepoint(pygame.mouse.get_pos()):
                    stage = Save.load()
                    stageList = stage.getList()
                    runGame()
 
        if newGameRect.collidepoint(pygame.mouse.get_pos()):
            newGameColor = hoverColor
        if loadGameRect.collidepoint(pygame.mouse.get_pos()):
            loadGameColor = hoverColor
            
            
        newGameText = font.render("New Game", True, newGameColor) 
        h = newGameRect.centery
        newGameRect = newGameText.get_rect()
        newGameRect.centerx = screen.get_rect().centerx
        newGameRect.centery = h
        
        loadGameText = font.render("Load Game", True, loadGameColor) 
        p = loadGameRect.centery
        loadGameRect = newGameText.get_rect()
        loadGameRect.centerx = screen.get_rect().centerx
        loadGameRect.centery = p        
                
        screen.blit(background,(0,0))
        
        

        screen.blit(newGameText,newGameRect)
        screen.blit(loadGameText,loadGameRect)
        
        pygame.display.update()
        newGameColor = black
        loadGameColor = black



#Initializing stuff for the start menu        



if __name__ == "__main__":
    pygame.init()
    
    screenWidth = 600
    screenHeight = 700
    playArea = min(screenWidth,screenHeight)
    
    hborder = 150                                              #horizontal border must be > (screenWidth - screenHeight)/2 in order for the screen to include the whole grid
    vborder =( screenHeight - screenWidth + 2*hborder )/ 2
    playBorder = min(hborder,vborder)
    gridSize = 6
    letterSize = int((playArea - 2*playBorder)/gridSize)
    
    
    #Initialize the startup menu dimensions
    
    
    firstClick = (0,0)                  #(0,0) represents no click, (1,1) represents the top left cell
    secondClick = (0,0)
    
    stageList = None
    stage = None
    
    pygame.display.set_caption('Sliders')
    screen = pygame.display.set_mode((screenWidth,screenHeight))
    font2 = pygame.font.SysFont('ActionIsShaded',int(letterSize*2))     #Here we initialize our fonts
    font3 = pygame.font.SysFont('ActionIsShaded',30)
    smallfont = pygame.font.SysFont('ActionIsShaded', 30)
    font = pygame.font.Font(os.path.join('fonts','BubbleLetters.ttf'), letterSize)
    menuFont = pygame.font.Font(os.path.join('fonts','BubbleLetters.ttf'), 50)
    saveFont = pygame.font.SysFont('ActionIsShaded',50)
    
    
    
    
    white = (255,255,255)       #Initializing our colors
    black = (0,0,0)
    red = (255,0,0)
    grey = (100,100,100)
    green = (50,205,50)
    
    saveRect = None
    helpRect = None
    saveGameColor = black
    helpColor = black
    
    letterColor = black             
    background = pygame.image.load('background.jpg')
    background = pygame.transform.scale(background, (screenWidth, screenHeight))
    
    
    
    
    
    colors = [[letterColor for x in range(gridSize)] for y in range(gridSize)]       #This list keeps track of what color we want each letter to be    
    
    newGameColor = black    
    newGameText = font.render("New Game", True, newGameColor) 
    newGameRect = newGameText.get_rect()
    newGameRect.centerx = screen.get_rect().centerx
    newGameRect.centery = vborder + 50
    
    loadGameColor = black
    loadGameText = font.render("Load Game", True, loadGameColor)
    loadGameRect = loadGameText.get_rect()
    loadGameRect.centerx = screen.get_rect().centerx
    loadGameRect.centery = newGameRect.centery + 100
    
    saveText = saveFont.render("Save Game", True, black)
    saveRect = saveText.get_rect()
    saveRect.centery = vborder/2
    saveRect.centerx = (screen.get_rect().centerx)
    
    helpText = saveFont.render("Help", True, helpColor)        #Showing the save icon
    helpRect = helpText.get_rect()
    helpRect.centery = vborder/4
    helpRect.centerx = hborder    
    
    hoverColor = red
    
    
    helpMessage = ['Instructions: Arrange the letters to make a word!',
                   'To slide a row or column, click on two letters in',
                   'the row/column you want to move.  Then click ',  
                   'anywhere to make the slide.  To unselect letters, ',  
                   'right click.  The red number shows your remaining ',  
                   'slides, and the green number shows the slides ',  
                   'you’ve made, which is your score.  To resume the ',  
                   'game, click anywhere.'  
                   ]
        
    
    
    startMenu(newGameColor,loadGameColor, hoverColor, newGameRect, loadGameRect)            #Run the start menu
    runGame()                                                                               #Run the Game
