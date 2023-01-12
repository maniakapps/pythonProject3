import sys
import csv
from random import uniform

assert len(sys.argv) == 4, 'Usage: python generate_fbleau_input.py <mapped.csv> <train.csv> <test.csv> (use your own custom names for the last 2).'
mapped = sys.argv[1]
train = sys.argv[2]
test = sys.argv[3]

mapped_csv = open(mapped)
train_csv = open(train, 'w')
test_csv = open(test, 'w')

for line in mapped_csv:
	if(uniform(0,1) < 0.8):
		train_csv.write(line)
	else:
		test_csv.write(line)

mapped_csv.close()
train_csv.close()
test_csv.close()