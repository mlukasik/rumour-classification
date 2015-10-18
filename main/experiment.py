'''
Copyright (c) 2014-2015, The University of Sheffield. 
This file is part of the SDQ rumour classification software 
(see https://github.com/mlukasik/rumour-classification), 
and is free software, licenced under the GNU Library General Public License,
Version 2, June 1991 (in the distribution as file LICENSE).

Created on 23 Mar 2015

@author: michal
'''
import numpy as np
from main.util.constants import extract_feature_indices
    
class Experiment(object):
    '''
    Class governing the process of the Classification Experiment.
    '''
    def __init__(self, X, y, train_set_ratios, foldtorun, splitter, evaluation_measures, 
                 methodnamesmultitask, methodsmultitask, methodnamessingletask, methodssingletask, print_metrics,
                 header, random_restarts=-1, results={}, filter_retweets=True):
        self.X = X
        self.y = y
        self.methodnamesmultitask = methodnamesmultitask
        self.methodsmultitask = methodsmultitask
        self.methodnamessingletask = methodnamessingletask
        self.methodssingletask = methodssingletask
        self.foldtorun = foldtorun
        self.splitter = splitter
        self.evaluation_measures=evaluation_measures
        self.print_metrics = print_metrics
        self.results = results
        self.header=header
        _, _, self.postprocessed_task_column_id, self.rttypecol_processed_column_id=extract_feature_indices(header)
        self.methodnames_all = self.methodnamesmultitask+self.methodnamessingletask
        self.filter_retweets = filter_retweets

    def run(self):
        for foldind, (train, test) in enumerate(self.splitter):
            if self.foldtorun==-1 or self.foldtorun==foldind:
                
                settings_dict={}
                settings_dict['multitask']=(self.X[train, :], self.X[test, :], self.y[train], self.y[test], 
                            self.methodnamesmultitask, 
                            self.methodsmultitask)
                settings_dict['singletask']=(self.X[train, :][self.X[train][:,self.postprocessed_task_column_id]==
                                              self.X[test, :][0,self.postprocessed_task_column_id]], 
                             self.X[test, :], 
                             self.y[train][self.X[train, :][:,self.postprocessed_task_column_id]==
                                           self.X[test, :][0,self.postprocessed_task_column_id]], 
                             self.y[test],
                             self.methodnamessingletask, 
                             self.methodssingletask)
                
                for v in settings_dict.values():
                    x_train, x_test, y_train, y_test, methodnamesmultitask, methodsmultitask = v
                    if self.filter_retweets:
                        #filtering out simple rt
                        y_train=y_train[x_train[:, self.rttypecol_processed_column_id]!=1]
                        x_train=x_train[x_train[:, self.rttypecol_processed_column_id]!=1, :]
                    for methodname, method_constructor in zip(methodnamesmultitask, methodsmultitask):
                        method = method_constructor()
                        result = self.evaluate_method(x_train, x_test, y_train, y_test, method, 
                                                      summarize_kernel=False)
                        self.results[methodname] = self.results.get(methodname, [])+[result]

    def evaluate_method(self, x_train, x_test, y_train, y_test, method, summarize_kernel):
        method.fit(x_train, y_train)
        y_mean = method.predict(x_test)
        print "y_predicted:"+",".join(map(str, y_mean))
        print "y_true:"+",".join(map(str, y_test))
        self.print_metrics(y_test, y_mean)
        results=[evaluation_measure(y_test, y_mean) for evaluation_measure in self.evaluation_measures]
        return results
    
    def summarize(self):
        print "[Experiment.summarize]"
        print "method", "mean", "std", "sample"
        import sys
        print >> sys.stderr, "foldtorun: "+str(self.foldtorun)+":"+str(self.results)
        for ind, _ in enumerate(self.evaluation_measures):
            for key in self.methodnames_all:
                value = map(lambda x: x[ind], self.results[key])
                print key, np.mean(value), np.std(value), len(value)