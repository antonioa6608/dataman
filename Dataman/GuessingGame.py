import random

def randomNum():
    return random.randint(1,20)

def getinput():
    try:
        guess = int(input("I am thinking of a number from 1-20 : " ))
        return guess
    except ValueError:
        print("Not correct input, try again")

        return getinput()

def guessGame():
    correctNum = randomNum()
    attempts= 0
    print(f"The guessing game")


    while True:
        guesses = getinput()

        attempts += 1

        if guesses < correctNum:
            print("Try again , the number is higher")
        elif guesses > correctNum:
            print("try again, the number is lower")
        else:
            print(f"RIGHT!, the correct number was {correctNum}")
            print(f"Attempts made : {attempts}")

            
            break

if __name__=="__main__":
    guessGame()
