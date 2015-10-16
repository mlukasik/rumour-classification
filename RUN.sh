#!/bin/bash
# Script for reconstructing experiments for the EMNLP 2015 paper.

mkdir results
METHODS0=("MostFrequentPooled" "BOWGPjoinedfeaturesPooledLIN" "BROWNGPjoinedfeaturesPooledLIN")
for FOLDTORUN in {0..6}; 
do 
	for METHOD in ${METHODS0[*]}
	do
		echo "Running fold "$FOLDTORUN" METHOD "$METHOD" with training data range 0"
		python run.py $FOLDTORUN $METHOD 0 data/londonriots_BOW_BROWN_ANONYMIZED_EMNLP2015.csv -1 1 > results/$FOLDTORUN"_"$METHOD"_0"
	done
done
METHODSMOREDATA=("MostFrequent" "BOWGPjoinedfeaturesPooledLIN" "BROWNGPjoinedfeaturesPooledLIN" "BOWGPjoinedfeatures" "BROWNGPjoinedfeatures" "BROWNGPjoinedfeaturesICMLIN" "BOWGPjoinedfeaturesICMLIN")
for FOLDTORUN in {0..6}; 
do 
	for METHOD in ${METHODSMOREDATA[*]}
	do
		for TRAININGDATASIZE in 10 20 30 40 50
		do
			echo "Running fold "$FOLDTORUN" METHOD "$METHOD" with training data range "$TRAININGDATASIZE
			python run.py $FOLDTORUN $METHOD $TRAININGDATASIZE data/londonriots_BOW_BROWN_ANONYMIZED_EMNLP2015.csv -1 1 > results/$FOLDTORUN"_"$METHOD"_"$TRAININGDATASIZE
		done
	done
done

#analyze results
python gather_results.py results
