class SelectionSort:
    name = 'Selection sort'
    history = []
    focus = []


    def reset(self):
        self.history = []
        self.focus = []
        

    def sort(self, unsorted_list):
        self.selection_sort(unsorted_list)
        return unsorted_list
        

    # O(1) space complexity
    # O(n2) comparisons
    # O(n) swaps
    # not adaptive
    # is used if the cost of swapping is high
    # runtime is always quadratic
    def selection_sort(self, array):
        for index, _ in enumerate(array):
            i = index
            for j in range(index + 1, len(array)):
                # if array[j] < array[i]:
                #     i = j
                i = j if array[j] < array[i] else i
                # print(array, j)
                self.history.append(list(array))
                self.focus.append(j)
            # swap
            array[index], array[i] = array[i], array[index]
        # print(array, -1)
        self.history.append(list(array))
        self.focus.append(-1)
