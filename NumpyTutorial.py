import numpy as np

#Creates an array of zeros
np.zeros(5)

#Creates a 2D array 3 downwards and 4 accross
a = np.zeros((3,4))
a
#prints the shape of 'a'
print(a.shape)

# equal to len(a.shape)
a.ndim  

#Prints total array size
print(a.size)


import matplotlib.image as mpimg
from matplotlib import pyplot as plt

imgArray=mpimg.imread('ap.jpg')
plt.imshow(imgArray, interpolation='nearest')
plt.show()

#Print the numbers that corospond to the image
#print(imgArray)

#makes two lots of 3x4 arrays filled with 'Zeros'
np.zeros((2,3,4))
type(np.zeros((3,4)))

#Makes an array and fills it with 'Ones'
np.ones((3,4))

#Creates a full array with pi
np.full((3,4), np.pi)

#Manually filling an array
np.array([[1,2,3,4], [10,20,30,40]])

#Create array in range
np.arange(1, 15)

#Create a array with a range but also give an incriment value
np.arange(1, 7, 0.5)

#Creates a array with 'x' number of points evenly distributed
print(np.linspace(0, 80, 6))

#create an array of size then randomly fill it
np.random.rand(3,4)



#draw chart
plt.hist(np.random.rand(100000), normed=True, bins=100, histtype="step", color="blue", label="rand: Uniform")
plt.hist(np.random.randn(100000), normed=True, bins=100, histtype="step", color="red", label="randn: Normal")
plt.axis([-2.5, 2.5, 0, 1.1])
plt.legend(loc = "upper left")
plt.title("Random distributions")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()