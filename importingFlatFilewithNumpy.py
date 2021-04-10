# Import package
import numpy as np

# Assign filename to variable: file
file = 'mnist_kaggle_some_rows.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=",")

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
import matplotlib.pyplot as plt
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

# Import numpy
import numpy as np

# Assign the filename: file
file = 'digits_header.txt'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows= 1, usecols=[0,2])

# Print data
print(data)

# Assign filename: file
file = 'seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()

# working with mixed data types
# the first argument is the filename,
# the second specifies the delimiter ,
# the third argument names tells us there is a header.
data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)
np.shape(data)

#to get the ith row, merely execute data[i]
#get the column with name 'Fare'
data['Fare']

# another way to work with mixed data types
# Assign the filename: file
file = 'titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file, delimiter=',', names=True, dtype=None)

# Print out first three entries of d
print(d[:3])


