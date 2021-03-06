from hindemith.types.common import Array

__author__ = 'leonardtruong'

import unittest
import numpy as np

from hindemith.operations.optical_flow.pyr_up import PyrUp

class TestPyrUp(unittest.TestCase):
    def test_simple_pyr_up(self):
        specialized = PyrUp()
        python = PyrUp(pure_python=True)
        rand_arr = Array('testArr', np.random.rand(60, 80).astype(np.float32) * 100)
        actual = specialized(rand_arr)
        expected = python(rand_arr)
        try:
            np.testing.assert_array_almost_equal(actual.data, expected.data, decimal=3)
        except AssertionError as e:
            self.fail("Outputs not equal: %s" % e.message)

