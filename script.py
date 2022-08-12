#for the bot choice:
import random


user_score = 0
bot_score = 0

#to avoid input problemes 
VALID_CHOICE = ["rock", "paper", "scissors"]

#welcome
print("""        ------------------------------------------------------------------------
               Welcome to Rock 🗿 Paper 📄 Scissors ✂ !
            U are vs a bot the first one to 3 win the game
                                    GL
        ------------------------------------------------------------------------""")


while user_score != 3 and bot_score != 3:
    user_choice = input("What do u play ? rock, paper, scissors: ").lower()
    #check the input
    if user_choice not in VALID_CHOICE:
        print(" Invalid choice... \n  Valid choices are : rock, paper, scissors")
        continue

    #bot choice
    bot_choice = random.choice(VALID_CHOICE)
    
#check the winner
    if user_choice == bot_choice :
        pass
    elif user_choice == "rock" and bot_choice == "scissors":
        user_score += 1
    elif user_choice == "paper" and bot_choice == "rock":
        user_score += 1
    elif user_choice == "scissors" and bot_choice == "paper":
        user_score += 1
    else:
        bot_score += 1

#print the score
    print(f"""        U choose {user_choice}
        The bot choose {bot_choice} 

        Ur score: {user_score}
        The bot score: {bot_score}
        """)

#The end ; print the winner of the game
if user_score == 3:
    print("U are the winner ! gg")
else:
    print("The bot won this one \nReady for the revenge ?")
