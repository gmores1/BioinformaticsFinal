#!/bin/bash
echo "Do you want to enter your own values? [y/n]"
read userChoice
if [[ $userChoice == 'n' ]]
then
	python gmores1_BioinfoFinal.py
else
	echo "Enter the population, birth rate, and death rate for orcas, seals, and penguins in that order. Then set your timestep and max time for running the simulation."
	read sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11]
	python gmores1_BioinfoFinal.py sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11]
fi