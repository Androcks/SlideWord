import random

possibleLetters = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', \
                   'B', 'B', 'C', 'C', 'D', 'D', 'D', 'D', 'E', \
                   'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', \
                   'E', 'E', \
                   'F', 'F', 'G', 'G', 'G', 'H', 'H', 'I', 'I', \
                   'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', \
                   'L', 'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', \
                   'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', \
                   'O', 'O', 'P', 'P', 'Q', 'R', 'R', 'R', 'R', \
                   'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', \
                   'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V', 'V', \
                   'W', 'W', 'X', 'Y', 'Y', 'Z']
def grabALetter() :
    winnerWinner = random.randint(0,97)
    #print(winnerWinner)
    blah = possibleLetters[winnerWinner]
    return blah


#TESTSTUFF = []
#for x in range(9800) :
    #dahNum = grabALetter()
    #TESTSTUFF.append(dahNum)
    ##print(TESTSTUFF)

#newDict = {}
#for eachEntry in TESTSTUFF :
    #if eachEntry in newDict :
        #newDict[eachEntry] += 1
    #else :
        #newDict[eachEntry] = 1

#numberPlace = 0
#for eachKey in sorted(newDict) :
    #numberPlace += 1
    #print(str(numberPlace) + '.   ' + eachKey + '   '  + str((newDict[eachKey])/100))
