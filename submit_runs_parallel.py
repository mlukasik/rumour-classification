'''
Copyright (c) 2014-2015, The University of Sheffield. 
This file is part of the SDQ rumour classification software 
(see https://github.com/mlukasik/rumour-classification), 
and is free software, licenced under the GNU Library General Public License,
Version 2, June 1991 (in the distribution as file LICENSE).

Created on 23 Mar 2015

@author: michal

Submitting jobs for different folds. Useful when running experiments in parallel.
Encoded information specific to a server used for parallelization:
University of Sheffield, Iceberg server.
'''
import sys
import os
from main.models.methods import get_allmethodnames
from subprocess import Popen, PIPE, STDOUT
import time
from main.util.seeds_emnlp2015 import getseed

SCRIPT_NAME="tmp.sh"
SCRIPT_HEADER="\n".join(["#!/bin/bash",
                       "#$ -l h_rt=6:00:00",
                       "#$ -o result.log",
                       "#$ -j y",
                       "#$-l mem=10G", 
                       "#$-l rmem=10G"])
OUTCAT="results"

cvfolds = sys.argv[1]
fname = sys.argv[2]
random_restarts = sys.argv[3]
train_set_ratios = sys.argv[4].split(",")
filter_retweets=sys.argv[5]
methodnames = get_allmethodnames()

global_parameters=[fname, random_restarts, filter_retweets]
for foldrun in xrange(int(cvfolds)):
    for methodname in methodnames:
        for train_set_ratio in train_set_ratios:
            run_parameters=[str(foldrun), methodname, train_set_ratio]
            seed=getseed(*run_parameters)
            with open(SCRIPT_NAME, 'w') as f:
                f.write(SCRIPT_HEADER+"\n")
                res_fname=os.path.join(OUTCAT,"_".join(run_parameters))
                if seed==None:
                    f.write(" ".join(["python", "run.py"]+run_parameters+global_parameters+[">"]+[res_fname]))
                else:
                    f.write(" ".join(["python", "run.py"]+run_parameters+global_parameters+[str(seed), ">"]+[res_fname]))
            cmd="qsub {}".format(SCRIPT_NAME)
            print "Submitting job with parameters: ", " ".join(run_parameters)
            Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT).communicate()[0]
            time.sleep(0.02)