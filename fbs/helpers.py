"""
Helper methods
"""

import math
import numpy as np
from scipy.stats import norm


class Option:
    def __init__(self, spot_price, exercise_price, risk_free_rate, std, expiration):
        """
        :param spot_price: spot price of the underlying asset at t0, float, required
        :param exercise_price: exercise price of the option, float, required
        :param risk_free_rate: float, required
        :param std: standard deviation of the return rate of P, float, required
        :param expiration: time to expiration, float, required
        :return: None
        """

        self.s = spot_price
        self.k = exercise_price
        self.r = risk_free_rate
        self.std = std
        self.t = expiration

    def compute_eu_call_price(self):
        """
        Determine the value of an European call option
        :return:
        """

        d1 = self.compute_d1()
        d2 = self.compute_d2()

        price = self.s * norm.cdf(d1) - self.k * math.exp(- self.r * self.t) * norm.cdf(d2)

        return price

    def compute_d1(self):
        """
        Determine d1 coefficient
        :return: float
        """

        numerator = (np.log(self.s / self.k) + (self.r + (self.std**2 / 2)) * self.t)
        denominator = self.std * np.sqrt(self.t)

        d1 = numerator / denominator

        return d1

    def compute_d2(self):
        """
        Determine d2 coefficient
        :return: float
        """

        d1 = self.compute_d1()
        d2 = d1 - self.std * np.sqrt(self.t)

        return d2
