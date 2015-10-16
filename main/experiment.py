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
    def __init__(self, X, y, train_set_ratios, FOLDTORUN, splitter, EVALUATION_MEASURES, 
                 METHODNAMESMULTITASK, METHODSMULTITASK, METHODNAMESSINGLETASK, METHODSSINGLETASK, print_metrics,
                 header, RANDOM_RESTARTS=-1, results={}, filter_retweets=True):
        self.X = X
        self.y = y
        self.METHODNAMESMULTITASK = METHODNAMESMULTITASK
        self.METHODSMULTITASK = METHODSMULTITASK
        self.METHODNAMESSINGLETASK = METHODNAMESSINGLETASK
        self.METHODSSINGLETASK = METHODSSINGLETASK
        self.FOLDTORUN = FOLDTORUN
        self.splitter = splitter
        self.EVALUATION_MEASURES=EVALUATION_MEASURES
        self.print_metrics = print_metrics
        self.results = results
        self.header=header
        _, _, self.POSTPROCESSED_TASK_COLUMN_ID, self.RTTYPECOL_PROCESSED_COLUMN_ID=extract_feature_indices(header)
        self.METHODNAMES_ALL = self.METHODNAMESMULTITASK+self.METHODNAMESSINGLETASK
        self.filter_retweets = filter_retweets

    def run(self):
        for foldind, (train, test) in enumerate(self.splitter):
            if self.FOLDTORUN==-1 or self.FOLDTORUN==foldind:
                
                settings_dict={}
                settings_dict['multitask']=(self.X[train, :], self.X[test, :], self.y[train], self.y[test], 
                            self.METHODNAMESMULTITASK, 
                            self.METHODSMULTITASK)
                settings_dict['singletask']=(self.X[train, :][self.X[train][:,self.POSTPROCESSED_TASK_COLUMN_ID]==
                                              self.X[test, :][0,self.POSTPROCESSED_TASK_COLUMN_ID]], 
                             self.X[test, :], 
                             self.y[train][self.X[train, :][:,self.POSTPROCESSED_TASK_COLUMN_ID]==
                                           self.X[test, :][0,self.POSTPROCESSED_TASK_COLUMN_ID]], 
                             self.y[test],
                             self.METHODNAMESSINGLETASK, 
                             self.METHODSSINGLETASK)
                
                for v in settings_dict.values():
                    X_train, X_test, y_train, y_test, METHODNAMESMULTITASK, METHODSMULTITASK = v
                    if self.filter_retweets:
                        #filtering out simple RT
                        y_train=y_train[X_train[:, self.RTTYPECOL_PROCESSED_COLUMN_ID]!=1]
                        X_train=X_train[X_train[:, self.RTTYPECOL_PROCESSED_COLUMN_ID]!=1, :]
                    for methodname, method_constructor in zip(METHODNAMESMULTITASK, METHODSMULTITASK):
                        method = method_constructor()
                        result = self.evaluate_method(X_train, X_test, y_train, y_test, method, 
                                                      summarize_kernel=False)
                        self.results[methodname] = self.results.get(methodname, [])+[result]

    def evaluate_method(self, X_train, X_test, y_train, y_test, method, summarize_kernel):
        method.fit(X_train, y_train)
        y_mean = method.predict(X_test)
        print "y_predicted:"+",".join(map(str, y_mean))
        print "y_true:"+",".join(map(str, y_test))
        self.print_metrics(y_test, y_mean)
        results=[EVALUATION_MEASURE(y_test, y_mean) for EVALUATION_MEASURE in self.EVALUATION_MEASURES]
        return results
    
    def summarize(self):
        print "[Experiment.summarize]"
        print "method", "mean", "std", "sample"
        import sys
        print >> sys.stderr, "FOLDTORUN: "+str(self.FOLDTORUN)+":"+str(self.results)
        for ind, _ in enumerate(self.EVALUATION_MEASURES):
            for key in self.METHODNAMES_ALL:
                value = map(lambda x: x[ind], self.results[key])
                print key, np.mean(value), np.std(value), len(value)