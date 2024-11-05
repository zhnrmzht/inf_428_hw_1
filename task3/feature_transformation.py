import math
import unittest

def time_to_cyclic_features(hour: int) -> float:
    angle = (2 * math.pi * hour) / 24
    return math.sin(angle), math.cos(angle)

def cyclic_time_difference(hour1: int, hour2: int) -> float:
    sin1, cos1 = time_to_cyclic_features(hour1)
    sin2, cos2 = time_to_cyclic_features(hour2)
    return math.acos(sin1 * sin2 + cos1 * cos2) * (24 / (2 * math.pi))

class TestCyclicTime(unittest.TestCase):
    def test_midnight_and_noon(self):
        self.assertAlmostEqual(cyclic_time_difference(0, 12), 12, delta=0.1)

    def test_evening_to_morning(self):
        self.assertAlmostEqual(cyclic_time_difference(23, 1), 2, delta=0.1)

    def test_same_time(self):
        self.assertAlmostEqual(cyclic_time_difference(8, 8), 0, delta=0.1)

    def test_across_noon(self):
        self.assertAlmostEqual(cyclic_time_difference(22, 10), 12, delta=0.1)

if __name__ == '__main__':
    unittest.main()