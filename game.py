import curses
import time
from co_player import COPlayer
from dice import Dice
from human_player import HumanPlayer
from player import Player
class Game:

    def init_players(self, playing_mode: str) -> tuple[Player, Player]:
        player1_name = input("Please enter your name: ")
        player1 : Player = HumanPlayer(0, player1_name, 0)
        player2 : Player
        if playing_mode == "1":
            player2 = COPlayer()
        else:
            player2_name = input("Please enter the second player name: ")
            player2 = HumanPlayer(1,player2_name, 0)
        return player1, player2

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



    def display_main_menu(self):
        print ("🎲 Welcome to Pig Dice Game 🎲")
        print ()
        print ("1. Start new game")
        print ("2. Player's Highscore")
        print ("3. Rules of the game")
        print ("4. Change player's name")
        return input("Your choice: ")

    
    def display_new_game_menu(self):
        print ("1. CO-Player")
        print ("2. Multi-Player")
        return input("Your choice: ")
    

    def display_game_rules(self):
        print("🎲 Pig Dice Game Rules🎲")
        print()
        print("🧩 Objective:🧩\nBe the first player to reach a total score of 100 points.")
        print("Equipment: 1 standard six-sided dice")
        print()
        print("🕹️  Gameplay:🕹️")
        print("1. Players take turns rolling the dice during their turn.")
        print("2. Players take turns rolling the dice during their turn.")
        print("3. If a player rolls a 2-6, they add that number to their turn total and can choose to either roll again or end their turn.")
        print("4. If a player chooses to end their turn, they add the turn total to their overall score.")
        print("5. Rolling a 1 during subsequent rolls forfeits all points gained in that turn.")
        print()
        print("🎊 Winning:🎊")
        print("The first player to reach or exceed 100 points wins the game.🥇")
        print()
        print("🤓 Strategy:🤓")
        print("Decide wisely when to stop rolling and 'bank' the points to avoid losing them on a subsequent roll.")
        print()
        print("🎲 Enjoy the game!🎲")