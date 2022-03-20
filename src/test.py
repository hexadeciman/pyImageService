import unittest
from lib import Parser
from constants import *

class NamesTestCase(unittest.TestCase):

    def test_csvToArray2d1(self):
        csvArray = Parser.csvToArray2d(CSV_PATH)
        print("first item", csvArray[0][0])
        self.assertEqual(len(csvArray), 5460)

    def test_csvToArray2d(self):
        csvArray = Parser.csvToArray2d(TEST_CSV_PATH)
        self.assertEqual(len(csvArray), 3)

    def test_getResizedImageFromCSV(self):
        image = Parser.getResizedImageFromCSV(TEST_CSV_PATH)
        self.assertEqual(image.height, 3)
        self.assertEqual(image.width, TARGET_WIDTH)

if __name__ == '__main__':
    unittest.main()
