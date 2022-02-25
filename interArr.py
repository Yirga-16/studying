import sys
import random
import math


def draw_poisson_inter_arrival_gap(lambda_mean_arrival_rate):
    """
    Draw a poisson inter-arrival gap.
    It uses random as random source, so be sure to set random.seed(...) beforehand for reproducibility.
    E.g.:
    If lambda = 1000, then mean gap is 0.001
    If lambda = 0.1, then mean gap is 10
    :param lambda_mean_arrival_rate:     Lambda mean arrival rate (i.e., every 1 in ... an event arrives)
    :return: Value drawn from the exponential distribution (i.e., Poisson inter-arrival distribution)
    """
    return - math.log(1.0 - random.random(), math.e) / lambda_mean_arrival_rate

print(draw_poisson_inter_arrival_gap(0.04))