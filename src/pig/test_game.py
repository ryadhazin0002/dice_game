import random
import unittest
from unittest.mock import patch
from game import Game
from human_player import HumanPlayer
from co_player import COPlayer
from easy_level import Easy
from hard_level import Hard


class TestGame(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        player1 = HumanPlayer("654548", "player1", ["120","100"])
        player2 = HumanPlayer("879855", "player2", [])
        players = [player1, player2]
        self.game = Game(players,0,"mock_players.txt")
        super().__init__(methodName)

    def test_init_game(self):
        self.assertIsInstance(self.game, Game)
        self.assertIsNotNone(self.game, None)
        
    def test_change_player_name(self):
        new_name = "new name"
        player = self.game.players[0]
        old_name = player.name
        self.game.change_player_name(new_name, player)
        self.assertEqual(player.name, new_name)
        self.assertNotEqual(player.name, old_name)
        self.assertIsInstance(player.name, str)
        self.game.change_player_name(old_name, player)

    @patch('builtins.input', side_effect=["1","1","player1","1","CHEAT","CHEAT","h","5"])
    def test_invalid_player_filename(self, mock_input):
        game = Game(self.game.players,0,"test.ttx")
        game.change_player_name("test", game.players[0])
        game.add_player("alksdhfkahsdl")
        game.start()
        #Todo: Capture output

    def test_get_existed_player(self):
        players_count = len(self.game.players)
        existed_player = self.game.get_player("player2")
        self.assertIsInstance(existed_player, HumanPlayer)
        self.assertIsNotNone(existed_player, None)
        self.assertEqual(len(self.game.players),players_count)
        non_existed_player = self.game.get_player("not existed player")
        self.assertIsNone(non_existed_player, None)
        self.assertEqual(len(self.game.players),players_count)    

    def test_add_player(self):
        players_count = len(self.game.players)
        player = self.game.add_player("player2")
        self.assertIsInstance(player, HumanPlayer)
        self.assertEqual(len(self.game.players), players_count)
        new_player = self.game.add_player(f"{random.randint(1, 100)}{random.randint(1, 100)}")
        self.assertIsInstance(new_player, HumanPlayer)
        self.assertNotEqual(len(self.game.players), players_count)

    @patch('builtins.input', side_effect=['player1', "player2","player1","1","player1","2"])
    def test_init_multiplayers(self, mock_input):
        player1, player2 = self.game.init_players("2")
        self.assertIsInstance(player1, HumanPlayer)
        self.assertIsInstance(player2, HumanPlayer)
        self.assertEqual(player1.name, "player1")
        self.assertEqual(player2.name, "player2")
        human_player, easy_co_player = self.game.init_players("1")
        self.assertIsInstance(human_player, HumanPlayer)
        self.assertIsInstance(easy_co_player, COPlayer)
        self.assertIsInstance(easy_co_player.level, Easy)
        self.assertEqual(human_player.name, "player1")
        self.assertEqual(easy_co_player.name, "CO")
        human_player, hard_co_player = self.game.init_players("1")
        self.assertIsInstance(human_player, HumanPlayer)
        self.assertIsInstance(hard_co_player, COPlayer)
        self.assertIsInstance(hard_co_player.level, Hard)
        self.assertEqual(human_player.name, "player1")
        self.assertEqual(easy_co_player.name, "CO")

    @patch('builtins.input', side_effect=["2","5","9","5","3","5","4","player1","new name","4","new name","player1","5"])
    def test_start_and_check_options(self,mock_input):
        self.game.start() #higscore case
        #TODO: Capture highscore and test it
        self.game.start() #invalid case
        self.game.start() #rultes case
        #TODO: Capture rules and test it
        self.game.start() #change name case

    @patch('builtins.input', side_effect=["1","1","player1","1","r","R","Q","1","1","player1","1","h","CHEAT","CHEAT","h","5"])
    def test_play_game(self,mock_input):
        self.game.start()
   
if __name__ == '__main__':
    unittest.main()
       