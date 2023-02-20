
import numpy as np
from os import path
from sys import argv
class Knapsack_Sample:
    @staticmethod    
    def Knapsack_generator(weight, value, size_of_items):
        _weight = np.random.randint(weight[0],weight[1], size_of_items)
        _value = np.random.randint(value[0], value[1], size_of_items)
        return _weight,_value
    @staticmethod
    def Knapsack_generator_str(weight:list, value:list, size_of_items:int,weight_of_knapsack:int):
        _weight, _value = Knapsack_Sample.Knapsack_generator(weight, value, size_of_items)
        lst = [f"{weight_of_knapsack} {size_of_items}"]
        for i in zip(_weight, _value):
            lst.append(f"{i[0]} {i[1]}")
        return lst


