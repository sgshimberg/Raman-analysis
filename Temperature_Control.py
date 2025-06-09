import minimalmodbus
import serial
import threading
import time


# PID control functions
class Temperature_Control:

    #Initilizing the PID controller
    def __init__(self, port='COM6', baudrate=9600):
        #initializing the instrument   
        self.instrument = minimalmodbus.Instrument('COM4',1,)
        self.instrument.serial.baudrate = 9600
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
        self.instrument.serial.stopbits = 1
        self.arduino = serial.Serial(port, baudrate, timeout=1)


    #Grabbing the present value from the PID controller
    def Current_temperature(self):
        #Temperature read to PV
        temperature = self.instrument.read_register(4096, 1)
        return temperature

    #set a new value to the PID controller
    def set_value(self, SV):
        #temperature write to SV
        self.instrument.write_register(4097, int(SV), 1) 

    








    
    

