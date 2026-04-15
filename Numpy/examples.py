import numpy as np

#Normalizing array

#standardization method
arr =np.array([10,20,30])
norm = (arr - np.mean(arr))/np.std(arr)
print(norm)

#min-max method
norm2 = (arr - np.min(arr))/(np.max(arr)-np.min(arr))
print(norm2)

#find rows with max value
a = np.array([[1,2,3],[4,5,6]])
row_idx = np.argmax(a , axis=1)
print(row_idx)

#


