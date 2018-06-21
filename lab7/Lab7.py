'''############
Willard Wider
6/20/18
ELEC 3800
Lab 7
Fourier stuffs
'''############

#importing all the modules we will need
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

#specify the stype of the plot to use
plt.style.use('ggplot')
#notes
#https://www.mathsisfun.com/calculus/fourier-series.html
#https://www.datacamp.com/community/tutorials/functions-python-tutorial
#https://www.pythoncentral.io/pythons-range-function-explained/
#https://en.wikipedia.org/wiki/Square_wave


#for problem 1
def Problem1(start,stop,interval,problem_name):
    #starts at 1, ends at 2, 20 frames
    #fouriers = np.linspace(1,10,10)
    fouriers = range(start,stop+1,interval)
    #set the int for the num of pngs to make
    i = 0
    val = 0
    x = np.linspace(-np.pi,np.pi,500)
    #for each itteration of the foruriour function creation
    for n in fouriers:
        #n is the fourier incriment itteration
        #create the y axis
        
        #ahh i see what's goign on here
        val = val + (-2/np.pi)*((np.cos(n*np.pi)*np.sin(x*n))/n)

        #create the two graphs for matlab plotting
        plt.plot(x,val)
        #setting all the plot information for each of the two plots
        plt.title("T = %s"%n)
        
        #plt.show()
        plt.savefig(problem_name + '_%s.png'%i)
        plt.close()
        i+=1
    return

    #for problem 1
def Problem2(start,stop,interval,problem_name,L_value=1):
    #starts at 1, ends at 2, 20 frames
    #fouriers = np.linspace(1,10,10)
    fouriers = range(start,stop+1,interval)
    #set the int for the num of pngs to make
    i = 0
    val = 0
    x = np.linspace(-np.pi,np.pi,500)
    #for each itteration of the foruriour function creation
    for n in fouriers:
        #n is the fourier incriment itteration
        #create the y axis
        
        #ahh i see what's goign on here
        val = val + (4/np.pi)*((1/n)*(np.sin(n*x*np.pi)/L_value))

        #create the two graphs for matlab plotting
        plt.plot(x,val)
        #setting all the plot information for each of the two plots
        plt.title("T = %s"%n)
        
        #plt.show()
        plt.savefig(problem_name + '_%s.png'%i)
        plt.close()
        i+=1
    return

    #for problem 1
def Problem3(start,stop,interval,problem_name,L_value):
    #starts at 1, ends at 2, 20 frames
    #fouriers = np.linspace(1,10,10)
    fouriers = range(start,stop+1,interval)
    #set the int for the num of pngs to make
    i = 0
    val = 0
    x = np.linspace(-np.pi,np.pi,500)
    #for each itteration of the foruriour function creation
    for n in fouriers:
        #n is the fourier incriment itteration
        #create the y axis
        
        #ahh i see what's goign on here
        #kind of
        val_part_1 = (8/(np.power(np.pi,2)))
        #val_part_2 = ((np.power(-1,(n-1)/2))/(np.power(n,2)))
        #almost...
        val_part_2_1 = np.float_power(-1,(n-1)/2)
        val_part_2_2 = np.power(n,2)
        val_part_2 = val_part_2_1/val_part_2_2
        val_part_3 = np.sin((n*x*np.pi)/L_value)
        val = val + val_part_1*val_part_2*val_part_3

        #create the two graphs for matlab plotting
        plt.plot(x,val)
        #setting all the plot information for each of the two plots
        plt.title("T = %s"%n)
        
        #plt.show()
        plt.savefig(problem_name + '_%s.png'%i)
        plt.close()
        i+=1
    return

    #for problem 1
def Problem4():
    #4.1/4.2 - Problem 1 and Problem 2 waves were not quite right because
    # they were not flat lines for each flat part. This makes sense 
    # because we are using sine/cosine WAVES(never flat) as approximations
    #4.3 - the result is that as you add more itterations of fourier,
    # it gives a better flatter part. Therefore in theroy, by adding
    # infinite fouriers you would achieve that flat line
    #4.4 - This is called the Gibbs phenomenon. The triangle wave does
    # not exeperience this because it does not have a jump discontinuity 
    # in its continouos function

    #https://en.wikipedia.org/wiki/Gibbs_phenomenon
    return
    
#from 1 to 10, with interval of 1
Problem1(1,10,1,"problem_1")

Problem2(1,20,2,"problem2",2)
#2.1 - a square wave was generated

Problem3(1,20,2,"problem3",1)
#3.1 - a triangle wave was generated

Problem4()
#^^yes, i just did that. even tho it does nothing. Because reasons.