from file_service import FileService
from game import Game

fileService = FileService()
try:
    players = fileService.load_players()
    game = Game(players)
    game.start()
except FileNotFoundError:
    print("An error occurred while trying to read the file.")
