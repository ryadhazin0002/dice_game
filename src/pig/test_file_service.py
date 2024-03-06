import unittest
from file_service import FileService
from human_player import HumanPlayer
import os

class TestFileService(unittest.TestCase):

    def setUp(self):
        self.file_service = FileService("mock_players.txt")
        with open(self.file_service.filename, 'w') as f:
            f.write("1:Ryad:100,200,120\n")
            f.write("2:Mustafa:150,120\n")

    def test_load_players(self):
        players = self.file_service.load_players()
        self.assertEqual(len(players), 2)
        self.assertIsInstance(players[0], HumanPlayer)
        self.assertIsInstance(players[1], HumanPlayer)
        self.assertEqual(players[0].id, "1")
        self.assertEqual(players[0].name, "Ryad")
        self.assertEqual(players[0].high_scores, ["100", "200", "120"])
        self.assertEqual(players[1].id, "2")
        self.assertEqual(players[1].name, "Mustafa")
        self.assertEqual(players[1].high_scores, ["150", "120"])
        self.assertTrue(os.path.exists(self.file_service.filename))

    def test_save_players(self):
        players = [
            HumanPlayer("3", "Zakaria", ["120", "100"]),
            HumanPlayer("4", "Merjam", ["120"])
        ]
        self.file_service.save_players(players)
        loaded_players = self.file_service.load_players()
        self.assertEqual(len(loaded_players), 2)
        self.assertEqual(loaded_players[0].id, "3")
        self.assertEqual(loaded_players[0].name, "Zakaria")
        self.assertEqual(loaded_players[0].high_scores, ["120", "100"])
        self.assertEqual(loaded_players[1].id, "4")
        self.assertEqual(loaded_players[1].name, "Merjam")
        self.assertEqual(loaded_players[1].high_scores, ["120"])
        with open(self.file_service.filename) as file:
            self.assertIn("3:Zakaria:120,100", file.read())

    def test_add_player(self):
        new_player = HumanPlayer("5", "Sara", ["120", "110"])
        self.file_service.add_player(new_player)
        loaded_players = self.file_service.load_players()
        self.assertEqual(len(loaded_players), 3)
        self.assertEqual(loaded_players[2].id, "5")
        self.assertEqual(loaded_players[2].name, "Sara")
        self.assertEqual(loaded_players[2].high_scores, [])
        with open(self.file_service.filename) as file:
            self.assertIn("5:Sara:", file.read())

if __name__ == '__main__':
    unittest.main()
