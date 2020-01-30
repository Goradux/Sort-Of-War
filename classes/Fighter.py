import random

from classes.algorithms.Quicksort import Quicksort
from classes.algorithms.Mergesort import Mergesort
from classes.algorithms.InsertionSort import InsertionSort
from classes.algorithms.SelectionSort import SelectionSort
from classes.algorithms.BubbleSort import BubbleSort


# Mergesort is not ready
# choices = [Quicksort(), Mergesort(), InsertionSort(), SelectionSort(), BubbleSort()]
choices = [Quicksort(), InsertionSort(), SelectionSort(), BubbleSort()]

class Fighter:
    algorithm = None
    name = 'generic'
    # history is a list of lists that holds all of the previous states of the
    # initial unsorted list
    history = []
    # focus is a list of indexes that shows which of the elements of the history
    # entries should be highlighted
    focus = []


    def __init__(self, alg=None, second=False):
        if not second:
            if alg is None:
                alg = 0
            if alg is 0:
                self.algorithm = random.choice(choices)
                choices.remove(self.algorithm)
            # can set the first algorithm to a specific type for debugging
            elif alg is 'Quicksort':
                self.algorithm = Quicksort()
            elif alg is 'Mergesort':
                self.algorithm = Mergesort()
            elif alg is 'Insertion sort':
                self.algorithm = InsertionSort()
            elif alg is 'Selection sort':
                self.algorithm = SelectionSort()
            elif alg is 'Bubble sort':
                self.algorithm = BubbleSort()
        else:
            if alg is None:
                alg = 0
            if alg is 0:
                self.algorithm = random.choice(choices)
            
        self.name = self.algorithm.name
        self.history = self.algorithm.history
        self.focus = self.algorithm.focus


    def sort(self, unsorted_list):
        return self.algorithm.sort(unsorted_list)


    def reset(self):
        self.history = []
        self.focus = []
        self.algorithm.reset()
        self.history = self.algorithm.history
        self.focus = self.algorithm.focus
        