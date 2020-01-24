import datetime

class Mergesort:
    counter = 0
    name = 'Mergesort'
    history = []

    def get_counter(self):
        return self.counter

    def get_history(self):
        return self.history

    def sort(self, unsorted_list):
        start = datetime.datetime.now()
        self.mergesort(unsorted_list)
        end = datetime.datetime.now()
        print(end - start)
        return unsorted_list
    
    def mergesort(self, unsorted_list):
        # print("Splitting ",unsorted_list)
        if len(unsorted_list) > 1: 
            mid = len(unsorted_list)//2 #Finding the mid of the unsorted_listay 
            L = unsorted_list[:mid] # Dividing the unsorted_listay elements  
            R = unsorted_list[mid:] # into 2 halves 
    
            self.mergesort(L) # Sorting the first half 
            self.mergesort(R) # Sorting the second half 
    
            i = j = k = 0
            
            # Copy data to temp unsorted_listays L[] and R[] 
            while i < len(L) and j < len(R): 
                # self.counter += 1
                if L[i] < R[j]: 
                    unsorted_list[k] = L[i] 
                    i+=1
                else: 
                    unsorted_list[k] = R[j] 
                    j+=1
                k+=1
            
            # Checking if any element was left 
            while i < len(L): 
                unsorted_list[k] = L[i] 
                i+=1
                k+=1
            
            while j < len(R): 
                unsorted_list[k] = R[j] 
                j+=1
                k+=1

        # print("Merging ",unsorted_list)
