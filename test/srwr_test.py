#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import scipy.io as sio
import numpy as np
from srwr.srwr import SRWR


class SRWRTest(unittest.TestCase):
    def setUp(self):
        self.c = 0.15
        self.epsilon = 1e-9
        self.gamma = 1.0
        self.beta = 1.0
        self.max_iters = 300
        self.handles_deadend = True
        self.verbose = False

    def __test_testcase(self, testcase):
        test_data_path = "data/sample-{:02d}.tsv".format(testcase)
        test_case_home = "data/testcases-{:02d}".format(testcase)
        srwr = SRWR()
        srwr.read_graph(test_data_path)
        srwr.normalize()
        n = srwr.A.shape[0] + 1
        for seed in range(1, n):
            mat_file_path = "{}/seed-{}.mat".format(test_case_home, seed)
            testcase = sio.loadmat(mat_file_path)
            mat_r = testcase['r']
            mat_rp = testcase['rp']
            mat_rn = testcase['rn']

            py_r, py_rp, py_rn, _ = srwr.query(seed,
                                               self.c,
                                               self.epsilon,
                                               self.beta,
                                               self.gamma,
                                               self.max_iters,
                                               self.handles_deadend,
                                               self.verbose)

            with self.subTest(seed = seed):
                error_r = np.linalg.norm(mat_r - py_r, 1)
                error_rp = np.linalg.norm(mat_rp - py_rp, 1)
                error_rn = np.linalg.norm(mat_rn - py_rn, 1)
                self.assertAlmostEqual(error_r, 0.0)
                self.assertAlmostEqual(error_rp, 0.0)
                self.assertAlmostEqual(error_rn, 0.0)

    def test_testcases_01(self):
        self.__test_testcase(1)

    def test_testcases_02(self):
        self.__test_testcase(2)


if __name__ == '__main__':
    unittest.main()
