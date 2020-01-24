import ctypes, sys, time
import shutil


def get_terminal_dimensions():
    dimensions = shutil.get_terminal_size()
    width = dimensions.columns
    height = dimensions.lines
    return (width, height)


def print_there(x, y, text):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
    sys.stdout.flush()


def clear_terminal(width, height, first=False):
    if first:
        print(chr(27) + "[2J")
    for i in range(height):
        print_there(i+1, 1, ''.ljust(width))


def print_80_24():
    print()
    for i in range(24):
        print(str(i).ljust(3), end='')
        for j in range(77):
            print('.', end='')
        print()


# print(chr(27) + "[2J") - escape sequence for clearing the terminal


class Renderer:


    i = 0
    term_width = None
    term_height = None


    def init(self):
        # essentially the same as colorama, but without shortcuts
        # enables ansi escape sequences (some of them anyway)
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        self.term_width, self.term_height = get_terminal_dimensions()
        clear_terminal(self.term_width, self.term_height, first=True)
        print(self.term_width, self.term_height)

    
    def test(self):
        clear_terminal(self.term_width, self.term_height)
        for i in range(20):
            clear_terminal(self.term_width, self.term_height)
            if i % 2 == 0:
                print_there(15, 10 + i, '#####')
                print_there(16, 10+ i, '#')
                print_there(17, 10+ i, '#')
                print_there(18, 10+ i, '#')
            else:
                pass
            time.sleep(0.5)
        # print(chr(27) + "[2J")

