import unittest
from sunshine import Sunshine

class SunshineTest(unittest.TestCase):

    def setUp(self):
        self.sunshine = Sunshine()

    def runTest(self):
        temperaments = ['benevolent', 'cranky', 'evil']
        self.assertIn(self.sunshine.temperament,temperaments)
