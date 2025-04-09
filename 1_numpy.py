import numpy as np 


# CREATING NUMPY ARRAYS

arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
arr2d = np.array([[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]])
zeros = np.zeros(10)
ones = np.ones(10)
identity = np.eye(3)

range_arr = np.arange(1, 50, 5) # start, stop, step
# print(range_arr)



# SPECIAL ARRAYS

linespace_arr = np.linspace(1, 1, 5) # five numbers between 1 and 5
# print(linespace_arr)
random_arr = np.random.rand(3, 3) # random numbers between 0 and 1
# print(random_arr) 
random_ints = np.random.randint(0, 10, size=(3, 3))  # 3x3 array of ints 0-9
# print(random_ints)



# ARRAY SLICING

arr = np.array([1,2,3,4,5,6,7,8,9,10])

# print (arr[1:4]) ## prints subarray from index 1 to index 4

# print(arr[::2]) ## print every second element


## AGGREGATION FUNCTIONS


arr = np.array([1,2,3,4,5,6,7,8,9,10])

# print(np.sum(arr)) ## sum of all elements
# print(np.mean(arr)) ## mean of all elements
# print(np.var(arr)) ## variance of all elements
# print(np.std(arr)) ## standard deviation of all elements
# print(np.min(arr)) ## minimum value of all elements
# print(np.max(arr)) ## maximum value of all elements
# print(np.argmin(arr)) ## index of minimum value