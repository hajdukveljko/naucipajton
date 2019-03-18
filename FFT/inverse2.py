from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import math

sampFreq, snd = wavfile.read('hromatic_original.wav')
N = snd.size
time_array = np.arange(0, N, 1.0)
time_array = time_array/sampFreq
time_array = time_array * 1000  # miliseconds
s1 = snd/2.**15
plt.plot(time_array, s1)
plt.xlabel('Time(ms)')
plt.ylabel('Amplitude')
plt.title("Input Signal")
plt.show()

fft_orig = np.fft.fft(snd)
nUniquePts = math.ceil((N+1)/2.0)
fft_real = fft_orig[0:nUniquePts]
mx = abs(fft_real)
mx = mx/float(N)
mx = mx**2
if N & 2 > 0:
    mx[1:] = 2 * mx[1:]
else:
    mx[1:-1] = 2 * mx[1:-1]
f = sampFreq/N * np.arange(0, nUniquePts) # frequency vector
# plotting
fig,ax = plt.subplots()
plt.plot(f,mx,linewidth=5)
ax.set_xscale('log')
ax.set_yscale('log')
plt.title("Fourie Transform of Input Signal")
plt.ylabel('Amplitude')
plt.xlabel('Frequency [Hz]')
plt.show()

# find point of freq 1000
for i in range(len(fft_real)):
    if sampFreq/N * i >= float(1000):
        print(i)
        break

my_fft = fft_orig
my_fft[0:i] = 0
my_fft[-i+1:] = 0

mx_new = mx
mx_new[:i] = 0
new_sig = np.fft.ifft(my_fft)
print(new_sig.dtype)
new_sig = new_sig.astype(int16)

fig,ax = plt.subplots()
plt.plot(f, mx_new,linewidth=5)
plt.title("Fourie Transform of New Signal")
ax.set_xscale('log')
ax.set_yscale('log')
plt.ylabel('Amplitude')
plt.xlabel('Frequency [Hz]')
plt.show()

wavfile.write('hromatic_1000_cut.wav', sampFreq, new_sig)