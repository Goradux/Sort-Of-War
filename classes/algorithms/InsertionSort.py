class InsertionSort:
    counter = 0
    name = 'Insertion sort'
    history = []
    # focus are the indeces
    focus = []


    def get_counter(self):
        return self.counter


    def get_history(self):
        return self.history


    def get_focus(self):
        return self.focus


    def reset(self):
        self.history = []
        self.focus = []
        self.counter = 0

    def sort(self, unsorted_list):
        self.insertion_sort(unsorted_list)
        return unsorted_list


    # O(1) space complexity
    # O(n2) comparisons and swaps
    # adaptive, O(n) when almost sorted
    # low overhead
    def insertion_sort(self, array):
        # print(array, '- starting point')
        for index, _ in enumerate(array):
            if index > 0:
                i = index
                while i > 0 and array[i] < array[i-1]:
                    # print(array, i)

                    # important to create a copy of a list because lists are
                    # mutable in Python
                    self.history.append(list(array))
                    self.focus.append(i)
                    # swap
                    array[i], array[i-1] = array[i-1], array[i]
                    i -= 1
        # print(array, -1)              # sorted array, with -1 as the focus
        self.history.append(list(array))
        self.focus.append(-1)