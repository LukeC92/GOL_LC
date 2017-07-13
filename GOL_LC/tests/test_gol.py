import unittest

import numpy as np
from numpy.testing import assert_array_equal
import GOL_LC


class TestAlive(unittest.TestCase):
    def setUp(self):
        self.blip = np.zeros((5,5))
        self.blip[1,2] = 1
        self.blip[2,2] = 1
        self.blip[3,2] = 1
        
        self.full = np.ones((5,5))

    def test_alive_rule_1(self):
        result = GOL_LC.alive(1, 2, self.blip)
        self.assertEqual(result, False)

    def test_alive_rule_2(self):
        result = GOL_LC.alive(2, 2, self.blip)
        self.assertEqual(result, True)
        
    def test_alive_rule_3(self):
        result = GOL_LC.alive(0,1,self.full)
        self.assertEqual(result, False)

    def test_alive_rule_4(self):
        result = GOL_LC.alive(2, 1, self.blip)
        self.assertEqual(result, True)

    def test_alive_rule_not_4(self):
        result = GOL_LC.alive(1, 3, self.blip)
        self.assertEqual(result, False)


class TestSum(unittest.TestCase):  

    def setUp(self):
        self.blip = np.zeros((5,5))
        self.blip[1,2] = 1
        self.blip[2,2] = 1
        self.blip[3,2] = 1
        
        self.full = np.ones((5,5))
 
    def test_sum_rule_1(self):
        result = GOL_LC.sumcells(1, 2, self.blip)
        self.assertEqual(result, 1)

    def test_sum_rule_2(self):
        result = GOL_LC.sumcells(2, 2, self.blip)
        self.assertEqual(result, 2)

    def test_sum_rule_3(self):
        result = GOL_LC.sumcells(0,1,self.full)
        self.assertEqual(result, 5)

    def test_sum_rule_4(self):
        result = GOL_LC.sumcells(2, 1, self.blip)
        self.assertEqual(result, 3)

    def test_sum_rule_not_4(self):
        result = GOL_LC.sumcells(1, 3, self.blip)
        self.assertEqual(result, 2)


class TestUpdate(unittest.TestCase):  

    def setUp(self):
        self.blip = np.zeros((5,5))
        self.blip[1,2] = 1
        self.blip[2,2] = 1
        self.blip[3,2] = 1
        self.blip_update = np.zeros((5,5))
        self.blip_update[2,1] = 1
        self.blip_update[2,2] = 1
        self.blip_update[2,3] = 1
        self.full = np.ones((5,5))
        self.full_update = np.zeros((5,5))
        self.full_update[0,0]=1
        self.full_update[4,0]=1
        self.full_update[0,4]=1
        self.full_update[4,4]=1
        self.dead = np.zeros((5,5))

#        print('here')
#        print(self.blip_update)
#        print('second')
#        print(GOL_LC.update(self.blip))
 
    def test_blip_update(self):
        result = GOL_LC.update(self.blip)
        assert_array_equal(result, self.blip_update)
        
    def test_blip_update_2(self):
        result = GOL_LC.update(GOL_LC.update(self.blip))
        assert_array_equal(result, self.blip)

    def test_full_update(self):
        result = GOL_LC.update(self.full)
        assert_array_equal(result, self.full_update)

    def test_full_update_2(self):
        result = GOL_LC.update(GOL_LC.update(self.full))
        assert_array_equal(result, self.dead)
        
    def test_dead_update(self):
        result = GOL_LC.update(self.dead)
        assert_array_equal(result, self.dead)

if __name__ == '__main__':
    unittest.main()
