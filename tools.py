import statistics as s

class stats_list():

    def __init__(self):
        self.lst = []

    def append(self, item):
        self.lst.append(item)
        return

    def get_min(self):
        return min(self.lst)
    
    def get_max(self):
        return max(self.lst)
    
    def get_mean(self):
        return s.mean(self.lst)
    
    def get_stdev(self):
        return s.stdev(self.lst)