# Write your code here
import random

print('H A N G M A N')
word_bank = ['python', 'java', 'kotlin', 'javascript']
hidden = random.choice(word_bank)
hyphened = ['-' for _ in range(len(hidden))]
trials = 8
guessed = ''.join(hyphened)
found = False
incword = ""
op = True
menu = input('Type "play" to play the game, "exit" to quit: ')
if menu == 'play':
    while trials > 0:
        print()
        print(guessed)
        letter = input('Input a letter: ')
        if letter not in hyphened and letter in hidden:
            for index, char in enumerate(hidden):
                if char == letter:
                    hyphened[index] = letter

            guessed = ''.join(hyphened)
            if guessed == hidden:
                found = True
                break

            continue
        #if letter not in hyphened and letter not in incword:
            #trials -= 1


        cap = letter.isupper()
        #if letter != 1:
            #letter = letter.islower()
        sym = letter.isalpha()
        aa = len(letter)


        if letter != hidden:
            if letter == '-':
                print("Please enter a lowercase English letter")
            elif letter in hyphened :
                print("You've already guessed this letter")
            elif aa != 1:
                print("You should input a single letter")
            elif cap == True:
                print("Please enter a lowercase English letter")
            elif sym == False:
                print("Please enter a lowercase English letter")
            elif letter in incword :
                print("You've already guessed this letter")
            else:
                print("That letter doesn't appear in the word")
                incword += letter
                trials -= 1





    print(f'You guessed the word {hidden}!\nYou survived!' if found else 'You lost!')

