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
i=0
L= file.readSignal(i)
# L = L[Fs*40*60:Fs*60*60]
t = np.arange(len(L))/Fs/60
#M = (L - R) /2
k = int(Fs * 0.5)
#f, t2, Sxx = signal.spectrogram(L, Fs, nperseg= k, nfft= k, noverlap=int(Fs*0.5), scaling  ="density",mode ='psd')
f, t2, Sxx = signal.spectrogram(L, Fs, nperseg= k, nfft= k, noverlap=k-10, scaling  ="spectrum",mode ='psd')
Sxx = 10*np.log10(Sxx)
Sxx[Sxx>16]=16
Sxx[Sxx<-19]=-19
# Sxx = ndimage.filters.gaussian_filter(Sxx,1)
fmax = 30
findex =np.where(f>fmax)[0][0]

#Sxx = Sxx/ np.mean(Sxx,axis=0)

plt.figure()
plt.subplot(2,1,1)
plt.title(signal_labels[i])
#plt.title('Test_2 : 14fev2019')
plt.plot(t,L)
plt.subplot(2,1,2)
#plt.pcolormesh(t2, f[:findex], np.log10(Sxx[:findex,:])** 0.9,cmap='hot')
# plt.pcolormesh(t2, f[:findex],  Sxx[:findex,:] ** 1, cmap='jet')
plt.pcolormesh(t2, f[:findex], Sxx[:findex,:],cmap='jet')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar()
plt.show()
    # plt.subplot(3,1,3)
    # plt.specgram(L, NFFT=Fs*2, Fs=Fs, noverlap=Fs*1)