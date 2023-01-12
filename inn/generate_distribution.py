import random
import sys

n = int(sys.argv[1])

distribution = []

for i in range(n):
	distribution.append(random.uniform(0, 1))


s = sum(distribution)
for i in range(n):
	distribution[i] /= s

for i in distribution:
    print(i)

print('Sum is: {}'.format(sum(distribution)))
