from math import factorial as f

def c(n,r):
	return int(f(n)/(f(r)*f(n-r)))

paths = 0
for i in range(21):
	paths += c(20,i)**2

print(paths)