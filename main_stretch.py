import random
numb = random.randint (1,100)
guess = 0
attempt = 0
again = "y"
pb = 0
print("I am thinking of a number between 1 and 100")

while again == "y":
    while int(guess) != numb:
        guess = input("Please input a number: ")
        if guess.isdigit():
            if (int(guess)) < numb:
                print("Too low")
                attempt = attempt + 1
            elif (int(guess)) > numb:
                print("Too high")
                attempt = attempt + 1
            elif (int(guess)) == numb:
                attempt = attempt + 1
                print(f"You guessed it! It only took you {attempt} amount of try!")
                if pb == 0:
                    pb = attempt
                elif attempt < pb:
                    pb = attempt
        else:
            print("Invalid input, please try again")
            guess = 0
    again = input("Do you want to play again? (y/n): ")
    if again == "y":
        print(f"Your personal best is {pb} and your current attempt is {attempt}")
        numb = random.randint (1,100)
        guess = 0
        attempt = 0
    elif again == "n":
        print(f"Your personal best is {pb}")
    else:
        print("Invalid input, please try again")
        again = "y"

    


