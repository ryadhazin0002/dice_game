from human_player import HumanPlayer


class FileService:

    def __init__(self) -> None:
        self.filename = "human_players.txt"
        pass

    filename: str

    def load_players(self) -> list[HumanPlayer]:
        players: list[HumanPlayer]
        with open (self.filename) as file:
            while True:
                line = file.readline().rstrip("\n")
                if line == "": break
                line = line.split(",")
                id = line[0]
                name = line[1]
                score = line[2]
                player = HumanPlayer(id, name, score)
                players.append(player)
        return player
    
    def save_players(self, players: list[HumanPlayer]):
        with open (self.filename, "w") as file:
            for player in players:
                file.write(f"{player.id},{player.name},{player.total_score}\n")

    def add_player(self, player: HumanPlayer):
        with open (self.filename, "a") as file:
                file.write(f"{player.id},{player.name},{player.total_score}\n")