import StageClass
import WordFinder
import graphicWordFinder
import Save


print()
print('--SlideWord--')
select = None
while select == None:
    select = input('Start a new Game (n)' + '\n' + 'Continue from last (c)' + '\n')
    if select == 'n':
        size = input("Select Grid Size: ")
        stage = StageClass.Stage(str(size))
        print()
        stage.letFill()
        print()
    elif select == 'c':
        stage = Save.load()
    else:
        print("Please print out a valid selection!" + '\n' + '(Look in the brackets for what to put in.)')
        select = None

        
while WordFinder.wordFinder(stage, False) == True:#Constantly checks the generated and loaded grids to
    #so as to avoid initial generation making words, or cheaters.
    WordFinder.wordFinder(stage, False)
#Checks to see if the loaded or randomly made grid already had words.
#We're not letting them off easy.
stage.gridDisplay()
print("To save and quit, input 'quit' at any time!")
gameStop = None
while gameStop == None:
    while stage.movesRemaining > 0: 
        print('Select a cell')
        column = input('column: ')
        if column == 'quit':
            break
        row = input('row: ')
        if row == 'quit':
            break
        orient = input('which direction (u,r,l, or d): ')
        if orient == 'quit':
            break
        move = input('spaces to move: ')
        if move == 'quit':
            break
        stage.slide(int(row), int(column), orient, int(move))
        

        while WordFinder.wordFinder(stage) == True:
            #stage.gridDisplay()
            WordFinder.wordFinder(stage, False)
        
        #insert deletion of found words and addition to slide moves here
        stage.gridDisplay()
        #insert insertion of new letters based on semi random system,
    if stage.movesRemaining != 0:
        select = input("Do you wanna save? (y/n)")
        if select == 'y':
            Save.save(stage)
            print("Game Saved!" + "\n" + "Come again to finish your game!")
    gameStop = 0
else:
    print("Game Over!")
