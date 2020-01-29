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


# random_list = [i + 1 for i in range(30)]
# print('A list:')
# print(random_list)


# random.shuffle(random_list)
# print()
# print('Shuffled:')
# print(random_list)


class Arena:
    

    renderer = None
    line_amount = None
    line_length = None

    fighter_left = None
    fighter_right = None


    def __init__(self):
        self.renderer = Renderer()
        self.line_amount, self.line_length = self.renderer.init()
        # self.fighter_left = Fighter(alg='quick')
        self.fighter_left = Fighter()
        # self.fighter_left = Fighter(alg='insertion')
        # self.fighter_right = Fighter(alg='bubble')
        self.fighter_right = Fighter()
        
        
    # def test(self):
    #     self.renderer.test()


    def start(self):
        # some_list = [i + 1 for i in range(self.line_amount)]
        some_list = random.sample(range(1, self.line_length+1), self.line_amount)
        random.shuffle(some_list)
        unsorted_left = some_list
        unsorted_right = list(some_list)
        # print()
        # print('Shuffled list:')
        # print(some_list)
        # print()



        # print('Left,', self.fighter_left.name)
        sorted_left = self.fighter_left.sort(unsorted_left)
        # print(sorted_left)
        # print(self.fighter_left.counter)
        # print(self.fighter_left.focus)
        
        # for array, index in zip(self.fighter_left.history, self.fighter_left.focus):
        #     print(array, index)
        # print(len(self.fighter_left.focus))


    
        # print('Right,', self.fighter_right.name)
        sorted_right = self.fighter_right.sort(unsorted_right)

        # for array, index in zip(self.fighter_right.history, self.fighter_right.focus):
        #     print(array, index)
        # print(len(self.fighter_right.focus))


        self.renderer.name_left(self.fighter_left.name)
        self.renderer.name_right(self.fighter_right.name)
        
        self.renderer.sort_both(self.fighter_left.history, self.fighter_left.focus, self.fighter_right.history, self.fighter_right.focus)

        # self.renderer.sort_left(self.fighter_left.history, self.fighter_left.focus)
        # self.renderer.sort_right(self.fighter_right.history, self.fighter_right.focus)

        # self.renderer.clear_terminal_right(1, self.renderer.term_height)