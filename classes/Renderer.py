import ctypes, sys, time, random
import shutil
import itertools


def get_terminal_dimensions():
    dimensions = shutil.get_terminal_size()
    width = dimensions.columns
    height = dimensions.lines
    return (width, height)


def print_at(line, column, text):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (line, column, text))
    sys.stdout.flush()


def clear_terminal(width, height, first=False):
    if first:
        print(chr(27) + "[2J")
    for i in range(height):
        print_at(i+1, 1, ''.ljust(width))


def print_80_24():
    print()
    for i in range(24):
        print(str(i).ljust(3), end='')
        for j in range(77):
            print('.', end='')
        print()


# print(chr(27) + "[2J") - escape sequence for clearing the terminal


class Renderer:


    # orientation = 'horizontal'
    term_width = None
    term_height = None
    line_length = None
    line_amount = None
    middle_line = None
    sorter_left = (None, None)
    sorter_right = (None, None)
    animation = (None, None)
    guy_side_amount = 0
    counter_current_left = 0
    counter_current_right = 0
    pixels_to_lose = 0
    moved_left = 0
    moved_right = 0
    rope_length = 0


    def clear_terminal_at_for(self, at_x, at_y, width, lines):
        for i in range(lines):
            print_at(at_y+i, at_x, ''.ljust(width))


    def clear_terminal_right(self, width, height, first=False):
        if first:
            print(chr(27) + "[2J")
        for i in range(height):
            print_at(i+1, self.middle_line + 1, ''.ljust(width))


    def init(self):
        # essentially the same as colorama, but without shortcuts
        # enables ansi escape sequences (some of them anyway)
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

        # get terminal dimensions
        self.term_width, self.term_height = get_terminal_dimensions()
        self.middle_line = round(self.term_width / 2)
        clear_terminal(self.term_width, self.term_height, first=True)
        # print(self.term_width, self.term_height)
        if self.term_width < 36 or self.term_height < 17:
            print('The terminal window is too small. Shutting down.')
            print('The terminal should be at least 36x20.')
            print('Current dimensions are: ', self.term_width, 'columns by', self.term_height, 'lines.')
            sys.exit(1)


        # draw some basic terminal parts
        self.outline()
        self.draw_rope()

        # number of blocks available per side
        # print_at(self.term_height-8, 0, self.middle_line-1)
        # print_at(1,1, str(self.term_width) + ' ' + str(self.term_height))


        self.guy_side_amount = self.calculate_guys_number()
        # print_at(self.term_height-7, 1, self.guy_side_amount)
        self.draw_guys_left()
        self.draw_guys_right()


        # 39 long max (80x24)
        # 15 lines max (80x24)
        self.line_length = self.middle_line - 2
        self.line_amount = self.term_height - 11
        if self.line_amount > self.line_length:
            self.line_amount = self.line_length

        return self.line_amount, self.line_length


    def calculate_guys_number(self):
        amount = 0
        length_left = self.middle_line
        while length_left > round((self.middle_line - 1) / 1.5) and length_left > 17:
            length_left -= 8
            amount += 1
        self.pixels_to_lose = length_left - round(self.middle_line / 3)
        # self.moved_left = self.pixels_to_lose
        # self.moved_right = self.pixels_to_lose
        # print_at(self.term_height-1, 0, self.pixels_to_lose)
        return amount


    def outline(self):
        middle_line = round(self.term_width / 2)
        for i in range(self.term_height-8):
            print_at(i, middle_line, '|')
        for i in range(self.term_width+1):
            print_at(self.term_height-9, i, '-')
        print_at(self.term_height-9, middle_line, '^')
        print_at(self.term_height-1, middle_line, '^')


    def name_left(self, name):
        print_at(self.term_height-10, 1, name.center(self.middle_line - 1))


    def name_right(self, name):
        print_at(self.term_height-10, self.middle_line + 1, name.center(self.middle_line - 1))


    def clean_counters(self):
        print_at(self.term_height-8, 1, '    ')
        print_at(self.term_height-8, self.term_width-3, '    ')


    def sort_both(self, array1, pointers1, array2, pointers2):
        self.clean_counters()
        counter = 0
        for entry1, focus1, entry2, focus2 in itertools.zip_longest(array1, pointers1, array2, pointers2, fillvalue=[]):
 
            if len(entry1) > 0:
                clear_terminal(self.line_length, self.line_amount)
                # counter for left one
                print_at(self.term_height-8, 1, str(counter).rjust(4))
                self.counter_current_left = counter
            if len(entry2) > 0:
                self.clear_terminal_right(self.line_length, self.line_amount)
                # counter for right one
                print_at(self.term_height-8, self.term_width-3, str(counter).ljust(4))
                self.counter_current_right = counter

            for index, packed in enumerate(itertools.zip_longest(entry1, entry2)):
                element1, element2 = packed
                if element1 is not None:
                    if index is focus1:
                        print_at(1+index, 0, ''.ljust(element1, '#'))
                    else:
                        print_at(1+index, 0, ''.ljust(element1, ':'))    

                if element2 is not None:
                    if index is focus2:
                        print_at(1+index, self.middle_line + 1, ''.ljust(element2, '#'))
                    else:
                        print_at(1+index, self.middle_line + 1, ''.ljust(element2, ':'))

            counter += 1
            time.sleep(0.04)
        return self.counter_current_left, self.counter_current_right


    def draw_rope(self, length=0):
        if length is 0:
            self.rope_length = round(self.term_width/6*4+1)
        else:
            self.rope_length -= length
        print_at(self.term_height - 4, length + round(self.term_width/6), ''.center(self.rope_length, '='))


    # each guy is 8x8 characters
    def draw_guy_left(self, y_offset='default'):
        if y_offset is 'default':
            y_offset = round(self.term_width/6) + 1 + self.moved_left
        else:
            y_offset += round(self.term_width/6) + 1 + self.moved_left
        x = self.term_height - 8
        print_at(x  , y_offset, ' __     ')
        print_at(x+1, y_offset, '/><\    ')
        print_at(x+2, y_offset, '\__/    ')
        print_at(x+3, y_offset, '|\ |\   ')
        print_at(x+4, y_offset, '==\/0\/0')
        print_at(x+5, y_offset, '|__|    ')
        print_at(x+6, y_offset, ' \  \   ')
        print_at(x+7, y_offset, ' /_  \_ ')

    
    def draw_guys_left(self):
        for i in range(self.guy_side_amount):
            self.draw_guy_left(i*8)


    def draw_guy_right(self, y_offset='default'):
            if y_offset is 'default':
                y_offset = round(self.term_width/6*5) - 8 - self.moved_right
            else:
                y_offset = round(self.term_width/6*5) - 8 - y_offset - self.moved_right
            x = self.term_height - 8
            print_at(x  , y_offset, '     __ ')
            print_at(x+1, y_offset, '    /><\\')
            print_at(x+2, y_offset, '    \__/')
            print_at(x+3, y_offset, '   /| /|')
            print_at(x+4, y_offset, '0\/0\/==')
            print_at(x+5, y_offset, '    |__|')
            print_at(x+6, y_offset, '    / / ')
            print_at(x+7, y_offset, '  _/ _\ ')


    def draw_guys_right(self):
        for i in range(self.guy_side_amount):
            self.draw_guy_right(i*8)


    def update_tug(self, winner):
        move = random.randint(1, 3)
        # clean_tug_area()
        self.clear_terminal_at_for(1, self.term_height-8, self.term_width, 8)
        # draw_new_rope()
        if winner is 'left':
            self.moved_left += move
            self.draw_rope(move)
        elif winner is 'right':
            self.moved_right += move
            self.draw_rope(move * -1)
        print_at(self.term_height-1, self.middle_line, '^')
        self.draw_guys_left()
        self.draw_guys_right()

        self.check_win_condition()

    
    def check_win_condition(self):
        if self.moved_left >= self.pixels_to_lose:
            print_at(self.term_height-7, self.middle_line-6, '+----------+')
            print_at(self.term_height-6, self.middle_line-6, '|RIGHT WON!|')
            print_at(self.term_height-5, self.middle_line-6, '+----------+')
            sys.exit(0)
        if self.moved_right >= self.pixels_to_lose:
            print_at(self.term_height-7, self.middle_line-6, '+----------+')
            print_at(self.term_height-6, self.middle_line-6, '|LEFT WON! |')
            print_at(self.term_height-5, self.middle_line-6, '+----------+')
            sys.exit(0)