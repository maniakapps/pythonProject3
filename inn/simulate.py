import sys
import crowds

args = sys.argv

if len(args) != 7:
    print('Usage: python3 simulate.py <phi> <graph-file> <corrupted-file> <users-file> <broken-paths> <fix-strategy>')
    sys.exit()

#phi
try:
    phi = float(args[1])
    if phi < 0 or phi >= 1:
        raise Exception('phi must be within (0,1)')
except Exception as e:
    print('phi: ' + str(e))
    sys.exit()

#graph-file
try:
    graph_file = open(args[2])
    
    graph = []
    for i, line in enumerate(graph_file):
        tmp = line.split()
        for j in tmp:
            if j not in ['0', '1']:
                raise Exception('graph-file may only contain 0 or 1 elements. Found '+str(j)+' in line '+str(i))
        graph.append(tmp)
    
    for row in graph:
        if len(row) != len(graph):
            raise Exception('graph-file must be n x n')

    num_users = len(graph)
    graph_file.close()
except Exception as e:
    print('graph-file: ' + str(e))
    sys.exit()


#corrupted-file
try:
    corrupted_file = open(args[3])

    corrupted_users = set()
    for i, line in enumerate(corrupted_file):
        user_id = int(line)
        
        if user_id < 0 or user_id >= num_users:
            raise Exception('user ids must be within [0, num_users-1]. Found '+str(user_id)+' in line '+str(i))
        if user_id in corrupted_users:
            raise Exception('found duplicate user id in line '+str(i))
        
        corrupted_users.add(user_id)
    corrupted_file.close()
except Exception as e:
    print('corrupted-file: '+str(e))
    sys.exit()

#users-file
try:
    users_file = open(args[4])

    senders = []
    for i, line in enumerate(users_file):
        user_id = int(line)

        if user_id < 0 or user_id >= num_users:
            raise Exception('user ids must be within [0, num_users-1]. Found '+str(user_id)+' in line '+str(i))
        if user_id in corrupted_users:
            raise Exception('user ids must not be in corrupted-file: a sender may not be corrupt')

        senders.append(user_id)

    users_file.close()
except Exception as e:
    print('users-file: '+str(e))
    sys.exit()

#broken-paths
try:
    broken_paths = int(args[5])

    if broken_paths < 0:
        raise Exception('broken paths must not be a negative number')
except Exception as e:
    print('broken-paths: '+str(e))

#fix-strategy
fix_strategy = args[6].lower()
if fix_strategy not in ['last-honest', 'initiator']:
    print('fix strategy may be one of: last-honest, initiator')
    sys.exit()


#Create a simulation object
simulation = crowds.CrowdsSimulation(phi, graph, corrupted_users, broken_paths, fix_strategy)

#delete unecessary data
del graph
del corrupted_users

#start the simulation
for sender in senders:
    simulation.simulate(sender)