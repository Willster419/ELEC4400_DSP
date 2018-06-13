'''############
Willard Wider
6/13/18
ELEC 3800
Lab 6
Python stuffs
'''############

#importing all the modules we will need
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

#specify the stype of the plot to use
plt.style.use('ggplot')

#creates an array from 0 to 0.22, with 20 evenly spaced numers
Tx = np.linspace(0,0.22,20)
i = 0
#standard for loop structure
for T in Tx:
    #creates an exponential array of e^-T, for numerator
    num = np.array([10-10*np.exp(-T)])
    #creatres an exponential array of e^-T, for denominator
    den = np.array([1, 10-11*np.exp(-T)])

    #create transfer function
    dtf = sig.dlti(num,den)
    #create a step response of the transfer function
    t,y = sig.dstep((dtf),n=1000)

    #create the circle for the graph using the array
    tCirc = np.linspace(0,2*np.pi,100)
    xCirc = np.cos(tCirc)
    yCirc = np.sin(tCirc)

    #use roots function to get the poles
    poleLocation = np.roots(den)

    #set colors for the graph
    colorIndicator = "b"
    markerIndicator = "o"

    #if the apsolute value of the pole location is greator than 1 (out of bounds)
    #set differnt colors
    if np.abs(poleLocation)>1:
        colorIndicator = "r"
        markerIndicator = "x"
    #print to pole location
    print("pole location",poleLocation)
    #create the two graphs for matlab plotting
    f,xarr = plt.subplots(2)
    #setting all the plot information for each of the two plots
    xarr[0].set_title("T = %s"%T)
    xarr[0].plot(t,y[:][0])
    xarr[1].plot(1,0,c="g",marker="o")
    xarr[1].plot(xCirc,yCirc)
    xarr[1].scatter(poleLocation,0,c=colorIndicator, marker=markerIndicator)
    xarr[1].set_xlabel("pole magnitude is %s"%poleLocation)
    xarr[1].set_xlim([-2,2])
    #i am ready
    plt.savefig('animation%s.png'%i)
    #plt.show()
    i+=1
