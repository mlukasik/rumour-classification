'''
Copyright (c) 2014-2015, The University of Sheffield. 
This file is part of the SDQ rumour classification software 
(see https://github.com/mlukasik/rumour-classification), 
and is free software, licenced under the GNU Library General Public License,
Version 2, June 1991 (in the distribution as file LICENSE).

Created on 2 Jun 2015

@author: michal
'''
import GPy
import numpy as np

def single_task_kernel(indices_features, ARD, name):
    active_dims=np.array(indices_features)
    if ARD:
        variances=np.ones_like(active_dims)
    else:
        variances=1
    k1=GPy.kern.Linear(len(indices_features),
                         variances=variances,
                         active_dims=active_dims, 
                         ARD=ARD, name=name)
    
    return k1

def multi_task_kernel(tasks_number, index_task, k1):
    W = np.ones((tasks_number, 1))*0.3
    k2 = GPy.kern.Coregionalize(input_dim=1, output_dim=tasks_number, rank=1, active_dims=index_task, W = W)
    pW =  k2['.*W.*']
    pW.constrain_positive()
    k2['.*kappa.*'] = np.ones_like(k2['.*kappa.*'])*0.9
    
    kernel = k1*k2
    return kernel
