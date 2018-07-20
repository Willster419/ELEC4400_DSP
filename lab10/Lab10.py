#######################
#Willard Wider
#7/20/18
#ELEC4400
#Lab 10
#######################

import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft
from scipy.signal import lfilter, freqz

#specify the stype of the plot to use
plt.style.use('ggplot')

#problem 1 - FFT and IFFT
#make the time domain signal. 1000 data points, 2 seconds in duration
x_index = np.linspace(0,2,1000)

#define the input signal
input_singal = np.cos(2*np.pi*10*x_index) + np.cos(2*np.pi*100*x_index) + np.cos(2*np.pi*200*x_index)

#the fft of the input signal
x_index_frequency = np.linspace(0,500,1000)
fft_input_out = fft(input_singal)

#the inverse fft of the fft (meta)
i_fft_input_out = ifft(fft_input_out)

#create three graphs for plotting
#graph of first plot
f,xarr = plt.subplots(3)
xarr[0].set_title('noisy signal')
xarr[0].plot(x_index,input_singal)

#graph of fft of first
xarr[1].set_title('fft out')
#https://stackoverflow.com/questions/15858192/how-to-set-xlim-and-ylim-for-a-subplot-in-matplotlib
xarr[1].set_xlim([0,250])
xarr[1].plot(x_index_frequency,np.abs(fft_input_out))

#graph of inverse of fftr
xarr[2].set_title('ifft')
xarr[2].plot(x_index,i_fft_input_out)

plt.show()

#problem 2 - time domain filtering
N = 15
b = (1/N)*np.ones(N)
filtered_output = lfilter(b,1,input_singal)

p2_f,p2_xarr = plt.subplots(2)
#signal first
p2_xarr[0].set_title('noisy signal')
p2_xarr[0].plot(x_index,input_singal)

p2_xarr[1].set_title('filtered signal')
p2_xarr[1].plot(x_index, filtered_output)

plt.show()


#probmel 3 - frequency domain filtering
hz,H = freqz(b,1,worN=x_index_frequency*2*np.pi/1000)

hzTrue = hz*1000/(2*np.pi)

fft_input_out_filtered = fft_input_out*H

#create three graphs for plotting
#graph of first plot
p3_f,p3_xarr = plt.subplots(3)
p3_xarr[0].set_title('noisy fft signal')
p3_xarr[0].set_xlim([0,250])
p3_xarr[0].plot(x_index_frequency,np.abs(fft_input_out))

#graph of filter frequency response
p3_xarr[1].set_title('filter frequency response')
p3_xarr[1].set_xlim([0,250])
p3_xarr[1].plot(hzTrue,H)

#graph result of frequncy domain filtering
p3_xarr[2].set_title('frequency domain filtered signal')
p3_xarr[2].set_xlim([0,250])
#xarr[1].plot(x_index_frequency,np.abs(fft_input_out))
p3_xarr[2].plot(x_index_frequency,np.abs(fft_input_out_filtered))

plt.show()

#problem 4 - Prestige
p4_f,p4_xarr = plt.subplots(4)

#graph of time domain filtering method
p4_xarr[0].set_title('time domain filtering, time domain')
p4_xarr[0].plot(x_index, filtered_output)

#graph of fft of time domain filter
p4_xarr[1].set_title('time domain filtering, frequency domain')
time_domain_fft = fft(filtered_output)
p4_xarr[1].set_xlim([0,250])
p4_xarr[1].plot(x_index_frequency, np.abs(time_domain_fft))

#graph of frequency domain filter, feqeucncy domain
p4_xarr[2].set_title('frequency domain filtering, frequency domain')
p4_xarr[2].set_xlim([0,250])
p4_xarr[2].plot(x_index_frequency,np.abs(fft_input_out_filtered))

#graph of frequency domain filter, time domain
p4_xarr[3].set_title('frequency domain filtering, time domain')
time_domain_ifft = ifft(fft_input_out_filtered)
p4_xarr[3].plot(x_index,time_domain_ifft)
plt.show()