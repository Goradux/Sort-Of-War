import datetime

class Quicksort:
    counter = 0
    name = 'Quicksort'
    history = []
    focus = []


    def get_counter(self):
        return self.counter


    def get_history(self):
        return self.history


    def get_focus(self):
        return self.focus


    def sort(self, array):
        # start = datetime.datetime.now()
        sorted_list = self.quicksort(array)
        # end = datetime.datetime.now()
        # print(end - start)
        return sorted_list

    def quicksort(self, array, old_left=[], old_right=[]):
        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0]
            for index, x in enumerate(array):
                self.focus.append(index)
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                elif x > pivot:
                    greater.append(x)
            # self.counter = self.counter + 1
            self.history.append(old_left + array + old_right)
            return self.quicksort(less, old_left, greater + old_right)+equal+self.quicksort(greater, old_left + less, old_right)
        else:
            return array

        
    def __init__(self):
        array = [5, 6, 7, 4, 0, 8, 1, 3, 2]
        array_sorted = self.sort(array)
        print(array_sorted, '- sorted array')


sorter = Quicksort()
for array in sorter.history:
    print(array)
    
# def my_quicksort(array=[5,2,3,1,4,0], direction='central'):
#     # import random
#     if len(array) > 1:
#         print(array, '- starting point', direction)
#         # pivot - element 0
#         i = 0
#         for index, _ in enumerate(array):
#             if index > 0:
#                 if array[index] < array[0]:
#                     print(array)
#                     # swap
#                     array[i], array[index] = array[index], array[i]
#                     i += 1
#         # swap
#         print(array)
#         array[0], array[i] = array[i], array[0]
#         my_quicksort(array[0:i-1], 'left')
#         my_quicksort(array[i+1:len(array)], 'right')
#         print(array)

# my_quicksort()
