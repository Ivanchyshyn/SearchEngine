class WebRank:
    #Don't compute links if they link each other: a -> b, b -> a, a -> a etc. 
    @staticmethod
    def is_reciprocal(graph, source, destination, k):
        if k == 0:
            if destination == source:
                return True
            return False
        if source in graph[destination]:
            return True
        for node in graph[destination]:
            if WebRank.is_reciprocal(graph, source, node, k-1):
                return True
        return False

    @staticmethod
    def compute_ranks(graph, k):
        d = 0.8 # damping factor
        numloops = 10
    
        ranks = {}
        npages = len(graph)
        for page in graph:
            ranks[page] = 1.0 / npages
    
        for i in range(0, numloops):
            newranks = {}
            for page in graph:
                newrank = (1 - d) / npages
                count = 0
                for page2 in graph:
                    if page in graph[page2]:
                        if not WebRank.is_reciprocal(graph, page2, page, k):
                            newrank += (d*ranks[page2] / len(graph[page2]))
                newranks[page] = newrank
            ranks = newranks
        return ranks