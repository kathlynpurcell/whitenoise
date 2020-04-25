# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:48:14 2020

@author: kpurc
 
Help from the following:
https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.normal.html
https://datatofish.com/plot-histogram-python/
https://jakevdp.github.io/PythonDataScienceHandbook/04.06-customizing-legends.html
https://pythontic.com/visualization/charts/autocorrelation
https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.linregress.html
https://medium.com/future-vision/plotting-equations-in-python-d0edd9f088c8
https://machinelearningmastery.com/white-noise-time-series-python/
https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.fftconvolve.html
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import stats
from pandas.plotting import autocorrelation_plot
from scipy import signal


length, mean, std = 1000000, 1, 0.1
bin10, bin20, bin50, bin100, bin200 = 10, 20, 50, 100, 200
sig1, sig2, sig3, sig4, sig5 = 0,0,0,0,0

#1
smpl = np.random.normal(mean, std, length)

#2
fig1=plt.figure(1)
plt.hist(smpl, bin10, label='bin 10'), plt.hist(smpl, bin20, label='bin 20')
plt.hist(smpl, bin50, label='bin 50')
plt.hist(smpl, bin100,label='bin 100'), plt.hist(smpl, bin200,label='bin 200')
plt.title('Histogram of White Noise Timeseries')
plt.xlabel('Mean Value')
plt.ylabel('Occurance Rate')
plt.legend()
plt.show()


#3


autocorr = signal.fftconvolve(smpl, smpl[::-1], mode='full')
fig2 = plt.figure(2)
plt.plot(np.arange(-len(smpl)+1,len(smpl)), autocorr)
plt.title('Autocorrelation of White Noise')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.show()



#4
n=0
while n != 1000000:
    if (1.1 > smpl[n] > 0.9):
        sig1 = sig1+1
    elif (1.2 > smpl[n] > 0.8):
        sig2 = sig2+1
    elif (1.3 > smpl[n] > 0.7):
        sig3 = sig3+1
    elif (1.4 > smpl[n] > 0.6):
        sig4 = sig4+1
    elif (1.5 > smpl[n] > 0.5):
        sig5 = sig5+1
    n=n+1
    
per1= sig1/length
per2= (sig2+sig1)/length
per3= (sig3+sig2+sig1)/length
per4= (sig4+sig3+sig2+sig1)/length
per5= (sig5+sig4+sig3+sig2+sig1)/length

print("1:", per1, sig1, "\n2:", per2, sig2, "\n3:", per3, sig3,"\n4:",per4, sig4,"\n5:",per5, sig5)


#5
x = [i for i in range(1000000)]
csum = np.cumsum(smpl)

slope, intercept, r_value, p_value, std_err = stats.linregress(x,csum)
print(slope, " ", intercept, "", r_value)


w = np.array(range(1000000))
y = slope*w + intercept
fig3=plt.figure(3)
plt.scatter(x, csum, label='Cumlative Sum')
plt.plot(w, y, color='r', label='Slope from Linregress') 
plt.title('Cumulative Function of White Noise Timescale')
plt.xlabel('Index Value')
plt.ylabel('Cumulative Values')     
plt.legend(loc="upper left")
plt.show()



    





