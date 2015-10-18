'''
Copyright (c) 2014-2015, The University of Sheffield. 
This file is part of the SDQ rumour classification software 
(see https://github.com/mlukasik/rumour-classification), 
and is free software, licenced under the GNU Library General Public License,
Version 2, June 1991 (in the distribution as file LICENSE).

Created on 4 Feb 2015

@author: michal
'''
import sklearn.metrics
from main.util.constants import LABELS
def print_metrics_multiclass(true, predicted):
    acc = sklearn.metrics.accuracy_score(true, predicted)
    print "accuracy:", acc
    print "Confusion matrix:"
    print sklearn.metrics.confusion_matrix(true, predicted, labels=LABELS)

def filter_methods(methodnames_in, methods_in, methodnames):
    methodsmultitask=[]
    methodnamesmultitask=[]
    for methodname in methodnames.split(","):
        try:
            ind = methodnames_in.index(methodname)
            methodsmultitask += [methods_in[ind]]
            methodnamesmultitask += [methodnames_in[ind]]
        except:
            pass
    return methodnamesmultitask, methodsmultitask