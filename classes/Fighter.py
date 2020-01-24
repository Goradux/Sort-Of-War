# import quicksort, mergesort, heapsort

# use only n log n algos for fairness


import random

from classes.algorithms.Quicksort import Quicksort
from classes.algorithms.Mergesort import Mergesort


class Fighter:
    algorithm = None
    name = 'generic'
    

    def __init__(self, alg=None):
        if alg is None:
            alg = 0
        if alg is 0:
            self.algorithm = random.choice([Quicksort(), Mergesort()])
        elif alg is 'quick':
            self.algorithm = random.choice([Quicksort()])
        elif alg is 'merge':
            self.algorithm = random.choice([Mergesort()])
        self.name = self.algorithm.name
    

    # return a sorted list
    def sort(self, unsorted_list):
        return self.algorithm.sort(unsorted_list)


    def counter(self):
        return self.algorithm.get_counter()

    def history(self):
        return self.algorithm.get_history()

    
    def focus(self):
        return self.algorithm.get_focus()