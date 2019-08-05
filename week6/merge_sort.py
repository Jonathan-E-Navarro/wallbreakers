import threading
import logging
import time
import random
import math
final = []
max_len = 20
'''
hardcoded multithreaded merge sort for logic testing
'''

def merge(left, right):
    print("merging: ",left,right)
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

    print('merged: ',merged_list)
    return merged_list

def merge_sort(array):
    print(array)
    if len(array) <= 1:
        return array
    else:
        midpoint = len(array)//2
        left = array[:midpoint]
        right = array[midpoint:]
        print("left: ",left)
        print("right: ",right)
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        merged = merge(sorted_left,sorted_right)
        if len(merged) >= (27/4): 
            print("adding!")
            final.append(merged)
        return merged

  
if __name__ == "__main__":
    test = []
    for i in range(27):
        test.append(random.randint(1,20))

    print(test)
    start = time.time()
    print("starting...")
    for i in range(4):
        low = i * (27 / 4) 
        high = (i + 1) * (27 / 4) - 1
        if  i == 3 and 27%2!=0:
            print("since its odd")
            high=27-1
        print('low: ',low,'high: ',high)
        part = test[low:high+1]
        print(part)
        print("Main    : create and start thread %d." % i)
        x = threading.Thread(target=merge_sort, args=(part,))
        x.start()
        x.join()
        print("\n")

    print(test)
    print(final)
    left = merge(final[0],final[1])
    right = merge(final[2],final[3])
    merge(left,right)
    
    end = time.time()
    print("finished in: ",end - start)




