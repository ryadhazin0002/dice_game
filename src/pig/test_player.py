import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("TestPlayer", 0)
    