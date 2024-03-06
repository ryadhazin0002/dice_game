from human_player import HumanPlayer
import os


class FileService:

    def __init__(self, filename : str) -> None:
        self.filename = filename
        pass

    filename: str

    def load_players(self) -> list[HumanPlayer]:
        """Load the players from players.txt"""
        if not os.path.exists(self.filename):
            raise FileNotFoundError()
        players: list[HumanPlayer] = []
        with open(self.filename, encoding="utf-8") as file:
            while True:
                line = file.readline().rstrip("\n")
                if line == "":
                    break
                line = line.split(":")
                id = line[0]
                name = line[1]
                high_score = line[2].split(",")
                if line[2] == "":
                    high_score = []
                player = HumanPlayer(id, name, high_score)
                players.append(player)
            return players

    def save_players(self, players: list[HumanPlayer]):
        """Save the players in players.txt"""
        if not os.path.exists(self.filename):
            raise FileNotFoundError()
        with open(self.filename, "w") as file:
            for player in players:
                file.write(
                    f"{player.id}:{player.name}:"
                    f"{str.join(',',player.high_scores)}\n"
                )

    def add_player(self, player: HumanPlayer):
        """Add new Player to players.txt"""
        if not os.path.exists(self.filename):
            raise FileNotFoundError()
        with open(self.filename, "a") as file:
            file.write(f"{player.id}:{player.name}:\n")
