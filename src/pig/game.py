import curses
import time
from co_player import COPlayer
from dice import Dice
from human_player import HumanPlayer
from player import Player
from file_service import FileService
import random


class Game:

    def __init__(self, players) -> None:
        """Init for Game Class"""
        self.players = players
        pass

    players: list[HumanPlayer]
    fileService = FileService()

    def change_player_name(self, new_name: str, player: HumanPlayer):
        """Change player name"""
        player.name = new_name
        try:
            self.fileService.save_players(self.players)
        except FileNotFoundError:
            print("An error occurred while trying to change player's name in the file.")

    def get_player(self, name: str) -> HumanPlayer | None:
        """Get player name"""
        for player in self.players:
            if name == player.name:
                return player

    def add_player(self, name: str) -> HumanPlayer:
        """Add player to players list and players.txt if player is not already exsist"""
        player = self.get_player(name)
        if player is not None:
            return player
        player = HumanPlayer(random.randint(1, 500), name, 0)
        try:
            self.fileService.add_player(player)
            self.players.append(player)
        except FileNotFoundError:
            print("An error occurred while trying to add new player to the file.")
        return player

    def init_players(self, playing_mode: str) -> tuple[Player, Player]:
        """Players initialization"""
        player1_name = input("Please enter your name: ")
        player1: Player = self.add_player(player1_name)
        player2: Player
        if playing_mode == "1":
            player2 = COPlayer()
        else:
            player2_name = input("Please enter the second player name: ")
            player2 = self.add_player(player2_name)
        return player1, player2

    def start(self):
        """The start menu"""
        while True:
            choice = self.display_main_menu()
            if choice == "1":
                playing_mode = self.display_new_game_menu()
                players: tuple[Player, Player] = self.init_players(playing_mode)
                self.play(players[0], players[1])
                try:
                    self.fileService.save_players(self.players)
                except FileNotFoundError:
                    print("An error occurred while trying to update the file.")
            elif choice == "2":
                self.display_players_highscore()
            elif choice == "3":
                self.display_game_rules()
            elif choice == "4":
                old_name = input("Enter your current name: ")
                new_name = input("Enter your new name: ")
                player = self.get_player(old_name)
                self.change_player_name(new_name, player)
            else:
                print("invalid value!!")
                print("Please enter 1, 2, 3 or 4")
                time.sleep(1)
                print()

    def play(self, first_player: Player, second_player: Player):
        """Play the game"""
        current_player: Player = first_player
        dice = Dice()
        round_score = 0
        print(f"🔥🔥🔥 {current_player.name} turn 🔥🔥🔥")
        while True:
            stdscr = curses.initscr()
            curses.noecho()
            curses.cbreak()
            diceValue = dice.roll_dice(stdscr)
            dice.print_to_terminal(diceValue)
            if diceValue != 1:
                round_score += diceValue
                self.display_dice_value_and_round_score(diceValue, round_score)
                roll_again = current_player.take_action()
                if roll_again == "r":
                    time.sleep(2)
                    continue
                elif roll_again == "h":
                    current_player.total_score = round_score
                    print(
                        f"{current_player.name}'s total"
                        f" score is {current_player.total_score}"
                    )
                    if max(first_player.total_score, second_player.total_score) >= 100:
                        winner: Player
                        if first_player.total_score > second_player.total_score:
                            winner = first_player
                        elif second_player.total_score > first_player.total_score:
                            winner = second_player
                        else:
                            self.display_draw()
                            break

                        self.display_congratulations(winner)
                        if isinstance(winner, HumanPlayer):
                            winner.high_scores.append(str(winner.total_score))
                        break
                    print("***************************************************")
                    time.sleep(2)
                    current_player = self.change_current_player(
                        current_player, first_player, second_player
                    )
                    round_score = current_player.total_score
                    print(f"🔥🔥🔥 {current_player.name} turn 🔥🔥🔥")
                    time.sleep(2)
                    continue
                elif roll_again == "CHEAT":
                    current_player.total_score += 90
                    round_score += 90
                    continue
                elif roll_again == "Q":
                    break
                elif roll_again == "R":
                    first_player.total_score = 0
                    second_player.total_score = 0
                    round_score = 0

                else:
                    print("invalid choice")
                    valid_choice = input("Roll again or Hold? 'r' or 'h': ")

            elif diceValue == 1:
                current_player = self.change_current_player(
                    current_player, first_player, second_player
                )
                round_score = current_player.total_score
                print("You have lost your round score!!!")
                print("******************************************************")
                time.sleep(2)
                print(f"🔥🔥🔥 {current_player.name} turn 🔥🔥🔥")
                time.sleep(2)
                print(f"your score is {round_score}")
                time.sleep(1)

    def display_draw():
        print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
        print(f"🎉🎉🎉 DRAW !!!! 🎉🎉🎉")
        print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")

    def display_congratulations(self, winner: Player):
        print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
        print(f"🎉🎉🎉 congratulations {winner.name} won 🎉🎉🎉")
        print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")

    def display_dice_value_and_round_score(self, diceValue, round_score):
        print(f"dice {diceValue}")
        print(f"Your current score is {round_score}")
        print("Press 'Q' to exit")
        print("Press 'R' to restart")

    def change_current_player(self, current_player, first_player, second_player):
        """Change the current player"""
        if current_player.name == first_player.name:
            current_player = second_player
        else:
            current_player = first_player
        return current_player

    def display_main_menu(self):
        """Display main menu"""
        print()
        print("*******************************")
        print("🎲 Welcome to Pig Dice Game 🎲")
        print("*******************************")
        print()
        print("1. Start new game")
        print("2. Player's Highscore")
        print("3. Rules of the game")
        print("4. Change player's name")
        return input("Your choice: ")

    def display_new_game_menu(self):
        """Display new game Menu"""
        print("1. CO-Player")
        print("2. Multi-Player")
        return input("Your choice: ")

    def display_co_player_level(self):
        """Display CoPlayer level"""
        print("1. Easy")
        print("2. Hard")
        return input("Your choice: ")

    def display_game_rules(self):
        """Display game rules"""
        print("🎲 Pig Dice Game Rules🎲")
        print()
        print(
            "🧩 Objective:🧩\nBe the first player to"
            " reach a total score of 100 points."
        )
        print("Equipment: 1 standard six-sided dice")
        print()
        time.sleep(1)
        print("🕹️  Gameplay:🕹️")
        print("1. Players take turns rolling the dice during their turn.")
        print("2. Players take turns rolling the dice during their turn.")
        print(
            "3. If a player rolls a 2-6, they add that number to their "
            "turn total and can choose to either roll again or "
            "end their turn."
        )
        print(
            "4. If a player chooses to end their turn, they add the turn"
            " total to their overall score."
        )
        print(
            "5. Rolling a 1 during subsequent rolls forfeits all points"
            " gained in that turn."
        )
        print()
        time.sleep(1)
        print("🎊 Winning:🎊")
        print("The first player to reach or exceed 100 points wins the game.🥇")
        print()
        time.sleep(1)
        print("🤓 Strategy:🤓")
        print(
            "Decide wisely when to stop rolling and 'bank' the points to "
            "avoid losing them on a subsequent roll."
        )
        print()
        time.sleep(1)
        print("🎲 Enjoy the game!🎲")

    def display_players_highscore(self):
        """Display player's highscore"""
        for player in self.players:
            print(f"{player.name}   {player.high_scores}")
