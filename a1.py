# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import numpy.matlib as mat


alpha = np.full((1, 4), 1/4)
alpha_2 = np.full((4, 1), 1/4)
P = np.matrix(  [[0, 1, 0, 0], 
                [ 1/4, 0, 3/4, 0],
                [0, 1/4, 0,  3/4],
                [0, 0, 1, 0 ]]
               )

beta = alpha * P
P3 = np.linalg.matrix_power(P,3) 
P2 = np.linalg.matrix_power(P,2) 
beta_2 = alpha*np.linalg.matrix_power(P,3) 