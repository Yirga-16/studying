import random
inart = 0
art = 0
print("Customer No.\t\tInter Arrival Time\tArrival Time")
for k in range(1, 20):
 if k == 1:
     print("%i \t\t\t -\t\t\t %i" % (k, art))
       
 else:
     print("%i \t\t\t %i \t\t\t %i" % (k, inart, art))
#take random inetarrival time

 inart: int = random.randrange(1, 100)
 art = inart + art
#library

from numpy import random
import seaborn as sns 
#possion graph

import matplotlib.pyplot as plt
sns.displot(random.poisson(lam=2, size=1000) ,color = 'yellow')
plt.show()