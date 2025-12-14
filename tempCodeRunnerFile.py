import random
while True:
    youstr = input("Enter choice: ")
    computer = random.choice([-1,0,1])
    game_values = {"s":-1,"w":0,"g":1}
    you = game_values[youstr]
    rev_game_values = {-1:"snake", 0:"water", 1:"gun"}

    if you == computer:
        print("It`s a Draw!")
    else:
        if you == 1 and computer == 0:
            print(f"You chose {rev_game_values[1]} \n computer chose {rev_game_values[0]} ")
            print("You Lose, Better luck next time!")
        elif you == 1 and computer == -1:
            print(f"You chose {rev_game_values[1]} \n computer chose {rev_game_values[-1]} ")
            print("You Win!!!")
        elif you == 0 and computer == -1:
            print(f"You chose {rev_game_values[0]} \n computer chose {rev_game_values[-1]} ")
            print("You Lose, Better luck next time!")
        elif you == 0 and computer == 1:
            print(f"You chose {rev_game_values[0]} \n computer chose {rev_game_values[1]} ")
            print("You Win!!!")
        elif you == -1 and computer == 0:
            print(f"You chose {rev_game_values[-1]} \n computer chose {rev_game_values[0]} ")
            print("You Win!!!")
        elif you == -1 and computer == 1:
            print(f"You chose {rev_game_values[-1]} \n computer chose {rev_game_values[1]} ")
            print("You Lose, Better luck next time!")
        else:
            print("something went wrong!")
    