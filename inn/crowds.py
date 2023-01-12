import random

class CrowdsSimulation:

    def __init__(self, phi, graph, corrupted_users, broken_paths, fix_strategy):
        self.phi = phi
        self.num_users = len(graph)
        self.broken_paths = broken_paths
        if fix_strategy not in ['initiator', 'last-honest']:
            raise Exception('fix strategy may only be one of: initiator, last-honest')
        self.fix_strategy = fix_strategy
        self.graph = []

        for i in range(self.num_users):
            is_corrupt = i in corrupted_users
            self.graph.append(User(i, is_corrupt))

        for i, row in enumerate(graph):
            #add the user themselves in their edges list so we can forward uniformly
            self.graph[i].add_edge(self.graph[i])
            '''
            For every 1 in the row, connect this user with id 'row' to the user with id 'column'
            In later iterations, connect them the other way around, since there will always 
            be a 1 in both places
            '''
            for j, element in enumerate(row):
                if element == '1':
                    self.graph[i].add_edge(self.graph[j])

    def simulate(self, user_id):
        #start the stack with just the sender
        self.stack = [self.graph[user_id]]
        broken_paths_left = self.broken_paths

        next_user = self.choose_forward()

        #keep forwarding while the message is not sent to the server
        self.output = ''
        while next_user is not None:
            self.stack.append(next_user)
            if self.stack[-1].is_corrupt:
                self.detect(self.stack[-2])
                broken_paths_left -= 1
                if broken_paths_left <= 0:
                    break
                self.fix()
            next_user = self.choose_forward()
            
            #The server is controlled by the adversary. Sending to the server causes a detection.
            if next_user is None:
                self.detect(self.stack[-1])

        #print the output without the last space or '-' if it's empty
        if self.output == '':
            print('-')
        else:
            print(self.output[:-1])


    def detect(self, user):
        #This user got detected by a corrupt user
        self.output += str(user.id) + ' '

    def fix(self):
        if self.fix_strategy == 'initiator':
            self.stack = self.stack[0:1]
        else:
            #last-honest
            del self.stack[-1]

    def choose_forward(self):
        user = self.stack[-1]

        will_forward = False
        if len(self.stack) == 1:
            #If it's the first user, always forward
            will_forward = True
        else:
            #Calculate whether we forward or not based on phi
            if random.random() <= self.phi:
                will_forward = True

        if will_forward:
            #return a random user from this user's edges
            return random.choice(user.edges)
        else:
            #the message is sent to the server
            return None


class User:

    def __init__(self, id, is_corrupt):
        self.id = id
        self.is_corrupt = is_corrupt
        self.edges = []

    def add_edge(self, user):
        self.edges.append(user)
