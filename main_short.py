import random
while True:
    print("*************************************")
    print("Your choices are: \n 1. Snake = s \n 2. Water = w \n 3.gun = g")
    youstr = input("Enter choice: ")
    computer = random.choice([-1,0,1])
    game_values = {"s":-1,"w":0,"g":1}
    you = game_values[youstr]
    rev_game_values = {-1:"snake", 0:"water", 1:"gun"}

    if you == computer:
        print("It`s a Draw!")
    else:

        #  if you == 1 and computer == 0: [you - computer = 1]
        #      print(f"You chose {rev_game_values[1]} \n computer chose {rev_game_values[0]} ") 
        #      print("You Lose, Better luck next time!")
        #  elif you == 1 and computer == -1: [you - computer = 2]
        #      print(f"You chose {rev_game_values[1]} \n computer chose {rev_game_values[-1]} ")
        #      print("You Win!!!")
        #  elif you == 0 and computer == -1:[you-computer = 1 ]
        #      print(f"You chose {rev_game_values[0]} \n computer chose {rev_game_values[-1]} ")
        #      print("You Lose, Better luck next time!")
        #  elif you == 0 and computer == 1: [you - computer = -1]
        #      print(f"You chose {rev_game_values[0]} \n computer chose {rev_game_values[1]} ")
        #      print("You Win!!!")
        #  elif you == -1 and computer == 0: [you - computer = -1]
        #      print(f"You chose {rev_game_values[-1]} \n computer chose {rev_game_values[0]} ")
        #      print("You Win!!!")
        #  elif you == -1 and computer == 1: [you - computer = -2]
        #      print(f"You chose {rev_game_values[-1]} \n computer chose {rev_game_values[1]} ")
        #      print("You Lose, Better luck next time!")
        #  else:
        #     print("something went wrong!")   so here in most cases when we losing we get difference of you and computer as either 1 or -2. sowe can use this logic to make our code shorter



        if (you - computer) == 1 or (you - computer) == -2:
            print(f"You chose {rev_game_values[you]} \ncomputer chose {rev_game_values[computer]} ") 
            print("You Lose, Better luck next time!")
        else:
            print(f"You chose {rev_game_values[you]} \ncomputer chose {rev_game_values[computer]} ") 
            print("You Win!!!")
