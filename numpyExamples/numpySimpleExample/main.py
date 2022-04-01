import numpy as np
firstArray = np.array([0, 1, 2, 3, 4, 5, 7, 8, 9])
print(firstArray)

lnsArray = np.linspace(start=0, stop=100, num=100, dtype=np.int)
print(lnsArray)

arnArray = np.arange(start=20)
print(arnArray)

zerosArray = np.zeros([3, 3])
print(zerosArray)

onesArray = np.ones([4, 4])
print(onesArray)

# reshape
reShapedArray = arnArray.reshape(4, 5)
print(reShapedArray)
print(reShapedArray[0])
