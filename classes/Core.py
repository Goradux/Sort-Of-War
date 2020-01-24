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

    fighter_left = None
    fighter_right = None


    def __init__(self):
        self.renderer = Renderer()
        # self.renderer.init()
        self.fighter_left = Fighter(alg='quick')
        self.fighter_right = Fighter(alg='merge')
        
        
    def test(self):
        self.renderer.test()


    def start(self):
        some_list = [i + 1 for i in range(15)]
        random.shuffle(some_list)
        print()
        print('Shuffled list:')
        print(some_list)
        print()



        print('Left,', self.fighter_left.name)
        sorted_left = self.fighter_left.sort(some_list)
        print(sorted_left)
        print(self.fighter_left.counter())
        print(self.fighter_left.focus())

        # print('Right,', self.fighter_right.name)
        # sorted_right = self.fighter_right.sort(some_list)
        # # print(sorted_right)
        # print(self.fighter_right.counter())
        