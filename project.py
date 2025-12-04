# Summary: console-based game program offering two games:
# "Hangman" and "Trivia." In the Hangman game, a random word is chosen, and
# the player has three attempts to guess it. In the Trivia game, a random question
# is asked, and the player has two attempts to answer. After each game, the program
# prompts the user to continue playing or return to the main menu. User scores, including
# correct and incorrect guesses, are recorded in a file if the user chooses to save.
# The program features a menu screen and a main function controlling the game flow through
# a loop. Overall, it provides a simple text-based gaming experience with options for
# playing different games and saving scores.

import random
def word_guess():
    #this list stores all the words for the game
    list_of_words = ['verdict', 'stimulation', 'temperature', 'champagne', 'legislation', 'ambition', 'north', 'qualification', 'accompany', 'projection', 'negligence', 'instrument']
    continue_operation = True
    correct_score=0         #these two variables will keep track of all of the users correct and incorrect responses
    incorrect_score=0
    while continue_operation:       # uses the same while loop logic as in the main function
        pick = random.randint(0, len(list_of_words))  #picks a random word from the list
        to_list = list(list_of_words[pick])              #converts the random word to a list so it can be steped throuth later
        attempts=3      # this variable stores the amount of attempts
        print('Try to guess the word, you have 3 attempts')
        for x in range(len(to_list)):           #this for loop is responsiable for obscuring the word chosen with underscores
            l_ = random.randint(0, 1)   #this picks a random number between 0 and 1
            if l_ == 0:                #if the random number is 0 it will display the letter in that position of the list
                print(to_list[x], end='')
            else:           #anything other than that will result in diplaying an underscore instead of the appropriate letter
                print('_', end='')
        for y in range(attempts):       #this loop continues for as long as there still attemps or the users answers correctly
            user_answer = input(' Type in what you believe to be the word: ')
            if user_answer == list_of_words[pick]:          # if the user gets it right it adds one to correct_score and breaks the loop
                print('Nice job, you got the it right')
                correct_score=correct_score+1
                break
            else:           #if incorrect the user will be prompted to try again and subtract one from attempts and add on to incorrect_score
                attempts=attempts-1
                print('Sorry, your answer is incorrect, ',attempts ,' attempts remaining')
                incorrect_score = incorrect_score + 1
            if attempts==0:     #if the user runs out of attempts the program will display the right answer
                print('The correct answer is: ', list_of_words[pick])
        print('|||')
        print('Go back to main menu type in N, to play again type in anything else')
        user_check = input('Your input: ')              #this is to see if the users wants to continue or not
        continue_operation = end_sequence(user_check)   #calls function using the user input as paramater
        if continue_operation:          # this is so if the user wants to continue the program won't ask if they want to save
            continue
        print('|||')
        print('To save your stats type S, or type anything else to continue')
        seeif=input('type here: ')                  # ask the user if they want to save
        if seeif == 's' or seeif == 'S':
            store_score(correct_score, incorrect_score)     #if so it call the store_score function

def trivia():
    #create a dictionary  with question and answers
    Dictionary_of_trivia={'Originally, Amazon only sold what kind of product?':'books' , 'In 2009, what became the first Morse code character to be added since WWII?':'@', 'Who was the first woman to win a Nobel Prize?':'Marie Curie', 'What does SPF in sunscreen stand for?':'Sun Protection Factor', 'In what year was the internet opened to the public?':'1993',"What is the capital of France?": "Paris"}
    continue_operation = True
    correct_score = 0
    incorrect_score = 0

    while continue_operation:       #same logic as before
        question = random.choice(list(Dictionary_of_trivia.keys()))     #picks a random question
        attempts = 2
        print(question)     #displays question
        for y in range(attempts):                                               #same for loop logic as before seen in word_guess function
            user_answer = input(' Type in what you believe to be the answer: ')
            if user_answer == Dictionary_of_trivia[question]:
                print('Nice job, you got the it right')
                correct_score=correct_score+1
                break
            else:
                attempts = attempts - 1
                print('Sorry, your answer is incorrect, ', attempts, ' attempts remaining')
                incorrect_score=incorrect_score+1
        print('|||')                                                                    #same logic as before
        print('Go back to main menu type in N, to play again type in anything else')
        user_check = input('Your input: ')
        continue_operation = end_sequence(user_check)
        if continue_operation:
            continue
        print('|||')
        print('To save your stats type S, or type anything else to continue')
        seeif = input('type here: ')
        if seeif == 's' or seeif == 'S':
            store_score(correct_score, incorrect_score)


def end_sequence(user_check):
    if user_check == 'n' or user_check == 'N':      # if the user inputs n the function will return False and end the while loop from the previous function
        print('Program ended')
        return False
    else:
        return True     # anything else other than n the return will be true

def store_score(correct, incorrect):
    total=correct+incorrect             #calculate total
    percent=(correct / total) * 100     #calculate percentage
    print('Number correct: ',correct)           #the infomation being displayed here is what will be stored in the file
    print('Number incorrect: ', incorrect)
    print('Total: ', total)
    print('Percentage correct:', percent)

    new=open("new_record.txt",'w')                         #create a new file and stores the info
    new.write('Number correct: '+str(correct)+'\n')
    new.write('Number incorrect: '+ str(incorrect)+'\n')
    new.write('Total: '+ str(total)+'\n')
    new.write('Percentage correct:'+ str(percent)+'\n')
    new.close()


def menu_screen():          #this function is to print the menu screen
    print('Type a number corresponding to the game you want to play, or type N to stop')
    print('1) Hang man')
    print('2) Trivia')
def main():
    continue_operation = True       #this is to start the loop
    while continue_operation:       #this loop will concinue for as long as the continue_operation variable is true
        menu_screen()               #call function to print the menu screen
        user_check = input('Your input: ')      #take user input
        if user_check=='1':             #in this series of if and esif statments we check what the user wants to do
            word_guess()
        elif user_check=='2':
            trivia()
        elif user_check == 'n' or user_check == 'N':
            print('Program ended')
            continue_operation = False      #this ends the loop and the program

main()

#ideas have so that the user can make a file of their progress and acceracy