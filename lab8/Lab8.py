#######################
#Willard Wider
#6/27/18
#ELEC4400
#Lab 8
#######################

import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile

def function_name(file_name):
    #https://stackoverflow.com/questions/2060628/reading-wav-files-in-python
    fs, data = wavfile.read(file_name)
    #fast fourier transform of the data
    fftOut = fft(data)
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
    return

if __name__ == "__main__":
    #function_name('kpt.wav')
    #question 1: to convince myself, the amplitude is the intensity (loudness)
    #of the sound at that frequency, and it would stand to reason
    #that louder sounds at that frequency tend to exist more in the file
    #
    #frequencies - notes
    #233 - A3#
    #310 - D4#
    #392 - G4
    #
    #pause...
    function_name('hkp.wav')
    #
    #frequencies - notes
    #392 - G4
    #465 - A4#
    #621 - D5#
    #
    #pause...
    #my analysis was core-rekt
