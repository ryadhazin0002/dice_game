import curses
import time
from co_player import COPlayer
from dice import Dice
from human_player import HumanPlayer
from player import Player
class Game:

    def play(self, first_player : Player, second_player : Player) -> Player:
        current_player : Player = first_player
        dice = Dice()
        round_score = 0
        print(f"🔥🔥🔥 {current_player.name} turn 🔥🔥🔥")
        while True:
             stdscr = curses.initscr()
             curses.noecho()
             curses.cbreak()
             diceValue = dice.roll_dice(stdscr)
             dice.print_to_terminal(diceValue)
             if diceValue != 1 and round_score < 100:
                 round_score += diceValue
                 print (f"dice {diceValue}")               
                 print (f"Your current score is {round_score}")
                 if round_score >= 100:
                     print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
                     print(f"🎉🎉🎉 congratulations {current_player.name} won 🎉🎉🎉")
                     print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
                     break
                 roll_again = current_player.take_action()
                 if roll_again == "r":
                     continue
                 elif roll_again == "h":
                     current_player.total_score = round_score
                     print (f"{current_player.name}'s total score is {current_player.total_score}")
                     print("**********************************************************************")
                     time.sleep(2)
                     current_player = self.change_current_player(current_player, first_player, second_player)
                     round_score = current_player.total_score
                     print(f"🔥🔥🔥 {current_player.name} turn 🔥🔥🔥")
                     time.sleep(2)
                     continue
                 else:
                     print("invalid choice")
                     valid_choice = input("Roll again or Hold? 'r' or 'h': ")
             
             elif diceValue == 1:
                 current_player = self.change_current_player(current_player, first_player, second_player)
                 round_score = current_player.total_score
                 print("You have lost your round score!!!")
                 print("**********************************************************************")
                 time.sleep(2)
                 print(f"🔥🔥🔥 {current_player.name} turn 🔥🔥🔥")
                 time.sleep(2)
                 print(f"your score is {round_score}")
                 time.sleep(1)
                 #ask_to_continue = input("New Game? 'y' or 'n': ")
                 #if ask_to_continue == "y":
                 #    continue
                 #elif ask_to_continue == "n":
                 #    break

    def change_current_player(self, current_player, first_player, second_player):
       if current_player.name == first_player.name:
           current_player = second_player
       else:
           current_player = first_player
       return current_player
