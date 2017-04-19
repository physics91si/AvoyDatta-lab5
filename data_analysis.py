#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

X_SPACING = 0.001

threshold_freq = 5

def wavepacket(x, k, sigma):
    """This function creates a wavepacket on the interval defined by x with
    wavevector k and standard deviation sigma."""
    return np.sin(k*x) *  np.exp(-(x**2)/(2*sigma**2))


def main():
    """This function sould call noisy_packet() to get a Gaussian wave
    packet, call clean_data() to apply a low pass filter to the data and
    finally plot the result."""
    #TODO add your code here


    x = np.arange(0, 5, X_SPACING)
    y = noisy_packet(x, 5, 1, 0.2)

    plt.plot(x, y)
    #plt.show()

    z = clean_data(x, y)

    plt.plot(x, z)
    plt.show()

def noisy_packet(x_values, k, sigma, noise_amplitude):
    """This function returns a noisy Gaussian wavepacket with wave
    vector k, standard deviation sigma and Gaussian noise of standard
    deviation noise_amplitude."""
    clean_y = wavepacket(x_values,k,sigma)
    noisy_y = clean_y + noise_amplitude*np.random.randn(len(x_values))
    return noisy_y

def clean_data(x_values,y_values):

	sorted_y = np.fft.rfft(y_values)
	clean_freq = np.fft.rfftfreq(len(x_values), X_SPACING)

	for i in range(0, len(clean_freq)):
		if clean_freq[i] > threshold_freq:
			sorted_y[i] = 0
	clean_y = np.fft.irfft(sorted_y)

	return clean_y



main()  # calls your main function
