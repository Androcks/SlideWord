#RandomGenerator
import random
        
def randLetterGen():
    decider = random.random()# random number between 0 and 1 is chosen

    if decider <= 0.12: # 12% chance of A
        return 'A'

    if decider > 0.12 and decider <= 0.21: # 9% chance of D
        return 'D'

    if decider > 0.21 and decider  <= 0.30:
        return 'I'

    if decider > 0.30 and decider <= 0.38:
        return 'O'

    if decider > 0.38 and decider <= 0.44:
        return 'N'

    if decider > 0.44 and decider <= 0.50:
        return 'R'

    if decider > 0.50 and decider <= 0.56:
        return 'T'

    if decider > 0.56 and decider <= 0.60:
        return 'L'

    if decider > 0.60 and decider <= 0.64:
        return 'S'

    if decider > 0.64 and decider <= 0.68:
        return 'U'

    if decider > 0.68 and decider <= 0.72:
        return 'D'

    if decider > 0.72 and decider <= 0.75:
        return 'G'

    if decider > 0.75 and decider <= 0.77:
        return 'B'

    if decider > 0.77 and decider <= 0.79:
        return 'C'

    if decider > 0.79 and decider <= 0.81:
        return 'M'

    if decider > 0.81 and decider <= 0.83:
        return 'P'

    if decider > 0.83 and decider <= 0.85:
        return 'F'

    if decider > 0.85 and decider <= 0.87:
        return 'H'

    if decider > 0.87 and decider <= 0.89:
        return 'V'

    if decider > 0.89 and decider <= 0.91:
        return 'W'

    if decider > 0.91 and decider <= 0.93:
        return 'Y'

    if decider > 0.94:
        return 'K'

    if decider == 0.95:
        return 'J'

    if decider == 0.96:
        return 'X'

    if decider == 0.97:
        return 'Q'

    if decider == 0.98:
        return 'Z'

    if decider >= 0.99:
        randLetterGen()
#tests
for letter in range(30):
    print(randLetterGen())

z = True
while z == True:
    print('TRYING')
    if randLetterGen() == 'K':
        print('Z found')
        z == False
