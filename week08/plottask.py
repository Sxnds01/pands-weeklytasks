# Plottask.py
# Wrie a program that displays a histogram of a normal distribution
# of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x^3 in the range 0 to 10, on the one set of axes.

import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from matplotlib import style 

x = np.random.normal(5, 2, 1000)
plt.hist(x, 40)
plt.show()