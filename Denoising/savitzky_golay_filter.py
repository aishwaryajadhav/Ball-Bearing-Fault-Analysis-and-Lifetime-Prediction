
#import scipy.signal.savgol filter
def savitzky_golay(y, window_size, order):
    import numpy as np
    from math import factorial

    try:
        window_size = np.abs(np.int(window_size))
        order = np.abs(np.int(order))
    except ValueError, msg:
        raise ValueError("window_size and order have to be of type int")
    
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    
    if window_size < order + 2:
        raise TypeError(”window_size is too small for the polynomials order”)
    
    order range = range(order+1)
    half window = (window_size -1) // 2
    b = np.mat([[k**i for i in order range] for k in range(-half window, half window+1)])
    m = np.linalg.pinv(b).A[0]
    firstvals = y[0] - np.abs( y[1:half window+1][::-1] - y[0] )
    lastvals = y[0] + np.abs(y[-half window-1:-1][::-1] - y[0] )
    y = np.concatenate((firstvals, y, lastvals))

    return np.convolve( m[::-1], y, mode=’valid’)



