import datetime, random

# quicksort notes:
# unstable

class Quicksort:
    counter = 0
    name = 'Quicksort'
    history = []
    focus = []
    tmp_array = []


    def get_counter(self):
        return self.counter


    def get_history(self):
        return self.history


    def get_focus(self):
        return self.focus


    def sort(self, array):
        # start = datetime.datetime.now()
        self.tmp_array = list(array)
        sorted_list = self.my_quicksort(array)
        # end = datetime.datetime.now()
        # print(end - start)
        self.history.append(sorted_list)
        self.focus.append(-1)
        return sorted_list

    # def quicksort(self, array, old_left=[], old_right=[]):
    #     less = []
    #     equal = []
    #     greater = []

    #     if len(array) > 1:
    #         pivot = array[0]
    #         for index, x in enumerate(array):
    #             self.focus.append(index)
    #             if x < pivot:
    #                 less.append(x)
    #             elif x == pivot:
    #                 equal.append(x)
    #             elif x > pivot:
    #                 greater.append(x)
    #         # self.counter = self.counter + 1
    #         self.history.append(old_left + array + old_right)
    #         return self.quicksort(less, old_left, greater + old_right)+equal+self.quicksort(greater, old_left + less, old_right)
    #     else:
    #         return array

        
    # def __init__(self):
    #     array = [5, 6, 7, 4, 0, 8, 1, 3, 2]
    #     print(array, '- starting array')
    #     array_sorted = self.sort(array)
    #     # print(array_sorted, '- sorted array')


# sorter = Quicksort()
# for array in sorter.history:
#     print(array)

    def my_quicksort(self, array, left=[], right=[], replace_index=0):
        if len(array) > 1:
            
            # print()
            # print(replace_index, '- replace index')
            # for j in range(len(array)):
            #     tmp_array[replace_index+j] = array[j]
            # print(tmp_array, '- tmp')
            # print()

            # IRRELEVANT
            # choosing pivot
            some_point = random.randint(1, len(array)-1)
            in_place = array[some_point]
            print('- starting point, pivot is', array[some_point])
            self.history.append(list(self.tmp_array))
            self.focus.append(replace_index)

            array[0], array[some_point] = array[some_point], array[0]
            
            for j in range(len(array)):
                self.tmp_array[replace_index+j] = array[j]

            # or comment this whole ^(81-90) thing out

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
                            
                            print(self.tmp_array, 'swapped', array[i], 'and', array[index])


            if i is not 0:
                # print(left + array + right, '- before pivot swapping')
                
                
                # swap
                array[0], array[i] = array[i], array[0]

                for j in range(len(array)):
                    self.tmp_array[replace_index+j] = array[j]
                # print(tmp_array, '- tmp')
            self.history.append(list(self.tmp_array))
            self.focus.append(replace_index+i+1)
            print(self.tmp_array, array[i], 'should be in place now')
            # print(left + array + right, array[i], 'should be in place now')


            return self.my_quicksort(array[0:i], left, [array[i]] + array[i+1:len(array)] + right, replace_index) + [array[i]] + self.my_quicksort(array[i+1:len(array)], left + array[0:i] + [array[i]], right, replace_index+i+1)
        else:
            # if len(array) is not 0:
            # print(array)
            return array


# to_sort = [i+1 for i in range(10)]
# random.shuffle(to_sort)
# print(to_sort, '- initial array')
# tmp_array = to_sort
# final = my_quicksort(to_sort)
# print(final)












# print(tmp_array, '- tmp')

# _# choose pivot_
# swap a[1,rand(1,n)]

# _# 2-way partition_
# k = 1
# for i = 2:n, if a[i] < a[1], swap a[++k,i]
# swap a[1,k]
# _→ invariant: a[1..k-1] < a[k] <= a[k+1..n]_

# _# recursive sorts_
# sort a[1..k-1]
# sort a[k+1,n]





# def my_quicksort(array, left=[], right=[], replace_index=0):
#     if len(array) > 1:
        
#         # print()
#         # print(replace_index, '- replace index')
#         # for j in range(len(array)):
#         #     tmp_array[replace_index+j] = array[j]
#         # print(tmp_array, '- tmp')
#         # print()

#         # IRRELEVANT
#         # choosing pivot
#         # some_point = random.randint(1, len(array)-1)
#         # in_place = array[some_point]
#         # print(left + array + right, '- starting point, pivot is', array[some_point])
#         # array[0], array[some_point] = array[some_point], array[0]
        

#         # pivot - element 0
#         print(array, '', array[0], 'is the pivot')
#         i = 0
#         for index, _ in enumerate(array):
#             if index > 0:
#                 if array[index] < array[0]:
#                     i += 1
#                     if i is not index:
#                         print(left + array + right, 'swapping', array[i], 'and', array[index])
                        
                        
#                         # swap
#                         array[i], array[index] = array[index], array[i]

#                         for j in range(len(array)):
#                             tmp_array[replace_index+j] = array[j]
#                         print(tmp_array, '- tmp')

#         if i is not 0:
#             print(left + array + right, '- before pivot swapping')
            
            
#             # swap
#             array[0], array[i] = array[i], array[0]

#             for j in range(len(array)):
#                 tmp_array[replace_index+j] = array[j]
#             print(tmp_array, '- tmp')
            
#         print(left + array + right, array[i], 'should be in place now')


#         return my_quicksort(array[0:i], left, [array[i]] + array[i+1:len(array)] + right, replace_index) + [array[i]] + my_quicksort(array[i+1:len(array)], left + array[0:i] + [array[i]], right, replace_index+i+1)
#     else:
#         # if len(array) is not 0:
#         # print(array)
#         return array