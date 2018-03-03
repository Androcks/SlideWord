import enchant

##Use our custom word list
wordList = enchant.request_pwl_dict("truncListWords.txt")

##Takes our string from the stage and checks it

def checkForWord(playerString) :
    return wordList.check(playerString)
