'''
Copyright (c) 2014-2015, The University of Sheffield. 
This file is part of the SDQ rumour classification software 
(see https://github.com/mlukasik/rumour-classification), 
and is free software, licenced under the GNU Library General Public License,
Version 2, June 1991 (in the distribution as file LICENSE).

Created on 6 Feb 2015

@author: michal

Main experiment script.
'''
import sys
from main.util.util import initialize_seed_with_currtime 
from main.data import load_data, foldsplitter
from main.experiment import Experiment

import sklearn.metrics
from main.models.util import filter_methods
from main.models.methods import get_methods_multitask,\
    get_methods_singletask
from main.util.constants import LABELS, extract_feature_indices
from main.models.util import print_metrics_multiclass

initialize_seed_with_currtime()

FOLDTORUN=int(sys.argv[1])
methodname=sys.argv[2]
train_set_ratios=[int(sys.argv[3])]
fname=sys.argv[4]
RANDOM_RESTARTS=int(sys.argv[5])
filter_retweets=bool(int(sys.argv[6]))

X, y, header = load_data(fname, labels_to_keep=LABELS)
_, _, POSTPROCESSED_TASK_COLUMN_ID, _=extract_feature_indices(header)
splitter = foldsplitter(X, POSTPROCESSED_TASK_COLUMN_ID, train_set_ratios)
EVALUATION_MEASURES = [sklearn.metrics.accuracy_score]
tasks_number=len(set(X[:, POSTPROCESSED_TASK_COLUMN_ID]))

METHODS, METHODNAMES = get_methods_multitask(tasks_number, header, RANDOM_RESTARTS=RANDOM_RESTARTS)
METHODSSINGLETASK, METHODNAMESSINGLETASK = get_methods_singletask(header, RANDOM_RESTARTS=RANDOM_RESTARTS)

if methodname != None:
    #if we are interested in keeping only one method
    METHODNAMES, METHODS = filter_methods(METHODNAMES, METHODS, methodname)
    METHODNAMESSINGLETASK, METHODSSINGLETASK = filter_methods(METHODNAMESSINGLETASK, METHODSSINGLETASK, methodname)

experiment = Experiment(X, y, train_set_ratios, FOLDTORUN, splitter, EVALUATION_MEASURES, METHODNAMES, METHODS, 
                        METHODNAMESSINGLETASK, METHODSSINGLETASK, print_metrics=print_metrics_multiclass, 
                        RANDOM_RESTARTS=RANDOM_RESTARTS, results={}, header=header, filter_retweets=filter_retweets)
experiment.run()
experiment.summarize()