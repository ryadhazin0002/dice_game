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
        self.fileService.save_players(self.players)

    def get_player(self, name: str) -> HumanPlayer | None:
        """Get player name"""
        for player in self.players:
            if name == player.name:
                return player

    def add_player(self, name: str) -> HumanPlayer:
        player = self.get_player(name)
        if player is not None:
            return player
        player = HumanPlayer(random.randint(1, 500), name, 0)
        self.fileService.add_player(player)
        self.players.append(player)
        return player

    def init_players(self, playing_mode: str) -> tuple[Player, Player]:
        player1_name = input("Please enter your name: ")
        player1: Player = self.add_player(player1_name)
        player2: Player

        while True:
            difficulty_choice = input("Choose Co-player difficulty (Easy or Hard): ").lower()
            if difficulty_choice in ("easy", "hard"):
                player2 = COPlayer(difficulty_choice)
                break
            else:
                print("Invalid choice. Please enter 'Easy' or 'Hard'.")

        return player1, player2

    def start(self):
        while True:
            choice = self.display_main_menu()
            if choice == "1":
                playing_mode = self.display_new_game_menu()
                players: tuple[Player, Player] = self.init_players(playing_mode)
                self.play(players[0], players[1])
                self.fileService.save_players(self.players)
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
                print(f"dice {diceValue}")
                print(f"Your current score is {round_score}")
                print("Press 'Q' to exit")
                print("Press 'R' to restart")
                if isinstance(current_player, COPlayer):  # Check if current player is COPlayer
                    roll_again = current_player.take_action(round_score)  # Pass round_score here
                else:
                    roll_again = input("Roll again or Hold? 'r' or 'h': ")
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
                            print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
                            print(f"🎉🎉🎉 DRAW !!!! 🎉🎉🎉")
                            print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
                            break

                        print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
                        print(f"🎉🎉🎉 congratulations {winner.name} won 🎉🎉🎉")
                        print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
                        if isinstance(winner, HumanPlayer):
                            winner.high_scores.append(str(winner.total_score))
                        break
                    print(
                        "***************************************************"
                        "*******************"
                    )
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

    def change_current_player(self, current_player, first_player, second_player):
        if current_player.name == first_player.name:
            current_player = second_player
        else:
            current_player = first_player
        return current_player

    def display_main_menu(self):
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
        print("1. CO-Player")
        print("2. Multi-Player")
        return input("Your choice: ")

    def display_co_player_level(self):
        print("1. Easy")
        print("2. Hard")
        return input("Your choice: ")

    def display_game_rules(self):
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
        for player in self.players:
            print(f"{player.name}   {player.high_scores}")
