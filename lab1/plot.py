from numpy import array
from binary import binary_search
from linear import linear_search
import matplotlib.pyplot as plt
import time

_, (plt1, plt2) = plt.subplots(nrows=1, ncols=2)
sizes = range(100,100000,100)
linear_besttime = []
linear_worsttime = []
binary_besttime = []
binary_worsttime = []

for size in sizes:
    data =range(size)
    start = time.time()
    linear_search(data,0)
    end = time.time()
    linear_besttime.append(end-start)

plt1.plot(sizes,linear_besttime,"*", label="Best Case of Linear Search")

for size in sizes:
    data =range(size)
    start = time.time()
    linear_search(data,size-1)
    end = time.time()
    linear_worsttime.append(end-start)
plt1.plot(sizes,linear_worsttime,"o", label="Worst Case of Linear Search")
plt1.set_title("Linear Search")
plt1.set_xlabel("Length of Array")
plt1.set_ylabel("Time (in s)")

plt1.legend()

for size in sizes:
    data =range(size)
    start = time.time()
    binary_search(data,0,size-1,(size-1)//2)
    end = time.time()
    binary_besttime.append(end-start)
plt2.plot(sizes,binary_besttime,"*", label="Best Case of Binary Search")

for size in sizes:
    data =range(size)
    start = time.time()
    binary_search(data,0,size-1,-1)
    end = time.time()
    binary_worsttime.append(end-start)
plt2.plot(sizes,binary_worsttime,"o", label="Worst Case of Binary Search")
plt2.set_title("Binary Search")
plt2.set_xlabel("Length of Array")
plt2.set_ylabel("Time (in s)")

plt2.legend()
    
plt.show()
    