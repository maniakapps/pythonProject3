import os

def p(s):
    #Make the first string point to the root of the project with respect to the directory this process is running 
    #return './Project\\ 1/'+s
    return './'+s

cor = ['cor', 'nocor']
uniform = ['uniform', 'nouniform']
phis = [0.5, 0.6, 0.7, 0.8, 0.9]
fix = ['last-honest', 'initiator']
broken_paths = [0, 1, 2]

simulate_path = p('simulate.py')
map_path = p('map_observables.py')
generate_fbleau_input = p('generate_fbleau_input.py')

for c in cor:
    for u in uniform:
        for phi in phis:
            for broken in broken_paths:
                for f in fix:

                    # 1. SIMULATE
                    #phi
                    graph = p('data/adj-matrices/adj-full')
                    if c == 'cor':
                        corrupted = p('data/corrupt/cor')
                    else:
                        corrupted = p('data/corrupt/nocor')
                    users = p('data/users/users-'+c+'-'+u)
                    #f
                    simulate_out = p('data/simulation-outputs/simulate/'+c+'-'+u+'-'+f+'-'+'broken'+str(broken)+'-'+str(phi))+'-'+'full'
                    simulate = 'python3 {} {} {} {} {} {} {} > {}'.format(simulate_path, phi, graph, corrupted, users, broken, f, simulate_out)
                    
                    print(simulate)
                    os.system(simulate)

                    # 2. MAP
                    map_out = p('data/simulation-outputs/map/'+c+'-'+u+'-'+f+'-'+'broken'+str(broken)+'-'+str(phi)+'-'+'full'+'.csv')
                    map_ = 'python3 {} {} {} {}'.format(map_path, simulate_out, users, map_out)
                    
                    print(map_)
                    os.system(map_)

                    # 3. GENERATE FBLEAU INPUT
                    fbleau_train = p('data/simulation-outputs/fbleau-input/'+c+'-'+u+'-'+f+'-'+'broken'+str(broken)+'-'+str(phi)+'-'+'full'+'-train.csv')
                    fbleau_test = p('data/simulation-outputs/fbleau-input/'+c+'-'+u+'-'+f+'-'+'broken'+str(broken)+'-'+str(phi)+'-'+'full'+'-test.csv')
                    fbleau_input = 'python3 {} {} {} {}'.format(generate_fbleau_input, map_out, fbleau_train, fbleau_test)

                    print(fbleau_input)
                    os.system(fbleau_input)

                    # 4. EXECUTE FBLEAU
                    fbleau_output = p('data/simulation-outputs/fbleau-output/'+c+'-'+u+'-'+f+'-'+'broken'+str(broken)+'-'+str(phi)+'-'+'full')
                    fbleau_execute = 'fbleau nn {} {} > {}'.format(fbleau_train, fbleau_test, fbleau_output)
                    
                    print(fbleau_execute)
                    os.system(fbleau_execute)
