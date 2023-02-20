import numpy as np
class Binary_Search_Sample:
    @staticmethod
    def make_sample(size_, min_=0, max_=100):
        rnd = np.random.random(size=size_)
        lst = [round((r*max_)-min_,3) for r in rnd]
        return lst
    @staticmethod
    def make_sample_with_str(size_, min_=0, max_=100):
        lst =  Binary_Search_Sample.make_sample(size_, min_, max_)
        lst = list(map(str,lst))
        return [",".join(lst), "name"]