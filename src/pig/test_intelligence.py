import unittest
from abc import ABC, abstractmethod


class Intelligence(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def playing_logic(self, total_score: int, current_score: int):
        pass

    def calc_round_score(self, total_score: int, current_score: int):
        return current_score - total_score


class TestIntelligence(unittest.TestCase):

    @unittest.skip("Cannot instantiate abstract class")
    def test_playing_logic(self):
        pass

    @unittest.skip("Cannot instantiate abstract class")
    def test_calc_round_score(self):
        pass

    def test_concrete_intelligence(self):
        class ConcreteIntelligence(Intelligence):
            def playing_logic(self, total_score: int, current_score: int):
                if current_score > total_score:
                    return 'current_score is greater' 
                else:
                    return 'total_score is greater'

        intelligence = ConcreteIntelligence()
        self.assertEqual(intelligence.playing_logic(5, 10), 'current_score is greater')
        self.assertEqual(intelligence.playing_logic(10, 5), 'total_score is greater')
        self.assertIsNot(intelligence.playing_logic(5, 10), intelligence.playing_logic(10, 5))
        self.assertIsNotNone(intelligence.playing_logic(5, 10))
        self.assertIsNotNone(intelligence.playing_logic(10, 5))
        self.assertTrue(intelligence.playing_logic(10, 5) == 'total_score is greater')
        self.assertFalse(intelligence.playing_logic(5, 10) == 'total_score is greater')
        
        self.assertGreater(intelligence.calc_round_score(5, 10), 0)
        self.assertLess(intelligence.calc_round_score(10, 5), 0)
        self.assertGreaterEqual(intelligence.calc_round_score(5, 10), 0)
        self.assertLessEqual(intelligence.calc_round_score(10, 5), 0)
        
        
if __name__ == '__main__':
    unittest.main()