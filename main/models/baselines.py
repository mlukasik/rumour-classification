'''
Copyright (c) 2014-2015, The University of Sheffield. 
This file is part of the SDQ rumour classification software 
(see https://github.com/mlukasik/rumour-classification), 
and is free software, licenced under the GNU Library General Public License,
Version 2, June 1991 (in the distribution as file license.html).

Created on 16 May 2015

@author: michal
'''
class SklearnBaseline(object):
    def __init__(self, cls, name, features):
        self.name=name
        self.features=features
        self.m=cls()
    def predict(self, x):
        return self.m.predict(x[:, self.features])
    def fit(self, X, y):
        return self.m.fit(X[:, self.features], y)