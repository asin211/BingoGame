import random    #module for random numbers
import sys       #module for quitting the game

print('\n********WELCOME TO BINGO************\n'
      'User Instruction: Please type in ONLY RANDOM NUMBERS between 1 and 80\n'
      'When all the numbers are matched, YOU WIN')

playerPrompt = str(input("Select any key to continue or N to exit: "))
if playerPrompt == 'n' or playerPrompt == 'N':
    sys.exit("See you next time")
else:
    pass
bingoCardNumbers = random.sample(range(1, 80), 10)
correctNumbers = []
while correctNumbers != bingoCardNumbers:
    # print(f"bingo numbers: {bingoCardNumbers}")   #for testing
    # print(f"player numbers: {correctNumbers}")    #for testing
    try:
        userNumbers = int(input('Enter your number: '))

        if userNumbers in correctNumbers:
            print('Number already been checked')
        elif userNumbers > 80:
            print('Number outside specified range, only enter numbers between 1 - 80')
        elif userNumbers in bingoCardNumbers:
            correctNumbers.append(userNumbers)
            correctNumbers.sort()
            bingoCardNumbers.sort()
            print('Correct Number')
            if bingoCardNumbers == correctNumbers:
                print('BINGO You Are WINNER')
        else:
            print('Not a match, Try Again')
    except:
        print('Please enter integer numbers only')
