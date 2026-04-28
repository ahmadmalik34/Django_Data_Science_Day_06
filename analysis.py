import numpy as np
from datetime import datetime

def load_stock_data(filepath):
    data=np.genfromtxt(filepath,delimeter=',',skip_header=1)
    dates=data[:,0]