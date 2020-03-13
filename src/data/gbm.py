import numpy as np
from .base import Price

class GBM(Price):
    """Brownian motion."""

    def __init__(self, T=1., sigma1=0.02, sigma2=0.01, s1=1., s2=1.,
                 drift1=0., drift2=0., n=100):
        self.sigma1 = sigma1
        self.sigma2 = sigma2
        self.drift1 = drift1
        self.drift2 = drift2
        self.n = n
        self.s1 = s1
        self.s2 = s2
        self.T = T

    def generate(self):
        dt1 = self.sigma1 ** 2 * self.T / self.n
        dt2 = self.sigma2 ** 2 * self.T / self.n

        bm1 = np.r_[[0.], np.sqrt(dt1) * np.random.randn(self.n - 1).cumsum()]
        bm2 = np.r_[[0.], np.sqrt(dt2) * np.random.randn(self.n - 1).cumsum()]

        path = np.c_[np.linspace(0, self.T, self.n), bm1, bm2]
        path[:, 1] = np.exp((self.drift1 - self.sigma1 ** 2 / 2.) * path[:, 0] + self.sigma1 * path[:, 1])
        path[:, 2] = np.exp((self.drift2 - self.sigma2 ** 2 / 2.) * path[:, 0] + self.sigma2 * path[:, 2])

        path[:, 1] *= self.s1
        path[:, 2] *= self.s2


        return path
