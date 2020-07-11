import random

user_name = input("Enter your name: ")
print("\nHello", user_name.capitalize(), "let's Play Mallu Version Hangman Game.lol")


userGuesslist = []
userGuesses = []
playGame = True
category = ""
continueGame = "Y"
location = ['munnar','Cochin','idukki','Kuttanad','Wayanad','Kumarakom','Kovalam','Vagamon','Nelliampathy','Ponmudi','Varkala','Thrissur','Gavi']
Cars  =['Maruti','Hyundai','Volkswagen','Nissan','Renault','Toyota','Honda','MG','KIA','Tata','Ford']


while True:
    #Choosing the Secret word
    while True:
        if category.upper() == 'C':
            secretWord = random.choice(Cars).lower()
            #print(secretWord)
            break
        elif category.upper() == 'L':
            secretWord = random.choice(location).lower()
            break
        else:
            category = input("\nPlease select a valid categary: For Cars press : C  For Location press : L  To exit press : X \nEnter the key : ").lower()

        if category.upper() == 'X':
            print("Bye. See you next time!")
            playGame = False
            break

    if playGame:
        secretWordList = list(secretWord)
        attempts = (len(secretWord) + 2)

        def printGuessedLetter():
            print("Your Secret word is: " + ''.join(userGuesslist))
    #Adding blank lines to userGuesslist to create the blank secret word
        for n in secretWordList:
            userGuesslist.append('_')
        printGuessedLetter()

        print("Remaining gussess", attempts)


        #starting the game
        while True:

            print("Guess a letter:")
            letter = input().lower()

            if letter in userGuesses:
                print("You already guessed this letter, try something else.")

            else:
                attempts -= 1
                userGuesses.append(letter)
                if letter in secretWordList:
                    print("Nice guess!")
                    if attempts > 0:
                        print("You have ", attempts, 'guess left!')
                    for i in range(len(secretWordList)):
                        if letter == secretWordList[i]:
                            letterIndex = i
                            userGuesslist[letterIndex] = letter.upper()
                    printGuessedLetter()

                else:
                    print("Oops! Try again.")
                    if attempts > 0:
                        print("You have ", attempts, 'guess left!')
                    printGuessedLetter()


            #Win/loss logic for the game
            joinedList = ''.join(userGuesslist)
            if joinedList.upper() == secretWord.upper():
                print("Yay lol! you won.")
                break
            elif attempts == 0:
                print("Too many Guesses!, Sorry better luck next time.")
                print("The secret word was: "+ secretWord.upper())
                break

        #Play again logic for the game
        continueGame = input("Do you want to play again? Y to continue, any other key to quit ")
        if continueGame.upper() == 'Y':
            category = input("\nPlease select a valid categary: \nFor Cars press : C \nFor Location press : L \nTo exit press : X\nEnter the key : ")
            userGuesslist = []
            userGuesses = []
            playGame = True
        else:
            print("Thank You for playing. See you next time!")
            break
    else:
        break
