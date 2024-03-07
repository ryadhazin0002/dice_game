from abc import ABC, abstractmethod


class Intelligence(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def playing_logic(self, total_score: int, current_score: int):
        """Abstract method to determine the playing logic of the Intelligence"""
        pass  # pragma: no cover

    def calc_round_score(self, total_score: int, current_score: int):
        """Claculates the round score based on the total score and current score"""
        return current_score - total_score
