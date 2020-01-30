# dev name: Fight.py

import random
import colorama
import time
import sys

from classes.Renderer import Renderer
from classes.Fighter import Fighter
# colorama.init()


# import ctypes
# kernel32 = ctypes.windll.kernel32
# kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


# for i in range(0, 256):
#     print(f"\033[{i}mAt {i} THIS happens! \033[0m")
# print()


class Arena:
    

    renderer = None
    line_amount = None
    line_length = None

    fighter_left = None
    fighter_right = None

    counter_current_left = 0
    counter_current_right = 0


    def __init__(self):
        self.renderer = Renderer()
        self.line_amount, self.line_length = self.renderer.init()
        # self.fighter_left = Fighter(alg='quick')
        self.fighter_left = Fighter()
        # self.fighter_left = Fighter(alg='insertion')
        # self.fighter_right = Fighter(alg='bubble')
        self.fighter_right = Fighter(second=True)
        
        
    # def test(self):
    #     self.renderer.test()


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
        # some_list = [i + 1 for i in range(self.line_amount)]
        while True:
            some_list = []
            some_list = random.sample(range(1, self.line_length+1), self.line_amount)
            random.shuffle(some_list)
            unsorted_left = list(some_list)
            unsorted_right = list(some_list)


            sorted_left = self.fighter_left.sort(unsorted_left)
            sorted_right = self.fighter_right.sort(unsorted_right)


            self.renderer.name_left(self.fighter_left.name)
            self.renderer.name_right(self.fighter_right.name)


            self.counter_current_left, self.counter_current_right = self.renderer.sort_both(self.fighter_left.history, self.fighter_left.focus, self.fighter_right.history, self.fighter_right.focus)


            winner = self.roll_winner()
            self.renderer.update_tug(winner)
            self.fighter_left.reset()
            self.fighter_right.reset()




        # self.renderer.sort_left(self.fighter_left.history, self.fighter_left.focus)
        # self.renderer.sort_right(self.fighter_right.history, self.fighter_right.focus)

        # self.renderer.clear_terminal_right(1, self.renderer.term_height)