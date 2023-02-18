from node import node
from sys import argv
import os

class Knapsack:
    def __init__(self, items):
        self.items = items
        self.__pre_process()
        self._node = None

    def __pre_process(self):
        ''' sort items in descending order of value/weight '''
        self.items.sort(key=lambda x: x[1]/x[0], reverse=True)
        self.value_weight = [item[1]/item[0] for item in self.items]


    def lenght(self):
        return len(self.items)


    def knapsack(self, weight_of_knapsack, method):
        ''' solve the knapsack problem'''
        self._node = node(self.items)
        self.__knapsack(weight_of_knapsack, method)
        return self._node

    def __knapsack(self, weight_of_knapsack, method, _node=None, i=0):
        ''' recursive function to solve the knapsack problem'''
        if _node is None:
            _node = node()

        # not feasible
        if _node.weight > weight_of_knapsack:
            return None
            
        # node is leaf
        if len(self.items) <= i:
            if _node.value > self._node.value:
                self._node = _node
            return None

        # calculate the upper limit of the node for problem 1
        if method:
            _node.ub = self.problem2(_node, i, weight_of_knapsack)
        # calculate the upper limit of the node for problem 2
        else:
            _node.ub = self.problem1(_node, i, weight_of_knapsack)
        # Pruning with the upper limit
        if _node.ub < self._node.ub:
            _node.ub = self._node.ub
            return None

        # left Tree
        left_node = node(_node.weight, _node.value)
        left_node.weight += self.items[i][0]
        left_node.value += self.items[i][1]
        left_node.selected_items = _node.selected_items
        left_node.selected_items.append(i)
        self.__knapsack(weight_of_knapsack,method, left_node, i+1)


        # right Tree
        right_node = node(_node.weight, _node.value)
        right_node.selected_items = _node.selected_items

        self.__knapsack(weight_of_knapsack, method, _node, i+1)

    def problem1(self, _node, i, weight_of_knapsack):
        ''' calculate the upper limit of the node for problem 1 '''
        return _node.value + (weight_of_knapsack - _node.weight)*(self.value_weight[i])

    def problem2(self, _node, i, weight_of_knapsack):
        ''' calculate the upper limit of the node for problem 2 '''
        ub = 0
        weight = 0
        for item in _node.selected_items:
            weight += self.items[item][0]
            ub += self.items[item][1]
        if weight > weight_of_knapsack:
            return ub
        for idx in range(i, len(self.items)):
            if weight + self.items[idx][0] > weight_of_knapsack:
                ub += (weight_of_knapsack - weight) * self.value_weight[idx]
                break
            weight += self.items[idx][0]
            ub += self.items[idx][1]
        return ub

    def print(self):
        # print the items
        _str = f' index | weight | value | value/weight '.center(50,"*")
        print(_str)
        for i,item in enumerate(zip(self.items, self.value_weight)):
            _str = f"{i:^5}|{item[0][0]:^8}|{item[0][1]:^7}|{item[1]:^12.3}"
            print(f"{_str:^50s}")

    @staticmethod
    def read_input(weight_of_knapsack, size_of_items):
        ''' read input from stdin '''
        print("Enter the weight and value of each item")
        items = []
        while len(items) < size_of_items:
            
            item = input(f"item {len(items)+1}: ").split()
            if len(item) != 2:
                print("Invalid input")
                continue
            items.append(list(map(int, item)))
        return items, weight_of_knapsack

    @staticmethod
    def read_txt(path):
        ''' read input from txt file '''
        if not os.path.exists(path):
            print("File not found")
            return None, None
        with open(path, "r") as f:
            s = f.readline().strip().split(" ")
            weight_of_knapsack, size_of_items = list(map(int, s))
            items = list()
            for line in f:
                items.append(list(map(int, line.strip().split(" "))))
        return items, weight_of_knapsack

