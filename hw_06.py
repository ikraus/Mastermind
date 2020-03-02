# ----------------------------------------------------------
#                           HW 06: MasterMind
# ----------------------------------------------------------
# Please answer these questions after having completed the
# entire assignment.
# ----------------------------------------------------------
# Name:Ruth Kissel 
#7
# Hours spent in total:6
#
# Collaborators (if any): Isabel Kraus
#
# ----------------------------------------------------------

# Write your functions below

import random #importing random module


def hidden_code():
    '''takes no parameters--> returns a list of the hidden code'''

    print("Welcome to my MasterMind game, get ready to be tricked, press enter to begin!")
    input()

    valid = False
    while not valid: #asking for input, until input is valid
        try: #if invalid input, raise exception
            L = int(input("What is the length of the code: "))
            C = int(input("How many colors: "))
            valid = True
        except ValueError: #raising exception
            print("Invalid input, make sure you're inputing integers")

    colors = ['r','o','y','g','b','i','v'] #list of colors of the random
    code = []

    # looping through number of colors user wants to use
    for i in range(C): 
        new_colors = colors[:i+1] #slicing the # of colors they want to use from list of colors
    #print(new_colors)

    # looping through the length the user chooses to assign color values
    for color in range(L): 
        random_c = random.choice(new_colors) #randomly selecting a color from the new_colors list
        code += [random_c] #creating the hidden code
            
    print("You chose", C, "colors, these are the colors available:", new_colors) 

    print(code)
    return code
    
    
# can tell them # of colors they're choosing from    

def feedback(guess,code):
    '''Takes 2 parameters the user's guess as a list and the code, also a list -->
       returns feedback for the user'''

    black_peg = 0 #to keep track of how many white and black pegs
    white_peg = 0
    clone_code = code[:] #cloning the lists so we don't modify the original list
    clone_guess = guess[:]

    # looping through the list of guesses 
    for i in range(len(clone_guess)):
        if clone_guess[i] == clone_code[i]:
            black_peg += 1
            clone_guess[i] = 'k' #changing it a letter that isn't a color option
            clone_code[i] = 'k'
        for j in range(len(clone_code)): #looping through code
            checked = 0 #keeping track of what has been checked
            for item in range(len(clone_guess)): #looping the guess
                if clone_code[j] == clone_guess[i] and checked == 0 and clone_guess[item] != 'k' and clone_code[j] != 'k': #if the code = the guess in that position, then it's correct
                    white_peg += 1
                    checked += 1 #if white peg but should be black

    # return feedback to user
    if black_peg == len(code): #if # of black pegs = length of code, they won
        print("Congrats, you won the game!!")
        return True
    else: #black and white peg counts
        print()
        pegs = print("You got", black_peg, "black pegs and", white_peg,"white pegs")
        print()
        return pegs
        
        
def play_again():
    '''takes no parameters, in order to restart the game or quit'''

    play = False
    # to restart game if user wants to 
    while not play:
        restart = input("Do you want to play my tricky game again? (y)es or (n)o: ")
        lower_restart = restart.lower() #making it case insensitive
        if lower_restart == 'y': #if yes
            main()
            play = True #getting out of loop
        elif lower_restart == 'n': #if no
            print()
            over = print("Thanks for playing! Come play again soon!")
            return over
        else: #put in wrong input
            print("Invalid input, try again and enter either (y)es or (n)o")
            
    
def main():
    '''no parameters, allowing the game to fully function'''
    # explain rules of code
    # providing instructions for the user
    print("""Your goal is to guess the hidden code, you have 10 guesses
to correctly guess the code and end the game. To win you must guess the correct
colors in the correct order.""")
    print()
    print("""To guess the code input the letter of the color, as
provided to you in the below statement.""")
    print()
    print("""The feedback provided will a black peg, white peg, or no peg.
A black peg means the color appears in the hidden code in the guessed position.
A white peg means the color appears in the hidden code, but not in the position
guessed by the user. No peg means the color does not appear in the hidden code""")
    print()

    code = hidden_code() #getting the code
    print()
    print("You have a total of 10 guesses to guess the correct code, good luck!")
    print()
    num_guesses = 0 #counter of their guesses
    
    # looping through the number of guesses, 10
    for i in range(10):
        guesses = []
        j = 0
        done = False
        while j < len(code):
            guess = input("Guess the code, if you want to quit type 'done': ")
            guess = guess.lower() #making it case insensitive
            if guess in ['r','o','y','g','b','i','v']: #if guess is in list of colots
                guesses += [guess]
                j += 1 #increment j to keep looping
            elif guess == 'done': #if the user types done to end game
                done = True
                break #break out of loop
            else:
                print("Invaid input, please try again.") #guess is not a valid input
        num_guesses += 1 #keeping track of how many guesses user has made

        # have the user's guess
        if done != True: #not giving up, so get feedback
            over = feedback(guesses, code)
            if over != True: #if they don't win, tell them how many guesses they have left
                print("You have", 10 - num_guesses, "guesses left")  #10 - number of guesses they've made so far
                print()
            elif over == True: # if they win
                print()
                print("You won in", num_guesses, "guesses!")
                play_again() #asking user if they want to play again
                break #get out of for loop

        if done == True: #is user wants to give up
            print()
            print("See my game was tricky! Game over, you lose!")
            print()
            print("The correct solution was", code)
            print()
            play_again()
            break #break out of loop to stop asking

    if num_guesses == 10: #checking if user's guesses = 10 their max guesses
        print()
        print("Shoot you used up all of your guesses!")
        print()
        play_again()
        

            
        

  
    
    
    
    
    

    
    
