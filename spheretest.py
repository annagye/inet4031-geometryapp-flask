import unittest
import sphere
import math

class sphereTest(unittest.TestCase):

    # Test 1: radius = 1
    def test_volume1(self):
        self.assertAlmostEqual(sphere.volume(1), (4/3) * math.pi * 1**3)

    # Test 2: radius = 3
    def test_volume2(self):
        self.assertAlmostEqual(sphere.volume(3), (4/3) * math.pi * 27)

    # Test 3: radius = 10
    def test_volume3(self):
        self.assertAlmostEqual(sphere.volume(10), (4/3) * math.pi * 1000)

if __name__ == '__main__':
    unittest.main()