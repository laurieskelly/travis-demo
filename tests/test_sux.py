import unittest
import sunshine

class SunshineTest(unittest.TestCase):

    def test_sun_actions(self):
        self.assertIn('incinerates',sunshine.Sunshine.get_sunshine_action)
