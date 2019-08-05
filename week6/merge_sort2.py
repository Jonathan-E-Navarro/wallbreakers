import threading
import time
import random 
'''
multi threaded merge sort with input 
user inputs size of random array to be sorted 
'''
class Threaded_Merge_sort(object):
    def __init__(self,size):
        self.test = []
        self.final = []
        self.size = size 

    def merge(self,left,right):
        # print("merging: ",left,right)
        if len(left) == 0:
            return right
        elif len(left) == 0:
            return left
        
        left_index = 0
        right_index = 0
        merged_list = []  

        list_len_target = len(left) + len(right)
        while len(merged_list) < list_len_target:
            if left[left_index] <= right[right_index]:
                merged_list.append(left[left_index])
                left_index += 1
            else:
                merged_list.append(right[right_index])
                right_index += 1
                
            if right_index == len(right):
                merged_list += left[left_index:]
                break
            elif left_index == len(left):
                merged_list += right[right_index:]
                break

        # print('merged: ',merged_list)
        return merged_list

    def merge_sort(self,array,depth=0):
        # print(array)
        if len(array) <= 1:
            return array
        else:
            midpoint = len(array)//2
            left = array[:midpoint]
            right = array[midpoint:]
            # print("left: ",left)
            # print("right: ",right)
            sorted_left = self.merge_sort(left,depth+1)
            sorted_right = self.merge_sort(right,depth+1)
            merged = self.merge(sorted_left,sorted_right)
            if len(merged) >= (self.size//4) and depth == 0: 
                # print("adding!")
                self.final.append(merged)
            return merged


    def threaded_sort(self):
        for i in range(self.size):
            self.test.append(random.randint(1,20))
        # print(self.test)
        start = time.time()
        if self.size == 1:
            final_list = self.test

        else:
            for i in range(4):
                # print(self.size)
                low = i * (self.size // 4) 
                high = (i + 1) * (self.size // 4) - 1
                if i == 3 : 
                    # print('adding the rest')
                    high = self.size-1
                # print('low: ',low,'high: ',high)
                part = self.test[low:high+1]
                # print(part)
                # print("Main    : create and start thread %d." % i)
                x = threading.Thread(target=self.merge_sort, args=(part,))
                x.start()
                x.join()
                # print("\n")

            # print(self.test)
            # print(self.final)
            # left = self.merge(self.final[0],self.final[1])
            # right = self.merge(self.final[2],self.final[3])
            # final_list = self.merge(left,right)
            final_list = []

            while self.final:
                left = final_list
                right = self.final.pop(0)
                final_list = self.merge(left,right)

        print("inital list: ",self.test)
        print("final list: ",final_list)
        # print("len: ",len(final_list))

        end = time.time()
        print("finished in: ",end - start)

    

if __name__ == "__main__":
    # threaded = Threaded_Merge_sort(299)
    # threaded.threaded_sort()
    while True:
        num = input("input the size of random array you want sorted: ")
        if num.isdigit():
            threaded = Threaded_Merge_sort(int(num))
            threaded.threaded_sort()
        elif num == "exit()":
            break
        else:
            print("please input a digit")
    