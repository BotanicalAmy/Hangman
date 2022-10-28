from replit import clear
from hangman_art import hangman_word

print("Welcome to hangman!")
print (hangman_word)

import random
from hangman_words import word_list_full
from hangman_words_boy import word_list_boy

list_selection = input("Do you want a random word, or do you want to write your own? \nType \"random\" or \"custom\": ")
if list_selection == "boy":
    word_list = word_list_boy
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
elif list_selection == "custom":
    chosen_word = input("Type a word for the other player to guess: ")
    word_length = len(chosen_word)
    clear()
else: 
    word_list = word_list_full
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

#print empty blanks for word guess
#count number of letters in the random word
display = "_" * word_length
blanks = "_"
display_list = list(display)
 #Join all the elements in the list and turn it into a String.
print(f"{' '.join(display_list)}")

#definitions for empty blanks, hangman lives & accidental second guessing
blanks == "_"
hangman_lives = 6
guess_list = []
playing = True

#Get ASCI art
from hangman_art import hangman, hangman_5, hangman_4, hangman_3, hangman_2, hangman_1, hangman_0


#Check guess and keep score
while blanks in display_list and hangman_lives > 0:
    guess = input("\n Guess a letter: \n").lower() 
    #Use the clear() function imported from replit to clear the output between guesses.
    clear()
    #print updated hangman art based on score (lives left)
    if hangman_lives == 6:
        print(hangman)
    if hangman_lives == 5:
        print(hangman_5)
    if hangman_lives == 4:
        print(hangman_4)
    if hangman_lives == 3:
        print(hangman_3)
    if hangman_lives == 2:
        print(hangman_2)
    if hangman_lives == 1:
        print(hangman_1)
    for position in range(word_length):
        char = chosen_word[position]
        if char == guess:
            display_list[position] = char
            print(f"{' '.join(display_list)}\n")
    if guess not in chosen_word:
        hangman_lives -= 1
        print(f"{' '.join(display_list)}\n")
        guess_list.append(guess)
        print(f"You have incorrectly guessed these letters: {guess_list}")
    
#If there are no lives left
if hangman_lives == 0:
    print("You Lose") 
    print(hangman_0)
    print(f"The word was {chosen_word}")
#When the word is guessed and you did not run out of lives
else:
    print("You Win!")
    print(hangman_word)