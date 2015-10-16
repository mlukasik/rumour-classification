'''
Copyright (c) 2014-2015, The University of Sheffield. 
This file is part of the SDQ rumour classification software 
(see https://github.com/mlukasik/rumour-classification), 
and is free software, licenced under the GNU Library General Public License,
Version 2, June 1991 (in the distribution as file LICENSE).

Created on 15 Feb 2015

@author: michal

Gathering results from the result text files.
'''
import sys
from os import listdir
from os.path import join
from main.postprocessing import display_results_table, apply_metric_results, metric_fixed_testset

METRIC=metric_fixed_testset
if __name__=="__main__":
    experiment_dir=sys.argv[1]
    results = {}
    method2foldresults = {}
    for fname_short in listdir(experiment_dir):
        fname = join(experiment_dir,fname_short)
        _, method, train_perc=fname_short.split("_")
        train_perc=int(train_perc)
        
        ypred=None
        ytrue=None
        with open(fname) as f:
            for l in f:
                if 'y_predicted' in l:
                    ypred=map(int, l.replace('y_predicted:', '').strip().replace('.0', '').split(','))
                if 'y_true' in l:
                    ytrue=map(int, l.replace('y_true:', '').strip().replace('.0', '').split(','))
    
        if ypred==None or ytrue==None:
            print "Problem with parsing:", fname
        else:
            results[method]=results.get(method, {})
            results[method][train_perc]=results[method].get(train_perc, [])+[(ypred, ytrue)]
            
    apply_metric_results(results, METRIC)
    display_results_table(results)