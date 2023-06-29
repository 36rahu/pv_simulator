import unittest
from datetime import datetime
from unittest.mock import patch
from module.simulator import PVSimulator


class TestPVSimulator(unittest.TestCase):

    @patch('module.simulator.datetime')
    def test_pv_value_and_ts_during_daytime(self, mock_datetime):
        # Mock the current time to be 10:30 AM
        mock_now = datetime(2023, 1, 1, 10, 30, 0)
        mock_datetime.now.return_value = mock_now

        pv_simulator = PVSimulator()
        pv_value, ts = pv_simulator.pv_value_and_ts()

        self.assertEqual(pv_value, 1.97)

    @patch('module.simulator.datetime')
    def test_pv_value_and_ts_before_daytime(self, mock_datetime):
        # Mock the current time to be 3:00 AM
        mock_now = datetime(2023, 1, 1, 3, 0, 0)
        mock_datetime.now.return_value = mock_now

        pv_simulator = PVSimulator()
        pv_value, ts = pv_simulator.pv_value_and_ts()

        self.assertEqual(pv_value, 0)

    @patch('module.simulator.datetime')
    def test_pv_value_and_ts_after_daytime(self, mock_datetime):
        # Mock the current time to be 14:15 PM
        mock_now = datetime(2023, 1, 1, 14, 15, 0)
        mock_datetime.now.return_value = mock_now

        pv_simulator = PVSimulator()
        pv_value, ts = pv_simulator.pv_value_and_ts()

        self.assertEqual(pv_value, 3.485)

    @patch('module.simulator.datetime')
    def test_pv_value_and_ts_after_daytime(self, mock_datetime):
        # Mock the current time to be 16:56 PM
        mock_now = datetime(2023, 1, 1, 16, 56, 0)
        mock_datetime.now.return_value = mock_now

        pv_simulator = PVSimulator()
        pv_value, ts = pv_simulator.pv_value_and_ts()

        self.assertEqual(pv_value, 2.944)


if __name__ == '__main__':
    unittest.main()
