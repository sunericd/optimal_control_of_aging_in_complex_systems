import numpy as np
import random
import math
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import time
from tqdm import tqdm 
from mpl_toolkits.mplot3d import Axes3D
from model_decoupled import *

exp_name = 'repair'
pop_size = 30
dependency = 0.1
parameter_type = 'r'
parameter_list = np.arange(0,0.1,0.0019)
T1_list = np.arange(0,101,10)
T2_list = np.arange(0,101,10)
T = 100
T_std = 10
highres_step = 1

optimizeBangBang_cluster (exp_name, pop_size, dependency, parameter_type, parameter_list, T1_list, T2_list, T_std, highres_step, T)
