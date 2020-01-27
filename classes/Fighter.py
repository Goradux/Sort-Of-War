# import quicksort, mergesort, heapsort

# use only n log n algos for fairness


import random

from classes.algorithms.Quicksort import Quicksort
from classes.algorithms.Mergesort import Mergesort
from classes.algorithms.InsertionSort import InsertionSort
from classes.algorithms.SelectionSort import SelectionSort
from classes.algorithms.BubbleSort import BubbleSort


class Fighter:
    algorithm = None
    name = 'generic'
    history = []
    focus = []
    counter = []

    def __init__(self, alg=None):
        if alg is None:
            alg = 0
        if alg is 0:
            self.algorithm = random.choice([Quicksort(), Mergesort(), InsertionSort(), SelectionSort(), BubbleSort()])
        elif alg is 'quick':
            self.algorithm = Quicksort()
        elif alg is 'merge':
            self.algorithm = Mergesort()
        elif alg is 'insertion':
            self.algorithm = InsertionSort()
        elif alg is 'selection':
            self.algorithm = SelectionSort()
        elif alg is 'bubble':
            self.algorithm = BubbleSort()
        self.name = self.algorithm.name

        # actually unsure why this works
        # !!! I think it works because we assign lists, and they are mutable
        # so they auto update
        self.history = self.algorithm.history
        self.focus = self.algorithm.focus
        # counter is kinda useless?
        self.counter = self.algorithm.counter


    # return a sorted list
    def sort(self, unsorted_list):
        return self.algorithm.sort(unsorted_list)


    # def counter(self):
    #     return self.algorithm.get_counter()

    # def history(self):
    #     return self.algorithm.get_history()

    
    # def focus(self):
    #     return self.algorithm.get_focus()