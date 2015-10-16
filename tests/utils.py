'''
Copyright (c) 2014-2015, The University of Sheffield. 
This file is part of the SDQ rumour classification software 
(see https://github.com/mlukasik/rumour-classification), 
and is free software, licenced under the GNU Library General Public License,
Version 2, June 1991 (in the distribution as file license.html).

Created on 8 Apr 2015

@author: michal
'''
import unittest
import numpy as np
from main.data import foldsplitter

class Test(unittest.TestCase):


    def test_foldsplitter(self):
        taskids=np.array([0 for _ in range(6)]+[1 for _ in range(6)])
        times=np.array(range(6)+range(6))
        X=np.transpose(np.vstack((times, taskids)))
        np.testing.assert_array_equal(list(foldsplitter(X, -1, [1, 2])), 
                                      [(np.array([ True, False, False, False, False, False,  True,  True,  True,
                                                  True,  True,  True], dtype=bool), 
                                        np.array([False,  True,  True,  True,  True,  True, False, False, False,
                                                  False, False, False], dtype=bool)), 
                                       (np.array([ True,  True, False, False, False, False,  True,  True,  True,
                                                  True,  True,  True], dtype=bool), 
                                        np.array([False, False,  True,  True,  True,  True, False, False, False,
                                                  False, False, False], dtype=bool)), 
                                       (np.array([ True,  True,  True,  True,  True,  True,  True, False, False,
                                                  False, False, False], dtype=bool), 
                                        np.array([False, False, False, False, False, False, False,  True,  True,
                                                  True,  True,  True], dtype=bool)), 
                                       (np.array([ True,  True,  True,  True,  True,  True,  True,  True, False,
                                                  False, False, False], dtype=bool), 
                                        np.array([False, False, False, False, False, False, False, False,  True,
                                                  True,  True,  True], dtype=bool))])
if __name__ == "__main__":
    unittest.main()