import numpy as np
from datetime import datetime

def load_stock_data(filepath):
    data=np.genfromtxt(filepath,delimeter=',',skip_header=1)
    dates=data[:,0]
    open=data[:,1]
    highs=data[:,2]
    lows=data[:,3]
    closes=data[:,4]
    volumes=data[:,5]
    return{
        'dates':dates,
        'open':open,
        'highs':highs,
        'lows':lows,
        'closes':closes,
        'volumes':volumes
    }