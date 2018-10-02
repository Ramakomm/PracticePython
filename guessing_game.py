import random
def game_on(a,b):
    if (a == b):
        print("you have guessed it right")
    elif (a<b):
        print("go lower")
    else:
        print("go higher")

choice = "yes"
while (choice != "0"):
    a = random.randint(1,9)
    user_input = input("Guess the number between 1 and 9  ")
    while(a!= int(user_input)):
        game_on(a,int(user_input))
        user_input = input("next guess ")
    print("Your guess is correct " + user_input)
    choice = input("Press 0 to Quit ").lower()