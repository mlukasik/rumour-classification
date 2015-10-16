'''
Copyright (c) 2014-2015, The University of Sheffield. 
This file is part of the SDQ rumour classification software 
(see https://github.com/mlukasik/rumour-classification), 
and is free software, licenced under the GNU Library General Public License,
Version 2, June 1991 (in the distribution as file LICENSE).

Created on 14 May 2015

@author: michal
'''
import numpy as np

def foldsplitter(X, POSTPROCESSED_TASK_COLUMN_ID, train_set_sizes):
    '''
    For each task id (in column POSTPROCESSED_TASK_COLUMN_ID) make the following split into 
    testing and training parts:
    - take rows starting from train_set_sizes for testing, 
    - take all other rows for training (so training consists of both other task ids and of 
    rows from the same task id up to number train_set_sizes-1).
    
    TESTED - see tests package
    '''
    folds=sorted(list(set(X[:, POSTPROCESSED_TASK_COLUMN_ID])))
    for fold in folds:
        for train_set_size in train_set_sizes:
            testfold2train=X[:, POSTPROCESSED_TASK_COLUMN_ID]==fold
            cnt=0
            for i, _ in enumerate(testfold2train):
                if testfold2train[i]:
                    cnt+=1
                    if cnt>train_set_size:
                        testfold2train[i]=False
            remaining_train=X[:, POSTPROCESSED_TASK_COLUMN_ID]!=fold
            x=np.logical_or.reduce([testfold2train,remaining_train])
            yield x, np.logical_not(x)

def load_data(fname, labels_to_keep=None):
    '''
    Load data from a csv file.
    '''
    X=np.loadtxt(fname, skiprows=1)
    header=open(fname).readline().split()
    #assuming label is the last column
    Xprocessed=X[:,:-1]
    headerprocessed=header[:-1]
    y=X[:, -1]
    if labels_to_keep!=None:
        Xprocessed=Xprocessed[np.logical_or.reduce([y==lbl for lbl in labels_to_keep]), :]
        y=y[np.logical_or.reduce([y==lbl for lbl in labels_to_keep])]
    return Xprocessed, y, headerprocessed