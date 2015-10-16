'''
Copyright (c) 2014-2015, The University of Sheffield. 
This file is part of the SDQ rumour classification software 
(see https://github.com/mlukasik/rumour-classification), 
and is free software, licenced under the GNU Library General Public License,
Version 2, June 1991 (in the distribution as file LICENSE).

Created on 15 Oct 2015

@author: michal

Script for anonymizing data - replacing BOW and BROWN header 
information with integers and shuffling appropriate columns.
'''
import sys
import numpy as np
from constants import extract_feature_indices
if __name__ == '__main__':
    data_in=sys.argv[1]
    data_out=sys.argv[2]
    
    header=open(data_in).readline().split()
    FEATURES_BOW, FEATURES_BROWN, index_task=extract_feature_indices(header)
    for fbow in FEATURES_BOW:
        header[fbow]="BOW_STR_"+str(fbow)+"_BOW_STR"
    for fbrown in FEATURES_BROWN:
        header[fbrown]="BROWN_"+str(fbrown)+"_BROWN"
    
    X=np.loadtxt(data_in, skiprows=1)
    #permute BOW columns 
    np.random.shuffle(X[:, FEATURES_BOW].T)
    #permute BROWN columns
    np.random.shuffle(X[:, FEATURES_BROWN].T)
    
    DELIMITER=" "
    with open(data_out, 'w') as fout:
        fout.write(DELIMITER.join(map(str, header))+"\n")
        for x in X:
            fout.write(DELIMITER.join(map(lambda x: str(int(x)), x))+"\n")
            