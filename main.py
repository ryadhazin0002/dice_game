import random

from human_player import HumanPlayer

player = HumanPlayer(0, input("please enter your name: "), 0)
round_score = 0
print(f"Welcome {player.name} to PIG Dice Game, Lets Start!!")
while True:
     diceValue = random.randint(1, 6)
     if diceValue != 1 and round_score < 100:
         round_score += diceValue
         print (f"dice {diceValue}")               
         print (f"Your current score is {round_score}")
         if round_score >= 100:
             print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
             print(f"🎉🎉🎉 congratulations {player.name}, you won 🎉🎉🎉")
             print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
             break
         roll_again = player.take_action()
         if roll_again == "r":
             continue
         elif roll_again == "h":
             player.total_score = round_score
             print (f"Your total score is {player.total_score}")
             print("**********************************************************************")
             continue
         else:
             print("invalid choice")
             valid_choice = input("Roll again or Hold? 'r' or 'h': ")
     
     elif diceValue == 1:
         round_score = player.total_score
         print("You have lost your round score!!!")
         print("**********************************************************************")