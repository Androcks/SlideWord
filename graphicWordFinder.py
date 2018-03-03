#Andrew Somerville
import StageClass
import wordVerification
from slidegraphics import showWord
def graphicWordFinder(stage, score = True):
    'Takes a Stage object and goes through the 2 dimensional grid \
    horizontally and vertically and compares strings of size \
    gridSize to 3 to a dictionary to confirm if they are a word.\
    If score is True then it will distribute more slides for the player'

    foundWord = False #value used to state that a word(s) has been found.
    #After the words are found, the starting coordinates of the word are stored in lists.
    #The lists are used to delete the letters after they have all been found.
    wordsX = []
    wordsY = []
    #XAXIS
    xIndex = 0
    for xAxis in stage.grid:#for every horizontal line in the grid
        #for every possible length of a word from the max (grid size) to 3
        for wordLength in reversed(range(3, stage.gridSize + 1)):
           # print(wordLength)
            #for every possible length, from max length to 3 in a line.
            index = 0 # index is reset at the beginning of the word gen.
            checkWord = [] # initial empty list for strings
            #for every letter in range of the start of the word (index) to the
            #end of its length(wordLength)

            while index < (stage.gridSize + 1 - wordLength):
                # While the index is less than the gridSize + 1 - the length of word
                #This loop initiates the word making loop repeatedly
                #until the starting index is too large to contain the word of the length
                #needed.

                for letter in range (index, wordLength + index):# makes the actual word
                    checkWord.append(xAxis[letter])
                    #adds letter from xAxis to checkWord
                    #print(checkWord)
                    if len(checkWord)  == wordLength:
                        finalWord = ''.join(checkWord)#forms individual string from string array
                        result = wordVerification.checkForWord(finalWord)
                        if result == True and len(wordsX)  == 0:
                            foundWord = True #As a word has been found, the foundWord value goes true.
                            if score == True:
                                stage.movesRemaining += (len(finalWord) - 2)
                                showWord(finalWord,stage)
                                
                                
                               
                               
                            #more slides are given based off the word Length
                            wordsX.append((xIndex,index, wordLength))#places the x y coord and word length info of the word into the wordsx list

                        elif result == True and xIndex != wordsX[-1][0]\
                        and wordsX[-1][1] + wordLength > index:
                            if score == True:
                                stage.movesRemaining += (len(finalWord) - 2)
                                showWord(finalWord,stage)
                                
                                
                               
                            wordsX.append((xIndex,index, wordLength))#places the x y coord and word length info of the word into the wordsx list
                            #Stores word coords and length to be used later in deletion

                    
                        elif ((index) + wordLength) >= stage.gridSize - 2:
                            #print('SHITTING FUCK') 
                            break

                # end of letter loop
                index += 1 # shifts the beginning index (starting position of word) 1.
                checkWord = [] # resets the made word to an empty list
            #if result == True and ((index - 1) + wordLength >= stage.gridSize - 2):
                #print('SHITTING FUCK') 
                #break
            #---- end of while
        xIndex += 1#increases the xIndex by 1 to track the index of the current xAxis
        #end of wordLength loop
        #increases the xIndex by 1 to track the index of the current xAxis

    #YAXIS
    
    #print("-------------------------------" + "YAXIS" +"-------------------------------" )
    for yAxis in range(stage.gridSize): #for every column in the grid
        for wordLength in reversed(range(3, stage.gridSize + 1)):
            index = 0
            checkWord = []
            #print(wordLength)

            while index < (stage.gridSize + 1 - wordLength): #checkword maker

                for letter in range (index, wordLength + index):
                    checkWord.append(stage.grid[letter][yAxis])
                    #print(checkWord)

                    if len(checkWord)  == wordLength:
                        finalWord = ''.join(checkWord)
                        result = wordVerification.checkForWord(finalWord)

                        if result == True and len(wordsY)  == 0:
                            foundWord = True 
                            if score == True:
                                stage.movesRemaining += (len(finalWord) - 2)
                                showWord(finalWord,stage)
                                
                                
                               
                            #more slides are given based off the word Length
                            wordsY.append((yAxis,index, wordLength))
                            

                        elif result == True and yAxis != wordsY[-1][0] and wordsY[-1][1] + wordLength > index:
                            if score == True:
                                stage.movesRemaining += (len(finalWord) - 2)
                                showWord(finalWord,stage)
                                
                                
                               
                            wordsY.append((yAxis,index, wordLength))
                            

                index += 1
                #print("index added")
                checkWord = []
            if result == True and ((index) + wordLength >= stage.gridSize - 2):#DOESNT WORK
                pointlessValue = None#DOESNT WORK
                break #if the last letter of a verified word is two letters away from the end,
            #no more words could possibly be made (due to a minimum of 3 letter words)
            #so it stops looking, and breaks out of the wordlength for loop. THIS WOULD BE IDEAL
            #IF IT ACTUALLY WORKED. 
            
    
    
    
    
    
     
    for xcoord in range(len(wordsX)):        
        stage.letDel(wordsX[xcoord][0], wordsX[xcoord][1], wordsX[xcoord][2], False)
        
    
    for ycoord in range(len(wordsY)):       
        stage.letDel(wordsY[ycoord][1], wordsY[ycoord][0], wordsY[ycoord][2], True)
       

    if foundWord == True: #If a word has been found, it will return a true value.
        stage.letFill()    
        return True
    else:
        False
            
            

        
        
                  