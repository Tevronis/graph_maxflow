INF = 1000000000    #1kkk

class edge:
    def __init__(self, flow=0, cup=0, first=None, second=None):
        self.first = first
        self.second = second
        self.flow = flow
        self.cup = cup