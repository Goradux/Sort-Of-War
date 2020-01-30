import random
import time
import sys

from classes.Renderer import Renderer
from classes.Fighter import Fighter


class Arena:
    
    # object that takes care of the GUI part of the program
    renderer = None
    # amount of lines is the limit for the size of the list to sort
    line_amount = None
    # line length is the limit for the size of the values to sort
    line_length = None
    # objects that wrap the sorting algorithms
    fighter_left = None
    fighter_right = None
    # counters that hold the amount of steps executed by each of the algorithms
    counter_current_left = 0
    counter_current_right = 0


    def __init__(self):
        self.renderer = Renderer()
        self.line_amount, self.line_length = self.renderer.init()
        self.fighter_left = Fighter()
        self.fighter_right = Fighter(second=True)


    # if both of the algorithms take the same amount of swaps to sort, then the
    # winner is determined randomly
    def roll_winner(self):
        # chance_left = self.counter_current_right
        # chance_right = self.counter_current_left
        # if random.randint(0, chance_left + chance_right) < chance_left:
        if self.counter_current_left < self.counter_current_right:
            return 'right'
        elif self.counter_current_left > self.counter_current_right:
            return 'left'
        else:
            return 'left' if random.random() < 0.5 else 'right'


    def start(self):
        while True:
            # generate a new list
            some_list = random.sample(range(1, self.line_length+1), self.line_amount)
            random.shuffle(some_list)
            unsorted_left = some_list
            unsorted_right = list(some_list)

            # run the sorting algorithms over the generated list
            self.fighter_left.sort(unsorted_left)
            self.fighter_right.sort(unsorted_right)

            # render the algo names
            self.renderer.name_left(self.fighter_left.name)
            self.renderer.name_right(self.fighter_right.name)

            # render the history of the sorted lists
            self.counter_current_left, self.counter_current_right = self.renderer.sort_both(self.fighter_left.history, self.fighter_left.focus, self.fighter_right.history, self.fighter_right.focus)

            # check the round winner and draw the updated tug
            winner = self.roll_winner()
            self.renderer.update_tug(winner)

            # delete the old history and focus of the algorithms
            self.fighter_left.reset()
            self.fighter_right.reset()


# for i in range(0, 256):
#     print(f"\033[{i}mAt {i} THIS happens! \033[0m")
# print()
