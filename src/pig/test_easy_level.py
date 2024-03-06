import unittest
from unittest.mock import patch
from easy_level import Easy  # Import the Easy class
import random
import time

class TestEasyLevel(unittest.TestCase):

    @patch('random.choice')
    @patch('time.sleep')
    def test_playing_logic_roll(self, mock_sleep, mock_choice):
        easy_instance = Easy()  
        mock_choice.return_value = 'r'  
        self.assertEqual(easy_instance.playing_logic(10, 5), 'r')
        mock_sleep.assert_called_with(1) 

    @patch('random.choice')
    @patch('time.sleep')
    def test_playing_logic_hold(self, mock_sleep, mock_choice):
        easy_instance = Easy() 
        mock_choice.return_value = 'h' 
        self.assertEqual(easy_instance.playing_logic(10, 5), 'h')
        mock_sleep.assert_called_with(1)  

if __name__ == '__main__':
    unittest.main()
    