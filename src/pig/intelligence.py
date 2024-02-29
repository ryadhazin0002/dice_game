from abc import ABC, abstractmethod


class Intelligence(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def playing_logic(self, total_score: int, current_score: int):
        pass

    def calc_round_score(self, total_score: int, current_score: int):
        return current_score - total_score
