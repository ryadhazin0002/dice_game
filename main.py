from file_service import FileService
from game import Game

fileService = FileService()
players = fileService.load_players()
game = Game(players)
game.start()