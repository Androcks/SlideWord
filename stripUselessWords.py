def stripUselessWords(inF, outF):
    '''DIS GUN BE FOR REMOVING ALL WORDS THAT WE DON'T NEED
    FROM OUR LIST OF ALL POSSIBLE WORDS.  WORDS DAT ARE LESS
    THAN 3 LETTERS AND MORE THAN 6 DON'T END UP IN THE LIST
    WE USE FOR GAME.'''
    validWords = 0
    with open(outF, 'a+') as gameWords :
        
        ## debug string print("opened output file")
        with open(inF, 'r') as demWords :
            ##print("opened input file")
            for eachLine in demWords :
                ##print("reading line from input file")
                eachLine = eachLine.strip(" ")  ##Some stupid stuff left in front of the words where I got the wordlist from
                eachLine = eachLine.strip("\n")
                ##print(eachLine)
                ##print(eachLine)
                ##eachLine = eachLine[:-1]
                if (len(eachLine) >= 3) and (len(eachLine) <= 6):
                    ##get rid of all this symbol garbage
                    eachLine = eachLine.strip('~!@#$%^&*()_+|}{":<>?`1234567890-=[]\'\\/.,')
                    eachLine = eachLine.upper()
                    gameWords.write(eachLine + "\n")
                    validWords +=1
                    print (eachLine)
                    print("add word: " + eachLine)
            print("SHIT'S DONE.  Valid words: ", validWords)
            ##Using the list of 5000 most common words, should give us ~2737 valid words that are from 3 to 6 letters in length

def convertDictCase(dictFile) :

    while (cycleComplete == False) :
        caseToChangeTo = input(print("Would you like 'U'PPERCASE or 'l'owercase?"))
        with open(dictFile, 'rw') as wordsToFix:
            if caseToChangeTo == 'u' or caseToChangeTo == 'U' :
                for eachLine in wordsToFix :
                    dictFile.write(wordsToFix.upper())
                
            


stripUselessWords("corncob_caps.txt", 'truncListWords.txt')
