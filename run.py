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

foldtorun=int(sys.argv[1])
methodname=sys.argv[2]
train_set_ratios=[int(sys.argv[3])]
fname=sys.argv[4]
random_restarts=int(sys.argv[5])
filter_retweets=bool(int(sys.argv[6]))
if len(sys.argv)>=8:
    #if random number generator seed has been passed
    seed=int(sys.argv[7])
    import numpy as np
    np.random.seed(seed)
else:
    initialize_seed_with_currtime()

X, y, header = load_data(fname, labels_to_keep=LABELS)
_, _, postprocessed_task_column_id, _=extract_feature_indices(header)
splitter = foldsplitter(X, postprocessed_task_column_id, train_set_ratios)
evaluation_measures = [sklearn.metrics.accuracy_score]
tasks_number=len(set(X[:, postprocessed_task_column_id]))

methodsmultitask, methodnamesmultitask = get_methods_multitask(tasks_number, header, random_restarts=random_restarts)
methodssingletask, methodnamessingletask = get_methods_singletask(header, random_restarts=random_restarts)

if methodname != None:
    #if we are interested in keeping only one method
    methodnamesmultitask, methodsmultitask = filter_methods(methodnamesmultitask, methodsmultitask, methodname)
    methodnamessingletask, methodssingletask = filter_methods(methodnamessingletask, methodssingletask, methodname)

experiment = Experiment(X, y, train_set_ratios, foldtorun, splitter, evaluation_measures, methodnamesmultitask, methodsmultitask, 
                        methodnamessingletask, methodssingletask, print_metrics=print_metrics_multiclass, 
                        random_restarts=random_restarts, results={}, header=header, filter_retweets=filter_retweets)
experiment.run()
experiment.summarize()