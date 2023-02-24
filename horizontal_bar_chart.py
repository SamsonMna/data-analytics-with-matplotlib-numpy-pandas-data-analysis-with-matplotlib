# coding: utf-8
import turtle

import numpy as np

import pandas as pd

import pickle

from sqlalchemy import create_engine

from pandas.io.json import json_normalize

import pymongo
import matplotlib.dates as mdates
import datetime
import math
from pylab import *
import matplotlib.pyplot as plt
index = np.arange(5)
values1 = [5, 7, 3, 4, 6]
std1 = [0.8, 1, 0.4, 0.9, 1.3]
plt.title("A Horizontal Bar Chart")
plt.barh(index, values1, xerr=std1, error_kw={'ecolor': '0.1', 'capsize': 6}, alpha=0.7, label='First')
plt.yticks(index+0.4, ['A', 'B', 'C', 'D', 'E'])
plt.legend(loc=5)
plt.show()
