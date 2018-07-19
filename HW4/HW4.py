#######################
#Willard Wider
#7/19/18
#ELEC4400
#HW4
#######################

import matplotlib.pyplot as plt
import numpy as np

#specify the stype of the plot to use
plt.style.use('ggplot')

#problem 1
x_index = np.linspace(-10,10,500)
HW_1_sine_part = np.sin(x_index*5)*(25*(x_index*x_index)-2)
HW_1_cos_part = np.cos(x_index*5)*(10*x_index)
HW_1_combo = HW_1_cos_part+HW_1_sine_part
HW_1_coef = 2/(np.power(x_index,3))
HW_1 = HW_1_coef*HW_1_combo

plt.plot(x_index,HW_1)
plt.title('HW4 problem 1')
plt.show()

plt.close()

#problem 2
#uses same x index...
#used a=2
HW_2_P1_1 = 1/(2-x_index)
HW_2_P1_2 = np.sin(8*np.pi - 4*x_index*np.pi)
HW_2_P2_1 = 1/(2+x_index)
HW_2_P2_2 = np.sin(8*np.pi + x_index*4*np.pi)
HW_2 = (HW_2_P1_1*HW_2_P1_2) + (HW_2_P2_1*HW_2_P2_2)

plt.plot(x_index,HW_2)
plt.title('HW4 problem 2')
plt.show()

plt.close()

#3 - modify a
#let's try it...

HW_2_P1_1 = 1/(6-x_index)
HW_2_P1_2 = np.sin(24*np.pi - 4*x_index*np.pi)
HW_2_P2_1 = 1/(6+x_index)
HW_2_P2_2 = np.sin(24*np.pi + x_index*4*np.pi)
HW_2 = (HW_2_P1_1*HW_2_P1_2) + (HW_2_P2_1*HW_2_P2_2)

plt.plot(x_index,HW_2)
plt.title('HW4 problem 2: new a = 6')
plt.show()

plt.close()

#modifying the a (frequency) paremeter changes where the frequency of the function is
#therefore, on a function on frequency to amplitude, changing the frequency changes where the amplitude is on the x axis
#the sampling time does matter, if you don't sample fast enough, you may loose the original function