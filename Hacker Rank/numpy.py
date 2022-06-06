import numpy

# import numpy

# my_array = numpy.array([1,2,3,4,5,6])
# print numpy.reshape(my_array,(3,2))

# #Output
# [[1 2]
# [3 4]
# [5 6]]

array = numpy.array(list(map(int,input().split())))
print(numpy.reshape(array,(3,3)))

# Transpose

# We can generate the transposition of an array using the tool numpy.transpose.
# It will not affect the original array, but it will create a new array.

# import numpy

# my_array = numpy.array([[1,2,3],
#                         [4,5,6]])
# print numpy.transpose(my_array)

# #Output
# [[1 4]
#  [2 5]
#  [3 6]]
# Flatten

# The tool flatten creates a copy of the input array flattened to one dimension.

# import numpy

# my_array = numpy.array([[1,2,3],
#                         [4,5,6]])
# print my_array.flatten()

# #Output
# [1 2 3 4 5 6]


n,m = input().split()
y=''
z=[]
for i in range(int(n)):
    z.append(list(map(int,input().split())))
array=numpy.array(z)
print(numpy.transpose(array))
print(array.flatten())