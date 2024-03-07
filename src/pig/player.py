from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self, name, total_score):
        self.name = name
        self.total_score = total_score

    name: str
    total_score: int

    @abstractmethod
    def take_action(self, current_score: int):
        """ "Abstract take action method"""
        pass  # pragma: no cover
