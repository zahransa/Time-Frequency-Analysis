import numpy as np
import pyedflib
import matplotlib.pylab as plt
from scipy import signal
from scipy import ndimage
#import scipy.io
#f = scipy.io.loadmat('Subject1.mat')


Fs =500


file = pyedflib.EdfReader('band0.5-30hz.edf')

n = file.signals_in_file
signal_labels = file.getSignalLabels()


# sigbufs = np.zeros((n, f.getNSamples()[0]))
#for i in np.arange(n):
#     sigbufs[i, :] = f.readSignal(i)
#
# #ts= int(233 * Fs)
# #te= int((233+5) * Fs)
# #sigbufs = sigbufs[:,ts:te]
# t = np.arange(sigbufs.shape[1])/Fs/60
#
# L = sigbufs[4, :]

#['EEG Fp1', 'EEG Fp2', 'EEG F3', 'EEG F4', 'EEG C3', 'EEG C4', 'EEG P3', 'EEG P4', 'EEG O1', 'EEG O2', 'EEG F7', 'EEG F8', 'EEG T7', 'EEG T8', 'EEG P7', 'EEG P8', 'EEG Fz', 'EEG Cz', 'EEG Pz', 'EEG Oz', 'EEG FC1', 'EEG FC2', 'EEG CP1', 'EEG CP2', 'EEG FC5', 'EEG FC6', 'EEG CP5', 'EEG CP6', 'EEG TP9', 'EEG TP10', 'EEG POz', 'ECG ECG', 'ECG ECG2', 'EOG HEOG', 'EOG VEOG']
i=5
L= file.readSignal(i)
# L = L[Fs*40*60:Fs*60*60]
t = np.arange(len(L))/Fs/60
dt = t[1] - t[0]

Y = np.fft.fft(L)
N = len(Y)//2+ 1
f = np.linspace(0, Fs/2, N, endpoint=True)


YALPHA = np.zeros(Y.shape)
print(YALPHA)
Alpha_f =[np.where(f>8)[0][0],np.where(f>12)[0][0]]
YALPHA[Alpha_f[0]:Alpha_f[1]] = Y[Alpha_f[0]:Alpha_f[1]]
YALPHA[-Alpha_f[1]:-Alpha_f[0]] = Y[-Alpha_f[1]:-Alpha_f[0]]
print(Alpha_f)


YDELTA= np.zeros(Y.shape)
DELTA_f =[0,np.where(f>4)[0][0]]
YDELTA[DELTA_f[0]:DELTA_f[1]] = Y[DELTA_f[0]:DELTA_f[1]]
YDELTA[-DELTA_f[1]:-DELTA_f[0]] = Y[-DELTA_f[1]:-DELTA_f[0]]

YTHETA= np.zeros(Y.shape)
THETA_f =[np.where(f>4)[0][0],np.where(f>8)[0][0]]
YTHETA[THETA_f[0]:THETA_f[1]] = Y[THETA_f[0]:THETA_f[1]]
YTHETA[-THETA_f[1]:-THETA_f[0]] = Y[-THETA_f[1]:-THETA_f[0]]


YBETA= np.zeros(Y.shape)
BETA_f =[np.where(f>12)[0][0],np.where(f>30)[0][0]]
YBETA[BETA_f[0]:BETA_f[1]] = Y[BETA_f[0]:BETA_f[1]]
YBETA[-BETA_f[1]:-BETA_f[0]] = Y[-BETA_f[1]:-BETA_f[0]]

plt.subplot(611)
plt.plot(Y)
plt.plot(YDELTA)
plt.plot(YTHETA)
plt.plot(YALPHA)
plt.plot(YBETA)
plt.subplot(612)
plt.plot(t,L)
plt.subplot(613)
plt.plot(t,np.fft.ifft(YDELTA))
plt.subplot(614)
plt.plot(t,np.fft.ifft(YALPHA))

#plt.plot(t,np.fft.ifft(YTHETA))
#plt.subplot(615)
#plt.plot(t,np.fft.ifft(YALPHA))
#plt.subplot(616)
#plt.plot(t,np.fft.ifft(YBETA))
plt.show()

