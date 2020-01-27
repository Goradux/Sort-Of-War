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


    def sort(self, unsorted_list):
        start = datetime.datetime.now()
        sorted_list = self.quicksort(unsorted_list)
        end = datetime.datetime.now()
        print(end - start)
        return sorted_list

    def quicksort(self, unsorted_list):
        less = []
        equal = []
        greater = []

        if len(unsorted_list) > 1:
            pivot = unsorted_list[0]
            for x in unsorted_list:
                self.focus.append(x)
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                elif x > pivot:
                    greater.append(x)
            self.counter = self.counter + 1
            return self.quicksort(less)+equal+self.quicksort(greater)
        else:
            return unsorted_list