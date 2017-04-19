#!/usr/bin/python

#The following statements are used to import numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, np.pi, .001);
print (x)
y = np.sin(x)
print (y)
plt.plot(x, y) 
#plt.show()

# TODO fill in this function
def integrate(y, dx):
	counter = 0
	for i in range(0, len(y)):
		counter += dx * y[i] 
	return counter

p = integrate(np.sin(x), 0.05)
print (p)


		
# TODO write code here to setup arrays x and y = sin(x) and then plot them.
# After this is done implement your integrate function above integrate y
