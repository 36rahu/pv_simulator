import unittest
from unittest.mock import patch
from module.meter import Meter


class TestMeter(unittest.TestCase):

    def setUp(self):
        self.meter = Meter()

    def test_generate_value(self):
        with patch('random.uniform', return_value=5.6789):
            result = self.meter.generate_value()
            self.assertIsInstance(result, dict)
            self.assertIn("consumption", result)
            self.assertEqual(result["consumption"], 5.6789)


if __name__ == '__main__':
    unittest.main()
