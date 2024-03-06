import unittest
from file_service import FileService
from human_player import HumanPlayer
import os

class TestFileService(unittest.TestCase):

    def setUp(self):
        self.file_service = FileService()
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



if __name__ == '__main__':
    unittest.main()
