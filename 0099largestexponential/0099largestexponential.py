import numpy as np
import math

exponentials = np.loadtxt('0099largestexponential\\0099_base_exp.txt',delimiter=',',dtype=int)

maxvalue = 0
maxline = -1
for i in range(len(exponentials)):
	exponential = exponentials[i]
	if maxvalue < math.log(exponential[0]) * exponential[1]:
		maxvalue = math.log(exponential[0]) * exponential[1]
		maxline = i + 1
print(maxline)