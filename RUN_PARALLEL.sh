#!/bin/bash
# Script for reconstructing experiments for the EMNLP 2015 paper: parallel version
python submit_runs_parallel.py 7 data/londonriots_BOW_BROWN_ANONYMIZED_EMNLP2015.csv -1 0,10,20,30,40,50 1
