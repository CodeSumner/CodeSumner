#https://codeinplace.stanford.edu/cip3/share/UzQqf5ZiONwPOQpLCdN1

"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Max number of guesses per game


def play_game(secret_word):

    INITIAL_GUESSES = 8 

    j = 0 # mark the index of repeated letter in 'secret_word_letters' list.

    guess_letter_index = 0 # the index of input 'guess_letter' in 'secret_word_letters' list.
    
    dash_list = [] # list of dash '-' .
    
    secret_word_letters = [] # list of secret word letters.
   
    # create list of '-' and secret word letters.
    for i in range(len(secret_word)):
        dash_list.append('-')
        secret_word_letters.append(secret_word[i])
        
    dash_word = ''.join(map(str, dash_list)) # convert das_list to string.

    
    
    while INITIAL_GUESSES != 0:
        
        
        print("The word now looks like this:"+ dash_word
            + "\n" + "You have " + str(INITIAL_GUESSES) + " guesses left")
            
        input_letter = input("Type a single letter here, then press enter: ")
        guess_letter = input_letter.upper()
    
        if guess_letter == '': # type '' to break.
            break

        # the user input one character.
        if len(guess_letter) == 1: 
            # the user input a letter that is in the secret word.
            if guess_letter in secret_word_letters:
                #  replace the '-' in dash list to the correct input letter, they both have the same index of position.
                if guess_letter not in dash_list: 
                    guess_letter_index = secret_word_letters.index(str(guess_letter))
                    dash_list[guess_letter_index] = guess_letter
                    dash_word = ''.join(map(str, dash_list))
                    print("That guess is correct.")

                # if the correct input letter is repeated in secret word, the replacement will repeat according to their index
                else:
                    # create a index list of a repeated letter to record the different postions in secret word.
                    guess_letter_indices = [i for i, x in enumerate(secret_word_letters) if x == guess_letter]
                    if len(guess_letter_indices) > j + 1:
                        j += 1 # the index is incremental for loops, the first index is 1.

                        # prevent Error of the index out of range.
                        if j > len(guess_letter_indices):
                            j = len(guess_letter_indices) - 1

                        dash_list[guess_letter_indices[j]] = guess_letter 
                        dash_word = ''.join(map(str, dash_list))
                        print("That guess is correct.")

                        # sometimes there are two or three different words repeated several times like 'MISSISSIPPI', 
                        # need to reset the j to 0 for new loop
                        if j == len(guess_letter_indices) - 1:
                            j = 0

                    # when the input letter is not repeated, do nothing.
                    else:
                        print("That guess is correct.")
                         
                
                # after all the '-' are replaced, user wins the game.
                if dash_word == secret_word:
                        print("Congratulations, the word is: " + dash_word)
                        return
                
            # the user input a letter that is not in the secret word.   
            else:
                INITIAL_GUESSES -= 1
                print("There are no " + guess_letter + "'s in the word")
        
        # the user input more than one characters.
        if len(guess_letter) > 1:
            print('Please type a single letter!')

    # when the times of INITIAL_GUESSES is runing out, check if all the '-' are replaced.             
    if "-" not in dash_list:       
        print("Congratulations, the word is: " + dash_word)
    else:
        print("Sorry, you lost. The secret word was:", secret_word)
        

def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    
    LEXICON_FILE = "Lexicon.txt" 
    file_list = []
    # read file to creat a words list.
    with open(LEXICON_FILE) as f:
            for line in f:
                line = line.strip()
                file_list.append(line)
    
    word = random.choice(file_list)
    return word
    """
    if index == 0:
        return 'ABACAS'
    elif index == 1:
        return 'ABBESSES'
    else:
        return 'MISSISSIPPI'
    """
    
    


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()