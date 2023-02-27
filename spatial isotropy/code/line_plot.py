##plot for line plot

import numpy as np
import matplotlib.pyplot as plt
import math

opacity=1 
##line for the curve
data=np.loadtxt('line_veg.txt')
print(data.shape)
x=data[:,0]
y=data[:,1]

plt.plot(x,y,c='black',alpha=opacity,linewidth=2,linestyle='solid' )
plt.yticks(np.arange(0, 0.2, 0.05))
plt.xlim(xmax = 120, xmin = 0)
##plt.title('Connectivity curve')
plt.ylabel('Connectivity')
plt.xlabel('Lag')
##plt.show()
plt.savefig('line_veg.png',dpi=300)
plt.clf()
   
