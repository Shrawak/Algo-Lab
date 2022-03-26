from random import random
import time
from insertion import insertion_sort
from merge import merge_sort
import matplotlib.pyplot as plt
import random

_, (plt1, plt2) = plt.subplots(nrows=1, ncols=2)
insertion_size = range(10, 1000, 10)
merge_size = range(100, 10000, 100)

insertion_bestcase = []
insertion_worstcase = []
insertion_averagecase = []
merge_bestcase = []
merge_worstcase = []

for size in insertion_size:
    values = list(range(size))
    start_time = time.time()
    insertion_sort(values)
    end_time = time.time()
    insertion_bestcase.append((end_time-start_time)*10**6)

for size in insertion_size:
    values = list(range(size))
    random.shuffle(values)
    start_time = time.time()
    insertion_sort(values)
    end_time = time.time()
    insertion_averagecase.append((end_time-start_time)*10**6)    
    
for size in insertion_size:
    values = list(reversed(range(size)))
    start_time = time.time()
    insertion_sort(values)
    end_time = time.time()
    insertion_worstcase.append((end_time-start_time)*10**6)

plt1.plot(insertion_size, insertion_bestcase, '*', label='Best Case')
plt1.plot(insertion_size, insertion_averagecase, 'x', label='Average Case')
plt1.plot(insertion_size, insertion_worstcase, 'o', label='Worst Case')

plt1.set_title("Insertion Sort")
plt1.set_xlabel("Length of Array")
plt1.set_ylabel("Time (in microsecond)")

plt1.legend()
    
for size in merge_size:
    values = list(range(size))
    start_time = time.time()
    merge_sort(values, 0, size-1)
    end_time = time.time()
    merge_bestcase.append((end_time-start_time)*10**6)
    
for size in merge_size:
    values = list(reversed(range(size)))
    start_time = time.time()
    merge_sort(values, 0, size-1)
    end_time = time.time()
    merge_worstcase.append((end_time-start_time)*10**6)
    
plt2.plot(merge_size, merge_bestcase, '*', label='Best Case')
plt2.plot(merge_size, merge_worstcase, 'o', label='Worst Case')

plt2.set_title("Merge Sort")
plt2.set_xlabel("Length of Array")
plt2.set_ylabel("Time (in microsecond)")

plt2.legend()

plt.show()