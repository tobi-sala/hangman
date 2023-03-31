import time
from tkinter import *
from tkinter import messagebox
import random, time
from string import ascii_uppercase
#create display window
window = Tk()
window.title("Hangman")
#create a list to enlarge scope of game
word_list = ["RUSSIA", "ARGENTINA", "MEXICO", "COLOMBIA", "GERMANY", "KAZAKISTAN",
             "HUNGARY", "TURKEY", "FINLAND", "INDIA", "CHINA" "SWEEDEN", "MONGOLIA",
             "MOROCCO", "NORWAY", "CHILE", "IRELAND", "ICELAND", "CROATIA"," SPAIN",
             "NIGERIA", "JAPAN", "GHANA", "LIBERIA", "LIBYA", "ALGERIA", "BRAZIL"] 
#photos to help make the game more interesting
photos = [PhotoImage(file="hang0.png"), PhotoImage(file="hang1.png"), PhotoImage(file="hang2.png"), PhotoImage(file="hang3.png"),
        PhotoImage(file="hang4.png"), PhotoImage(file="hang5.png"),PhotoImage(file="hang6.png"), PhotoImage(file="hang7.png"),
        PhotoImage(file="hang8.png"), PhotoImage(file="hang9.png"), PhotoImage(file="hang10.png"), PhotoImage(file="hang11.png")]
#define how a game starts and continues
def newGame():
    #create the global variables for each function to be able to inherit
    global the_word_withSpace
    global numberOfGuesses
    #initiate the number of guesses
    numberOfGuesses = 0
    #configure each game to start with the first image
    imgLabel.config(image=photos[0])
    #let any of the words be used for the guessing
    the_word = random.choice(word_list)
    #let there be spaces separating the words
    the_word_withSpace = " ".join(the_word)
    #use a dash to note the number of letters in the word
    lblWord.set(" ".join("_"*len(the_word)))
#let the player have a number of chances before losing or winning
def guess(letter):
    global numberOfGuesses
    if numberOfGuesses < 11:
        txt = list(the_word_withSpace)
        guessed = list(lblWord.get())
        if the_word_withSpace.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                lblWord.set("".join(guessed))
                if lblWord.get() == the_word_withSpace:
                    messagebox.showinfo("Hangman", "You guessed it!!!")
                    newGame()
        else:
            numberOfGuesses += 1
            imgLabel.config(image=photos[numberOfGuesses])
            if numberOfGuesses == 11:
                messagebox.showwarning("Hangman", "You are DEAD\n Game OVER!!!")

imgLabel = Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image = photos[0])

lblWord = StringVar()
Label(window, textvariable = lblWord, font = ("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=6, pady=10)
      
n = 0
for c in ascii_uppercase:
    Button(window, text = c, command = lambda c=c: guess(c), font="Helvetica 15",width=4).grid(row=1+n//9, column=n%9)
    n += 1

Button(window, text= "New\nGame", command= lambda:newGame(), font = ("Consolas 10 bold")).grid(row=3, column=8, sticky="NSNE")

newGame()
window.mainloop()

print("___________________________________________________________________________________")

print("\ Welcome to HangMan Game!!!")
name = input("Enter Your Name: ")
print("Hello " + name.title() + "!, Best of Luck!")
time.sleep(2)
print("The game is about to start!\ Let's play HangMan!")

def main():
    global count
    global display
    global word
    global already_used
    global length
    global play_game
    word_to_guess = ["January","February","March","April","May","June","July","\
                    August","September","October","November","December"]
    word = random.choice(word_to_guess)
    length = len(word)
    count = 0
    display = '_ ' * length
    already_used = []
    play_game = ""

def play_loop():
    global play_game
    play_game = input("Do you want to play aain? y= yes, n = no")
    while play_game not in ["Y","y","N","n"]:
        play_game = input("Do you want to play again? y= yes, n = no")
    if play_game == "y":
        main()
    else:
        print("Thanks for Playing! We expect you back again!")
        exit()
def hangman():
    global count
    global display
    global word
    global already_used
    global play_game
    limit = 5
    guess = input("This is the hangman word: "+ display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, try a letter\n")
        hangman()
    elif guess in word:
        already_used.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
    elif guess in already_used:
        print("Try another letter.\n")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_used,word)
            play_loop()
    if word == "_" * length:
        print("Congrats! You guessed the word correcrly!")
        play_loop()
    elif count != limit:
        hangman()
main()
hangman()


name = input("Enter your name: ")
print("Hello, " + name + "\n Time to play HangMAN!!!")
print("Start Guessing...")
time.sleep(0.5)
word = ("Secret")
guess = ""
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guess:
            print(char,end = " ")
        else:
            print("",end= "")
            failed += 1
    if failed == 0:
        print("You WON!!!")
        break
    guesses = input("Guess a character: ")
    guess += guesses
    if guesses not in word:
        turns -= 1
        print("Wrong!!!")
        print("You have " + str(turns) + "more guesses")
    if turns == 0:
        print("You Lose!!!")
