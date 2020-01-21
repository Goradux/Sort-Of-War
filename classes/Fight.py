import random
# import colorama
# colorama.init()

random_list = [i + 1 for i in range(30)]
print('A list:')
print(random_list)

random.shuffle(random_list)
print()
print('Shuffled:')
print(random_list)

print()
for i in range(24):
    print(str(i).ljust(3), end='')
    for j in range(77):
        print('.', end='')
    print()

# print(chr(27) + "[2J") - escape sequence for clearing the terminal

import sys
def print_there(x, y, text):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
    sys.stdout.flush()

import time
for i in range(20):
    if i % 2 == 0:
        print_there(15, 10 + i, '#####')
        print_there(16, 10+ i, '#')
        print_there(17, 10+ i, '#')
        print_there(18, 10+ i, '#')
    else:
        # print_there(15, 10, '.')
        # print_there(16, 10, '.')
        # print_there(17, 10, '.')
        # print_there(18, 10, '.')
        pass
    time.sleep(0.5)
    print(chr(27) + "[2J")
