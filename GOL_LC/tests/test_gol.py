import unittest

import numpy as np
from numpy.testing import assert_array_equal
import GOL_LC

def makearrays(self):
    self.blinker = np.zeros((5,5))
    self.blinker[1:4,2] = 1
    self.full = np.ones((5,5))
    self.blinker_update = np.zeros((5,5))
    self.blinker_update[2,1:4] = 1
    self.full_update = np.zeros((5,5))
    self.full_update[0,0]=1
    self.full_update[4,0]=1
    self.full_update[0,4]=1
    self.full_update[4,4]=1
    self.dead = np.zeros((5,5))

class TestAlive(unittest.TestCase):
    def setUp(self):
        makearrays(self)

    def test_alive_rule_1(self):
        result = GOL_LC.alive(1, 2, self.blinker)
        self.assertEqual(result, False)

    def test_alive_rule_2(self):
        result = GOL_LC.alive(2, 2, self.blinker)
        self.assertEqual(result, True)
        
    def test_alive_rule_3(self):
        result = GOL_LC.alive(0,1,self.full)
        self.assertEqual(result, False)

    def test_alive_rule_4(self):
        result = GOL_LC.alive(2, 1, self.blinker)
        self.assertEqual(result, True)

    def test_alive_rule_not_4(self):
        result = GOL_LC.alive(1, 3, self.blinker)
        self.assertEqual(result, False)




class TestSum(unittest.TestCase):  

    def setUp(self):
        makearrays(self)
 
    def test_sum_rule_1(self):
        result = GOL_LC.sumcells(1, 2, self.blinker)
        self.assertEqual(result, 1)

    def test_sum_rule_2(self):
        result = GOL_LC.sumcells(2, 2, self.blinker)
        self.assertEqual(result, 2)

    def test_sum_rule_3(self):
        result = GOL_LC.sumcells(0,1,self.full)
        self.assertEqual(result, 5)

    def test_sum_rule_4(self):
        result = GOL_LC.sumcells(2, 1, self.blinker)
        self.assertEqual(result, 3)

    def test_sum_rule_not_4(self):
        result = GOL_LC.sumcells(1, 3, self.blinker)
        self.assertEqual(result, 2)


class TestNeighbours(unittest.TestCase):
    
    def setUp(self):
        makearrays(self)
        self.blinkerN = np.zeros((5,5))
        self.blinkerN[0,1:4] = 1
        self.blinkerN[4,1:4] = 1
        self.blinkerN[1,1]=2
        self.blinkerN[1,3]=2
        self.blinkerN[2,2]=2
        self.blinkerN[3,1]=2
        self.blinkerN[3,3]=2
        self.blinkerN[2,1]=3
        self.blinkerN[2,3]=3
        self.blinkerN[1,2]=1
        self.blinkerN[3,2]=1
        
        self.blinkerUN = np.array([[ 0,  0,  0,  0,  0,],
                                 [ 1,  2,  3,  2,  1,],
                                 [ 1,  1,  2,  1,  1,],
                                 [ 1,  2,  3,  2,  1,],
                                 [ 0,  0,  0,  0,  0,]])
        
        
        self.fullN = np.array([[ 3,  5,  5,  5,  3,],
                               [ 5,  8,  8,  8,  5,],
                               [ 5,  8,  8,  8,  5,],
                               [ 5,  8,  8,  8,  5,],
                               [ 3,  5,  5,  5,  3,]])
        
        self.fullUN = np.array([[ 0,  1,  0,  1,  0,],
                                [ 1,  1,  0,  1,  1,],
                                [ 0,  0,  0,  0,  0,],
                                [ 1,  1,  0,  1,  1,],
                                [ 0,  1,  0,  1,  0,]])
        
    def test_blinker_neighbour(self):
        result = GOL_LC.neighbours(self.blinker)
        assert_array_equal(result, self.blinkerN)
        
        
    def test_blinker_update_neighbour(self):
        result = GOL_LC.neighbours(self.blinker_update)
        assert_array_equal(result, self.blinkerUN)    
        
    def test_full_neighbour(self):
        result = GOL_LC.neighbours(self.full)
        assert_array_equal(result, self.fullN)   
        
    def test_full_update_neighbour(self):
        result = GOL_LC.neighbours(self.full_update)
        assert_array_equal(result, self.fullUN)              


class TestUpdateM(unittest.TestCase):
    def setUp(self):
        makearrays(self)
        
    def test_blinker_updateM(self):
        result = GOL_LC.updateM(self.blinker)
        assert_array_equal(result, self.blinker_update)
        
    def test_blinker_updateM_2(self):
        result = GOL_LC.updateM(GOL_LC.updateM(self.blinker))
        assert_array_equal(result, self.blinker)

    def test_full_updateM(self):
        result = GOL_LC.updateM(self.full)
        assert_array_equal(result, self.full_update)

    def test_full_updateM_2(self):
        result = GOL_LC.updateM(GOL_LC.updateM(self.full))
        assert_array_equal(result, self.dead)
        
    def test_dead_updateM(self):
        result = GOL_LC.updateM(self.dead)
        assert_array_equal(result, self.dead)

class TestUpdate(unittest.TestCase):  

    def setUp(self):
        makearrays(self)
 
    def test_blinker_update(self):
        result = GOL_LC.update(self.blinker)
        assert_array_equal(result, self.blinker_update)
        
    def test_blinker_update_2(self):
        result = GOL_LC.update(GOL_LC.update(self.blinker))
        assert_array_equal(result, self.blinker)

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
