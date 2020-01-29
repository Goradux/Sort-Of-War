import ctypes, sys, time
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
        self.term_width, self.term_height = get_terminal_dimensions()
        self.middle_line = round(self.term_width / 2)
        clear_terminal(self.term_width, self.term_height, first=True)
        # print(self.term_width, self.term_height)
        if self.term_width < 80 or self.term_height < 24:
            print('The terminal window is too small. Shutting down.')
            print('The terminal should be at least 80x24.')
            sys.exit(1)
        # if self.term_height > 50:
        #     self.orientation = 'vertical'
        # print_80_24()
        self.outline()

        # 39 long max (80x24)
        # 15 lines max (80x24)

        self.line_length = 38
        self.line_amount = 15

        self.line_amount = self.term_height - 11
        if self.line_amount > self.line_length:
            self.line_amount = self.line_length

        return self.line_amount, self.line_length


    def outline(self):
        middle_line = round(self.term_width / 2)
        for i in range(self.term_height-8):
            print_at(i, middle_line, '|')
        for i in range(self.term_width+1):
            print_at(self.term_height-9, i, '-')
        print_at(self.term_height-9, middle_line, '+')


    def name_left(self, name):
        print_at(self.term_height-10, 1, name.center(self.middle_line - 1))


    def name_right(self, name):
        print_at(self.term_height-10, self.middle_line + 1, name.center(self.middle_line - 1))


    # def test(self):
    #     clear_terminal(self.term_width, self.term_height)
    #     # self.outline()
    #     for i in range(20):
    #         clear_terminal(self.term_width, self.term_height)
    #         if i % 2 == 0:
    #             print_at(15, 10 + i, '#####')
    #             print_at(16, 10+ i, '#')
    #             print_at(17, 10+ i, '#')
    #             print_at(18, 10+ i, '#')
    #         else:
    #             pass
    #         time.sleep(0.5)
        # print(chr(27) + "[2J")


    def sort_both(self, array1, pointers1, array2, pointers2):
        # test_index = 0
        for entry1, focus1, entry2, focus2 in itertools.zip_longest(array1, pointers1, array2, pointers2, fillvalue=[]):
            # clear_terminal(80,1)
            # print_at(1, 1, entry1)
            # print_at(2, 1, entry2)
            # print_at(3, 1, test_index)
            # test_index += 1

            if len(entry1) > 0:
                clear_terminal(self.line_length, self.line_amount)
            if len(entry2) > 0:
                self.clear_terminal_right(self.line_length, self.line_amount)

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

            time.sleep(0.05)


    # def sort_left(self, array, pointer):
    #     for entry, focus in zip(array, pointer):
    #         clear_terminal(self.line_length, self.line_amount)
    #         # self.outline()

    #         # print all of them
    #         for index, element in enumerate(entry):
    #             if index is focus:
    #                 print_at(1+index, 0, ''.ljust(element, '-'))
    #             else:
    #                 print_at(1+index, 0, ''.ljust(element, '#'))
    #         time.sleep(0.05)
    #     # return 0
    
    # def sort_right(self, array, pointer):
    #     for entry, focus in zip(array, pointer):
    #         self.clear_terminal_right(self.line_length, self.line_amount)

    #         for index, element in enumerate(entry):
    #             if index is focus:
    #                 print_at(1+index, self.middle_line + 1, ''.ljust(element, '-'))
    #             else:
    #                 print_at(1+index, self.middle_line + 1, ''.ljust(element, '#'))
    #         time.sleep(0.05)

