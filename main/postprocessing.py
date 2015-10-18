'''
Copyright (c) 2014-2015, The University of Sheffield. 
This file is part of the SDQ rumour classification software 
(see https://github.com/mlukasik/rumour-classification), 
and is free software, licenced under the GNU Library General Public License,
Version 2, June 1991 (in the distribution as file LICENSE).

Created on 25 May 2015

@author: michal
'''
import numpy as np
import sklearn.metrics

def metric_fixed_testset(a, b, train_perc, max_train):
    '''
    Find accuracy score for labels a and b only caring about
    what happens starting from max_train-train_perc.
    This is because we want to test methods on the same
    test set, but they have varying training sets.
    '''
    start_index=max_train-train_perc
    return sklearn.metrics.accuracy_score(a[start_index:], b[start_index:])

def apply_metric_results(results, metric):
    '''
    Process results - overwrite their old content by
    the mean 'metric' value over the old content. 
    '''
    for method in results.keys():
        max_train=max(results[method].keys())
        for train_perc in sorted(results[method].keys()):
            samples=len(results[method][train_perc])
            metric_val=np.mean([metric(a, b, train_perc=train_perc, max_train=max_train) 
                                for a, b in results[method][train_perc]])
            results[method][train_perc]=(metric_val, samples)

def display_results_table(results):
    for method in results.keys():
        print "method:", method
        for train_perc in sorted(results[method].keys()):
            print train_perc, ":", results[method][train_perc][0], results[method][train_perc][1]