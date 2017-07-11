import unittest

import numpy as np

import GOL_LC


class TestAlive(unittest.TestCase):
    def setUp(self):
        self.blip = np.zeros((5,5))
        self.blip[1,2] = 1
        self.blip[2,2] = 1
        self.blip[3,2] = 1

    # TODO: Verify which rule this is.
    def test_alive_rule_2(self):
        result = GOL_LC.alive(1, 2, self.blip)
        self.assertEqual(result, False)

    # TODO: Verify which rule this is.
    def test_alive_rule_3(self):
        result = GOL_LC.alive(2, 2, self.blip)
        self.assertEqual(result, True)

    # TODO: Verify which rule this is.
    def test_alive_rule_4(self):
        result = GOL_LC.alive(2, 1, self.blip)
        self.assertEqual(result, True)

    # TODO: Verify which rule this is.
    def test_alive_rule_5(self):
        result = GOL_LC.alive(1, 3, self.blip)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()