import seabreeze
seabreeze.use('cseabreeze')
from seabreeze.spectrometers import list_devices, Spectrometer
import numpy as np


#SETUP
spec = Spectrometer.from_first_available()
integration_time = spec.integration_time_micros(100000)        #0.1seconds  # This has to be passed as an arguement


class plot_correction:
    #Initilize the Raman
    def __init__(self):
        self.spec = spec
        self.wavelengths = spec.wavelengths()

    # Get the unfiltered data for the plot # here
    def plot_array(self):
        self.intensity = self.spec.intensities()
        return np.array([self.wavelengths,self.intensity],dtype=float)    #,self.intensity Can you come to 214, OMW
    
        #time.sleep(integration_time)

    #get the background data with the laser off.
    def background_array(self):
        self.background_intensity = self.spec.intensities
        return np.array([self.wavelengths, self.background_intensity], dtype=float) ,self.background_intensity

    # subtract the background information from the information we want.
    def corrected_plot(self):
        if not hasattr(self, 'intensity') or not hasattr(self, 'background_intensity'):
            raise ValueError("Call plot_array() and background_array() before corrected_plot()")
        self.corrected_data = self.intensity - self.background_intensity
        return np.array([self.wavelengths,self.corrected_data],dtype=float)

plot = plot_correction()
plot.plot_array()



