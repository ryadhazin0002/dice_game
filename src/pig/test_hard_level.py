import unittest
from unittest.mock import patch
from hard_level import Hard
import time

class TestHardLevel(unittest.TestCase):
    @patch('builtins.print')
    @patch('time.sleep')
    def test_playing_logic_roll(self, mocked_sleep, mocked_print):
        hard_instance = Hard()
        choice = hard_instance.playing_logic(50, 20)
        self.assertEqual(choice, "r")
        mocked_print.assert_called_with("Roll")
        mocked_sleep.assert_called_with(1)  
    

    
if __name__ == "__main__":
    unittest.main()