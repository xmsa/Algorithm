
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

test_mode = False
if __name__ == "__main__":
    if test_mode:
        weight_of_knapsack = 10
        size_of_items = 140
        min_weight = 1
        max_weight = 10
        min_value = 10
        max_value = 50
    else:
            exit()
    weight = (min_weight , max_weight)
    value = (min_value , max_value)

    make_sample(weight, value, size_of_items,weight_of_knapsack)
