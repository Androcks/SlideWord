import linecache
import wordVerification
import randomTest
import random

def randomWordVerificationTest(numberOfIterations) :

    '''testing suite for wordVerification'''
    with open ("truncListWords.txt", "r") as wordList :
        n = numberOfIterations
        
        numberOfWordsInList = 0
        totalRunSoFar = 0
        totalRandomFromListSuccess = 0
        totalRandomFromListFailure = 0
        totalRandomFromListRuns = 0
        totalRandomLettersSuccess = 0
        totalRandomLettersFailures = 0
        totalRandomLettersRuns = 0
        totalLengthWordsChecked = {3 : 0, 4 : 0, 5 : 0, 6 : 0}
        allRandomLettersThatMadeWords = []
        testWord = ""


        
        ##determine how many words in list, for randomly picking one.
        for eachLine in wordList :
            numberOfWordsInList += 1
        print(numberOfWordsInList)
        while (totalRunSoFar <= n) :
            testToPerform = random.randint(0, 1)
            if testToPerform == 0 :
                ## Pull random word from list of possible words, run it through checker
                testWordRNG = random.randint(1, numberOfWordsInList)
                print(testWordRNG)
                testWord = linecache.getline("truncListWords.txt", testWordRNG)
                print(testWord)
                testWord = testWord.replace('\n', '')
                print(testWord)
                if wordVerification.checkForWord(testWord) == True :
                    totalRandomFromListSuccess += 1
                else :
                    totalRandomFromListFailure += 1
                totalRandomFromListRuns += 1

                ##This case we pick random letters and see if it's in the list
            elif testToPerform == 1 :
                wordLength = random.randint(3, 6)
                rngTestWord = ''
                
                for x in range(wordLength) :
                    ##Grabs a random letter and appends it to the string we're building
                    rngTestWord += randomTest.grabALetter()
                    print(rngTestWord)
                print(rngTestWord)
                if wordVerification.checkForWord(rngTestWord) == True :
                    totalRandomLettersSuccess += 1
                    allRandomLettersThatMadeWords.append(rngTestWord)
                else :
                    totalRandomLettersFailures += 1
                totalRandomLettersRuns += 1
                totalLengthWordsChecked[len(rngTestWord)] += int(1)
            totalRunSoFar += 1

        
        print('totalRandomFromListSuccess' , totalRandomFromListSuccess)
        print('totalRandomFromListFailure' , totalRandomFromListFailure)
        print('totalRandomFromListRuns' , totalRandomFromListRuns)
        print('totalRandomLettersSuccess' , totalRandomLettersSuccess)
        print('totalRandomLettersFailures' , totalRandomLettersFailures)
        print('totalRandomLettersRuns' , totalRandomLettersRuns)
        print('totalLengthWordsChecked' , totalLengthWordsChecked)
        print('allRandomLettersThatMadeWords' , allRandomLettersThatMadeWords)
                        
                
