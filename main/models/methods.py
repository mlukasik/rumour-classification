'''
Copyright (c) 2014-2015, The University of Sheffield. 
This file is part of the SDQ rumour classification software 
(see https://github.com/mlukasik/rumour-classification), 
and is free software, licenced under the GNU Library General Public License,
Version 2, June 1991 (in the distribution as file LICENSE).

Created on 8 Apr 2015

@author: michal

Lists of methods for experiments.
'''
from main.models.multiclassgp import MCGP
from sklearn.dummy import DummyClassifier
from main.util.constants import LABELS, extract_feature_indices,\
    TASK_FEATURENAME, IS_SIMPLE_RETWEET_FEATURENAME
from main.models.kernels import single_task_kernel, multi_task_kernel
from main.models.baselines import SklearnBaseline

def get_methods_multitask(tasks_number, header, RANDOM_RESTARTS=-1):
    FEATURES_BOW, FEATURES_BROWN, index_task, _=extract_feature_indices(header)
    
    GPCONSTRUCTOR=lambda kernel_constructor, name, RANDOM_RESTARTS: MCGP(kernel_constructor=kernel_constructor, 
                                                                         labels=LABELS, name=name, RANDOM_RESTARTS=RANDOM_RESTARTS)
    
    METHODSMULTITASK=[
             lambda: SklearnBaseline(lambda: DummyClassifier("most_frequent"), "MostFrequentPooled", [0]),
             lambda: GPCONSTRUCTOR(kernel_constructor=lambda: single_task_kernel(FEATURES_BOW, False, "FEATURES_BOW"), 
                                   name="BOWGPjoinedfeaturesPooledLIN", 
                                   RANDOM_RESTARTS=RANDOM_RESTARTS),
             lambda: GPCONSTRUCTOR(kernel_constructor=lambda: single_task_kernel(FEATURES_BROWN, False, "FEATURES_BROWN"), 
                                   name="BROWNGPjoinedfeaturesPooledLIN", 
                                   RANDOM_RESTARTS=RANDOM_RESTARTS),
             lambda: GPCONSTRUCTOR(kernel_constructor=lambda: multi_task_kernel(tasks_number, index_task, 
                                                                                single_task_kernel(FEATURES_BROWN, False, "FEATURES_BROWN")), 
                                                                                name="BROWNGPjoinedfeaturesICMLIN", RANDOM_RESTARTS=RANDOM_RESTARTS),
             lambda: GPCONSTRUCTOR(kernel_constructor=lambda: multi_task_kernel(tasks_number, index_task, 
                                                                                single_task_kernel(FEATURES_BOW, False, "FEATURES_BOW")), 
                                                                                name="BOWGPjoinedfeaturesICMLIN", RANDOM_RESTARTS=RANDOM_RESTARTS),
             ]
    return METHODSMULTITASK, map(lambda x: x().name, METHODSMULTITASK)

def get_methods_singletask(header, RANDOM_RESTARTS=-1):
    FEATURES_BOW, FEATURES_BROWN, _, _=extract_feature_indices(header)
    GPCONSTRUCTOR=lambda kernel_constructor, name, RANDOM_RESTARTS: MCGP(kernel_constructor=kernel_constructor, labels=LABELS,
                                                                         name=name, RANDOM_RESTARTS=RANDOM_RESTARTS)
        
    METHODSMULTITASK=[
             lambda: SklearnBaseline(lambda: DummyClassifier("most_frequent"), "MostFrequent", [0]),
             lambda: GPCONSTRUCTOR(kernel_constructor=lambda: single_task_kernel(FEATURES_BOW, False, "BOW"), 
                                   name="BOWGPjoinedfeatures", 
                                   RANDOM_RESTARTS=RANDOM_RESTARTS),
             lambda: GPCONSTRUCTOR(kernel_constructor=lambda: single_task_kernel(FEATURES_BROWN, False, "BROWN"), 
                                   name="BROWNGPjoinedfeatures", 
                                   RANDOM_RESTARTS=RANDOM_RESTARTS)
             ]
    return METHODSMULTITASK, map(lambda x: x().name, METHODSMULTITASK)

def get_allmethodnames():
    tasks_number=1
    header=[TASK_FEATURENAME, IS_SIMPLE_RETWEET_FEATURENAME]
    _, NAMES1 = get_methods_multitask(tasks_number, header)
    _, NAMES2 = get_methods_singletask(header)
    return NAMES1+NAMES2
