'''
Copyright (c) 2014-2015, The University of Sheffield. 
This file is part of the SDQ rumour classification software 
(see https://github.com/mlukasik/rumour-classification), 
and is free software, licenced under the GNU Library General Public License,
Version 2, June 1991 (in the distribution as file LICENSE).

Created on 13 Mar 2015

@author: michal
'''
import time
import numpy as np
import os
def initialize_seed_with_currtime():
    RANDOM_SEED = np.int(time.time())
    print "[initialize_seed_with_currtime] Initializing RANDOM_SEED to:", RANDOM_SEED
    np.random.seed(RANDOM_SEED)

def make_dir(dir_):
    if not os.path.exists(dir_):
        os.makedirs(dir_) 
        
def current_time_str():
    return time.strftime("%d_%m_%Y_%H_%M_%S")