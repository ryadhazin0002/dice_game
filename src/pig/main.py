from file_service import FileService
from game import Game
from in_venv import in_venv

fileService = FileService()
try:
    print(in_venv())
    players = fileService.load_players()
    game = Game(players)
    game.start()
except FileNotFoundError:
    print("An error occurred while trying to read the file.")