"""
Finding out rank of web page.
"""
class WebRank:
    @staticmethod
    def is_reciprocal(graph, source, destination, k):
        """Don't compute links if they link each other: a -> b, b -> a, a -> a etc."""
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
        damp = 0.8 # damping factor
        numloops = 10

        ranks = {}
        npages = len(graph)
        for page in graph:
            ranks[page] = 1.0 / npages

        for _ in range(numloops):
            newranks = {}
            for page in graph:
                newrank = (1 - damp) / npages
                for page2 in graph:
                    if page in graph[page2]:
                        if not WebRank.is_reciprocal(graph, page2, page, k):
                            newrank += (damp*ranks[page2] / len(graph[page2]))
                newranks[page] = newrank
            ranks = newranks
        return ranks
