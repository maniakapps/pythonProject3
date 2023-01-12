import sys
import csv

#the output of the simulation
simulation_out = open(sys.argv[1])
#the corresponding users_file that produced the result above
users_file = open(sys.argv[2])
#the name of the csv file to direct the output
fbleau_input = sys.argv[3]

#build a dictionary based on the unique values
d = {}

with open(fbleau_input, mode='w') as f_input:
    csv_writer = csv.writer(f_input, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for sender, out in zip(users_file, simulation_out):
        sender = sender[:-1]
        key = tuple(out.split())
        if key not in d:
            d[key] = len(d)
        csv_writer.writerow([sender, d[key]])
