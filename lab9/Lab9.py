#######################
#Willard Wider
#7/11/18
#ELEC4400
#Lab 9
#######################

import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile
import time

def myOwnDFT(u):
    N = len(u)
    Un = []
    for n in np.arange(0,N):
        Uk=0
        for k in np.arange(0,N):
            Uk+=u[k]*np.exp((-1*2j*np.pi*k*n)/N)
        Un.append(Uk)
    return Un

if __name__ == "__main__":
    #specify the stype of the plot to use
    plt.style.use('ggplot')
    #make a sine wave, duration 1s
    x_index = np.linspace(0,1,500)
    x_index_frequnecy = np.arange(len(x_index))
    print("making sine wave 10hz...")
    y_values_10 = np.sin(2*np.pi*10*x_index)
    fourier_10 = myOwnDFT(y_values_10)
    print("making sine wave 20hz...")
    y_values_20 = np.sin(2*np.pi*20*x_index)
    fourier_20 = myOwnDFT(y_values_20)
    print("making sine wave 30hz...")
    y_values_30 = np.sin(2*np.pi*30*x_index)
    fourier_30 = myOwnDFT(y_values_30)

    #create the three graphs for fourier frequency plotting
    f,xarr = plt.subplots(3)
    xarr[0].set_title('10-30Hz analysis')
    xarr[0].plot(x_index_frequnecy, fourier_10)
    xarr[1].plot(x_index_frequnecy, fourier_20)
    xarr[2].plot(x_index_frequnecy, fourier_30)
    plt.show()

    #show how long it takes for each sample ammount
    samples_array = [200,400,600,800,1000]
    time_array = []
    for i in samples_array:
        time_x_index = np.linspace(0,1,i)
        #https://docs.python.org/3/tutorial/inputoutput.html
        print(f'running transform for {i} samples...')
        time_y_values = np.sin(2*np.pi*10*time_x_index)
        #start the timer
        start_time = time.time()#time since epoch
        time_fourier = myOwnDFT(time_y_values)
        time_array.append(time.time()-start_time)
    plt.plot(samples_array,time_array)
    plt.title('time of running each transform')
    plt.show()

    #estimate how long it will abe to run a transform of the wave file we used
    print(f'it took {time_array[4]} to run a fourier transform of {samples_array[4]} samples')
    fs, data = wavfile.read('kpt.wav')
    print(f'the wavefile from previous lab is {len(data)} sampels...') #should be 561,152
    ratio = time_array[4] / samples_array[4]
    print(f'thus it will take {ratio*len(data)} to complete this one')
    
    #analyse the smaller sample to find the wave used
    print('analysing the smaller sample...')
    #https://stackoverflow.com/questions/2060628/reading-wav-files-in-python
    fs, data = wavfile.read('kpt1note2k.wav')
    #fast fourier transform of the data
    #fftOut = fft(data)
    fftOut = myOwnDFT(data)
    #total ammount of time in the recording
    length = len(data) / fs
    #a list of sample indicies, probably audio frames
    n = np.arange(len(data))
    #fs the the sampling frequency, the number of samples per second
    #we need the duration of time between samples
    #time between is 1 (sec) divided by frequency
    total_frequencies = n / length
    plt.plot(total_frequencies,np.abs(fftOut))
    #limit the plot
    plt.xlim(([0,4186]))
    plt.title("Piano Note Analysis")
    plt.xlabel("frequency (Hz)")
    plt.ylabel("amplitude (Db)")
    plt.show()
    print('results show that it was 462Hz, close to 450Hz, A4')
