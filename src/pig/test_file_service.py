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



if __name__ == '__main__':
    unittest.main()
