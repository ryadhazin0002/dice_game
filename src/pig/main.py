from file_service import FileService
from game import Game
from in_venv import in_venv
import os

current_directory = os.getcwd()

fileService = FileService(filename="./human_players.txt")
try:
    print(in_venv())
    players = fileService.load_players()
    game = Game(players,1,"./human_players.txt")
    game.start()
except FileNotFoundError:
    print("An error occurred while trying to read the file.")
