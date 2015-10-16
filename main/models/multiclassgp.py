'''
Copyright (c) 2014-2015, The University of Sheffield. 
This file is part of the SDQ rumour classification software 
(see https://github.com/mlukasik/rumour-classification), 
and is free software, licenced under the GNU Library General Public License,
Version 2, June 1991 (in the distribution as file license.html).

Created on 7 Feb 2015

@author: michal
'''
import GPy
import numpy as np
class MCGP(object):
    '''
    Multi Class Gaussian Process Classifier, implemented as One vs All.
    '''
    def __init__(self, kernel_constructor, labels, name=None, RANDOM_RESTARTS=-1, 
                 optimize=True):
        self.k_constructor = kernel_constructor
        self.name = name
        self.RANDOM_RESTARTS = RANDOM_RESTARTS
        self.optimize = optimize
        
    def fit(self, X, y):
        self.labels = list(set(y.flatten()))
        self.models = {}
        
        for label in self.labels:
            ytmp=y.copy()
            ytmp[ytmp!=label]=0
            ytmp[ytmp==label]=1
            
            m=GPy.models.GPClassification(X, ytmp[:, None], kernel=self.k_constructor())
            
            if self.optimize:
                if self.RANDOM_RESTARTS > 1:
                    m.optimize_restarts(messages=True, robust=True, 
                                        num_restarts=self.RANDOM_RESTARTS)
                else:
                    m.optimize(messages=True)
            self.models[label]=m
        
    def predict(self, X):
        results_dict={}
        for label in self.labels:
            mean, _ = self.models[label].predict(X)
            results_dict[label]=mean
        Y=np.vstack(tuple([results_dict[label].T for label in self.labels]))
        result=map(lambda x: self.labels[x], Y.argmax(0))
        
        return result
    
    def get_params(self, deep=False):
        return self.__dict__