import sys

tol = 1e-5

if len(sys.argv) != 3:
    print('Usage: python create_users_file.py <apriori-file> <num-iterations>')
    sys.exit()

#apriori-file
try:
    apriori_file = open(sys.argv[1])

    apriori = []
    for line in apriori_file:
        p = float(line)
        if p < 0 or p > 1:
            raise Exception('probabilities must be in [0,1]')
        apriori.append(p)

    apriori_file.close()

    s = sum(apriori)
    if abs(s-1) > tol:
        raise Exception('probabilities must sum to 1')
except Exception as e:
    print('apriori-file: '+str(e))
    sys.exit()

#num_iterations
try:
    num_iterations = int(sys.argv[2])
    if num_iterations <= 0:
        raise Exception('the number of iterations must be a positive integer')
except Exception as e:
    print('num_iterations')
    sys.exit()

#Create users-file
for i, f in enumerate(apriori):
    n = int(num_iterations*f)
    for j in range(n):
        print(i)
