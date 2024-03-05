import unittest
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, total_score):
        self.name = name
        self.total_score = total_score

    @abstractmethod
    def take_action(self, current_score: int):
        """Abstract take action method"""
        pass


class ConcretePlayer(Player):
    def take_action(self, current_score: int):
        if current_score < 50:
            return "r"
        else:
            return "h"




if __name__ == '__main__':
    unittest.main()
