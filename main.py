import random

from human_player import HumanPlayer
from player import Player

player1 = HumanPlayer(0, input("please enter the first player name: "), 0)
player2 = HumanPlayer(0, input("please enter the second player name: "), 0)
currentPlayer : Player = player1
round_score = 0
print(f"Welcome {player1.name}, {player2.name} to PIG Dice Game, Lets Start!!")
print(f"{currentPlayer.name}'s Turn")
while True:
     diceValue = random.randint(1, 6)
     if diceValue != 1 and round_score < 100:
         round_score += diceValue
         print (f"dice {diceValue}")               
         print (f"Your {currentPlayer.name}'s score is {round_score}")
         if round_score >= 100:
             print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
             print(f"🎉🎉🎉 congratulations {currentPlayer.name}, you won 🎉🎉🎉")
             print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
             break
         roll_again = currentPlayer.take_action()
         if roll_again == "r":
             continue
         elif roll_again == "h":
             currentPlayer.total_score = round_score
             print (f"{currentPlayer.name} total score is {currentPlayer.total_score}")
             print("**********************************************************************")
             if currentPlayer.name == player1.name:
                 currentPlayer = player2
             else:
                 currentPlayer = player1
             round_score = currentPlayer.total_score
             print(f"{currentPlayer.name}'s Turn")
             continue
         else:
             print("invalid choice")
             valid_choice = input("Roll again or Hold? 'r' or 'h': ")
     
     elif diceValue == 1:
         if currentPlayer.name == player1.name:
             currentPlayer = player2
         else:
             currentPlayer = player1
         round_score = currentPlayer.total_score
         print("You have lost your round score!!!")
         print("**********************************************************************")
         print(f"{currentPlayer.name}'s Turn")