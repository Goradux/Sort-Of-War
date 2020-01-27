class BubbleSort:
    counter = 0
    name = 'Bubble sort'
    history = []
    # focus are the indeces
    focus = []


    def get_counter(self):
        return self.counter


    def get_history(self):
        return self.history


    def get_focus(self):
        return self.focus


    def sort(self, unsorted_list):
        self.bubble_sort(unsorted_list)
        return unsorted_list


    # stable
    # O(1) space complexity
    # O(n2) comparisons and swaps
    # adaptive: O(n) when almost sorted
    def bubble_sort(self, array):
        # print(array, '- starting point')
        for index, _ in enumerate(array):
            swapped = False
            for i in range(len(array)-1, index, -1):
                if array[i] < array [i-1]:
                    # print(array, i)
                    self.history.append(list(array))
                    self.focus.append(i)
                    # swap
                    array[i], array[i-1] = array[i-1], array[i]
                    swapped = True
            if swapped is False:
                break
        # print(array, -1)
        self.history.append(list(array))
        self.focus.append(-1)