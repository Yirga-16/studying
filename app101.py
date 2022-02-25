# # import scipy as sp 
# # import sklearn as skl 
# # from scipy.stats import expon
# # import numpy as np

# # def Inverse_transform_sampling_Exponential(M,lambda_):
# #     expon_x = []

# #     for i in range(M):
# #         u = np.random.uniform(0, 1)
# #         x = expon.ppf(u, lambda_) - 1
# #         expon_x.append(x)

# #     return(np.array(expon_x))

# # exponential_random_samples = Inverse_transform_sampling_Exponential(M = 10000,lambda_ = 1)

# # import matplotlib.pyplot as plt
# # counts, bins, ignored = plt.hist(exponential_random_samples, 25, density = True, color = 'purple')
# # plt.title("Inverse Transform Sampling from Exponential Distribution with Unif(0,1) and Inverse CDF")
# # plt.ylabel("Probability")
# # plt.show()




# ##Rejection
# import numpy as np
# from scipy.stats import norm

# mu_ps = 30
# sigma_ps = 10
# mu_ps2 = 80
# sigma_ps2 = 20

# mu_q = 50
# sigma_q = 30

# def P_star(x):
#     p_x = norm.pdf(x,mu_ps,sigma_ps) + norm.pdf(x,mu_ps2,sigma_ps2)
#     return(p_x)

# def Q(x):
#     q_x = norm.pdf(x,mu_q,sigma_q)
#     return(q_x)

# def Rejection_Sampling_MixtureNormals(M,c):
#     accepted_values = []

#     for i in range(M):
#         x = np.random.normal(mu_q, sigma_q)
#         u = np.random.uniform(0,c * Q(x))

#         if u <= P_star(x):
#             accepted_values.append(x)

#     return(np.array(accepted_values))

# x = np.arange(-10,150)
# c = max(P_star(x) / Q(x))
# X_accepted = Rejection_Sampling_MixtureNormals(M = 100000,c = c)

# import matplotlib.pyplot as plt
# counts, bins, ignored = plt.hist(X_accepted, x, density = True,color = 'purple', label = 'accepted samples')
# plt.title("Rejection Sampling for Mixture of Normal Distribution with Unif(0,cQ(x))")
# plt.ylabel("Probability")
# plt.show()


# import scipy as sp 
# import pandas as pd 
# import math 
# import random
# import matplotlib.pyplot as plt 
# # x = range(10000)
# # for x in x:
# #     f = ((5**x) * math.exp(-5))/math.factorial(x)
# #     print(f)

# lam = 30
# s = 1 #hour
# event = math.exp(1, lam)
# time = event 
# # event = (-1/lam)*math.log(1 - random)
# while event < s:
#     event = event + math.exp(1, lam)
#     if event < s:
#         time = time + lam
#     print(time)
# plt.plot(event, time)
# plt.show()



import numpy as np
import pandas as pd
import math

class Blocking_System:
    def __init__(self, m: int, service, arrival, 
                 arrival_method: str = 'poisson', service_method: str = 'exp'): 
        self.clock=0.0                      #simulation clock
        self.num_service_units=m            #system with m service units
        self.arrival_mtd=arrival_method     #arrival distribution
        self.service_mtd=service_method     #service distribution
        self.param_service=service          #parameter for service dist.
        self.param_arrival=arrival          #parameter for arrival dist.
        self.num_arrivals=0                 #total number of arrivals
        self.t_arrival=self.gen_arrival_time()   #time of next arrival
        self.t_departures=np.ones(m)*100000. #departure times for each service unit (100.000 as infinite)
        self.dep_sums=np.zeros((m,), dtype=int) #Sum of service time
        self.states=np.zeros((m,), dtype=int) #current states
        self.num_of_departures=np.zeros((m,), dtype=int) #number of customers served
        self.lost_customers=0               #customers who left without service
        self.num_in_system=0                #customers in the system


    def time_adv(self):                                                       
        t_departure=min(self.t_departures)
        idx = list(self.t_departures).index(t_departure)
        if self.t_arrival<t_departure:
            self.clock=self.t_arrival
            self.arrival()
        else:
            self.clock=t_departure
            self.departure(idx)


    def arrival(self):              
        self.num_arrivals += 1
        self.num_in_system += 1

        accepted = False
        for idx in range(self.num_service_units):
            if self.states[idx]==0:
                accepted = True
                dep=self.gen_service_time()
                self.dep_sums[idx] += dep
                self.t_departures[idx]=self.clock + dep
                self.states[idx]=1
                break

        self.t_arrival=self.clock+self.gen_arrival_time()
        if not accepted:
            self.lost_customers += 1


    def departure(self, idx: int):
        self.num_of_departures[idx] += 1
        self.t_departures[idx]=100000. # (100.000 as infinite)
        self.states[idx]=0                  


    def gen_arrival_time(self):         #function to generate arrival times 
        if self.arrival_mtd=='erlang':
            return (np.random.gamma(self.param_arrival)) # Erlang distribution (using Gamma with shape=int)
        elif self.arrival_mtd=='hyperexp': # Hyper Exponential distribution p1 = 0.8, λ1 = 0.8333, p2 = 0.2, λ2 = 5.0
            if np.random.uniform() <= 0.8: #p1
                return (np.random.exponential(scale=1./0.833)) #λ1
            else: #p2
                return (np.random.exponential(scale=1./5.)) #λ2
        else:
            return (np.random.poisson()) # Poisson distribution

    
    def gen_service_time(self):         #function to generate service time
        if self.service_mtd=='constant':
            return self.param_service
        if self.service_mtd=='pareto': # Pareto distribution
            u = np.random.uniform()
            return (1 / np.power(u,(1/self.param_service)))
        if self.service_mtd=='normal':
            return (np.random.normal(loc=self.param_service)) # Normal Distribution
        else:
            return (np.random.exponential()) # Exponential distribution (lamda=1)

results = pd.DataFrame([],columns=['run','mean','count','std','CI low limit','CI high limit','CI range'])    
print(results)

m = 10
mu_service = 8
mu_arrival = 1
s=Blocking_System(m, mu_service, mu_arrival)
df=pd.DataFrame(columns=['Fraction of blocked customers','Average interarrival time','Total Customers','Blocked Customers'])

for i in range(10):
    np.random.seed(i)
    s.__init__(m, mu_service, mu_arrival)
    while s.num_in_system <= 10000 :
        s.time_adv() 
    a=pd.Series([s.lost_customers/s.num_arrivals,s.clock/s.num_arrivals,s.num_arrivals,s.lost_customers],index=df.columns)
    df=df.append(a,ignore_index=True)   
    
print(df) 

