from functions import frequency
import extract_data as ed
import matplotlib.pyplot as plt
import numpy as np
import graph as gh
import sys
themain=ed.titles('../data/breast-cancer-cell-data.csv',int(sys.argv[1]))


print('length of all parameters is {}'.format(len(themain)))