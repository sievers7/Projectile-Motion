import numpy as np
import math as m
import matplotlib.pylab as plot
 
v = 30
g = 9.8
theta = np.arange(m.pi/6, m.pi/3, m.pi/36)
t = np.linspace(0,5, num =100)
for i in theta:
   x1 = []
   y1 = []
   for k in t:
       x = ((v*k)*np.cos(i))
       y = ((v*k)*np.sin(i))-((0.5*g)*(k**2))
       x1.append(x)
       y1.append(y)
   p = [i for i, j in enumerate(y1) if j < 0]
   for i in sorted(p, reverse = True):
       del x1[i]
       del y1[i]
 
   plot.plot(x1, y1)
 
plot.show()
