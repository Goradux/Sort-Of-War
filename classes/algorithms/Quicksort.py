import datetime, random


class Quicksort:
    name = 'Quicksort'
    history = []
    focus = []
    tmp_array = []


    def reset(self):
        self.history = []
        self.focus = []
        

    def sort(self, array):
        self.tmp_array = list(array)
        sorted_list = self.my_quicksort(array)
        self.history.append(sorted_list)
        self.focus.append(-1)
        return sorted_list


    def my_quicksort(self, array, left=[], right=[], replace_index=0):
        if len(array) > 1:

            # choosing pivot
            some_point = random.randint(1, len(array)-1)
            in_place = array[some_point]
            # print('- starting point, pivot is', array[some_point])
            self.history.append(list(self.tmp_array))
            self.focus.append(replace_index)

            array[0], array[some_point] = array[some_point], array[0]
            
            for j in range(len(array)):
                self.tmp_array[replace_index+j] = array[j]


            # pivot - element 0
            # print(array, '', array[0], 'is the pivot')
            i = 0
            for index, _ in enumerate(array):
                if index > 0:
                    if array[index] < array[0]:
                        i += 1
                        if i is not index:
                            # print(left + array + right, 'swapping', array[i], 'and', array[index])
                            
                            self.history.append(list(self.tmp_array))
                            self.focus.append(replace_index+index)
                            
                            # swap
                            array[i], array[index] = array[index], array[i]

                            for j in range(len(array)):
                                self.tmp_array[replace_index+j] = array[j]
                            # print(tmp_array, '- tmp')
                            
                            # print(self.tmp_array, 'swapped', array[i], 'and', array[index])

            if i is not 0:
                # print(left + array + right, '- before pivot swapping')
                
                # swap
                array[0], array[i] = array[i], array[0]

                for j in range(len(array)):
                    self.tmp_array[replace_index+j] = array[j]
                # print(tmp_array, '- tmp')
            self.history.append(list(self.tmp_array))
            self.focus.append(replace_index+i+1)
            # print(self.tmp_array, array[i], 'should be in place now')

            return self.my_quicksort(array[0:i], left, [array[i]] + array[i+1:len(array)] + right, replace_index) + [array[i]] + self.my_quicksort(array[i+1:len(array)], left + array[0:i] + [array[i]], right, replace_index+i+1)
        else:
            return array
