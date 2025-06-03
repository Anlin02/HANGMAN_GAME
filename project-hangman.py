HANGMANPICS = [''' 
  +---+ 
  |   | 
  O   | 
 /|\  | 
 / \  | 
      | 
=========''', ''' 
  +---+ 
  |   | 
  O   | 
 /|\  | 
 /    | 
      | 
=========''', ''' 
  +---+ 
  |   | 
  O   | 
 /|\  | 
      | 
      | 
=========''', ''' 
  +---+ 
  |   | 
  O   | 
 /|   | 
      | 
      | 
=========''', ''' 
  +---+ 
  |   | 
  O   | 
  |   | 
      | 
      | 
=========''', ''' 
  +---+ 
  |   | 
  O   | 
      | 
      | 
      | 
=========''', ''' 
  +---+ 
  |   | 
      | 
      | 
      | 
| 
========= ''']
# step 1:choosing a random word
from operator import truediv

wordList=["hangman","python","pycharm","world","hello"]
import random
chosenword=random.choice(wordList)
print(chosenword)

# step 2:display blanks equal to word length
displayblanks=""
wordlength=len(chosenword)
for a in range(wordlength):
    displayblanks +="_"
print(displayblanks)

# step 3:initialising game variables
noofchances=6
gameactive=True

# step 5:making local memory
correctletters=[]

# step 4:Game Loop
while gameactive:
    userguess=input("enter your alphabet: ").lower()
    display=""

    for a in chosenword:
        if a==userguess:
            display+=a
            correctletters.append(a)
        elif a in correctletters:
            display+=a
        else:
            display+="_"


# losing conditions
    if userguess not in chosenword:
        noofchances-=1
        if noofchances==0:
             gameactive=False
             print("u lost")

    if "_" not in display:
        print("u won")
        gameactive=False
    print(HANGMANPICS[noofchances])
    print(display)


