'''1. kcell_block Class
Constructor (__init__):

Parameters:

root: tkinter's main window.
port: Serial port name (e.g., "COM1" or "/dev/ttyUSB0").
baudrate: Serial port communication speed (e.g., 9600).
text: Label text for the Kcell device (e.g., "KCELL 1").
address: Modbus slave address of the device.
x and y: Coordinates for placing the labels in the GUI.
Functionality:

Initializes a Modbus device instance (minimalmodbus.Instrument).
Sets up GUI elements:
A label to display the device name.
A label to show the current temperature.
Schedules a periodic call to read_temperature every 10 seconds to fetch the temperature from the device.
read_temperature Method:

Purpose:

Reads the temperature from the Modbus device's register and updates the GUI label.
If the read operation fails, prints an error message.
Key Functionality:

python
Copy code
temperature = self.instrument.read_register(address, 1)
Reads the temperature value from the specified Modbus register (address) with 1 decimal precision.
Periodic Update:

python
Copy code
self.root.after(10000, self.read_temperature, 4096)
Calls itself every 10 seconds to continuously update the temperature.
set_temperature Method:

Purpose:
Sends a command to the Modbus device to set a new target temperature.
Key Functionality:
python
Copy code
self.instrument.write_register(address, NEW_TEMPERATURE, 1)
Writes the new temperature value (NEW_TEMPERATURE) to the specified Modbus register (address) with 1 decimal precision.
'''
import minimalmodbus
from tkinter import *
import tkinter as tk
import time

class kcell:
    def __init__(self, root, port, baudrate, text, address, x, y):
        self.root = root
        self.instrument = minimalmodbus.Instrument(port, address)  # port name, slave address (in decimal)
        self.instrument.serial.baudrate = baudrate
        self.instrument.close_port_after_each_call = True
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
        self.instrument.serial.stopbits = 1
        self.instrument.serial.timeout = 1  # seconds
        self.instrument.mode = minimalmodbus.MODE_RTU  # Use RTU mode
        self.instrument.close_port_after_each_call = True

        # Label for Kcell Title
        self.label_ST = Label(root, text=text, bg="skyblue", font=('Times', 12))
        self.label_ST.place(x=x, y=y)

        # Label for Temperature Value
        self.ST_stat = Label(root, text="50", fg="green", bg="skyblue", font=('Times', 12))
        self.ST_stat.place(x=x, y=y+20)

        # Label for Temperature Unit
        self.ST_unit = Label(root, text="C", fg="black", bg="skyblue", font=('Times', 12))
        self.ST_unit.place(x=x+40, y=y+20)  # Adjust position to be next to the temperature value

        self.root.after(10000, self.read_temperature, 4096)

    def read_temperature(self, address):
        try:
            temperature = self.instrument.read_register(address, 1)  # Register number, number of decimals
            print(temperature)
            self.ST_stat.config(text=temperature)  # Update the temperature value
        except IOError:
            print("Failed to read from instrument")

        self.root.after(10000, self.read_temperature, 4096)

    def set_temperature(self, address, NEW_TEMPERATURE):
        try:
            self.instrument.write_register(4097, NEW_TEMPERATURE, address)  # Writing the scaled temperature
            print(f"Setpoint updated to {NEW_TEMPERATURE}")
        except IOError:
            print("Failed to write to instrument")
            return None


#class kcell:
#    def __init__(self, root, port, baudrate):
#        self.root = root
#        self.port = port
#        self.baudrate = baudrate

        # Create instances of kcell_block with updated positions
#        self.kcell_1 = kcell_block(self.root, self.port, self.baudrate, "Kcell 1", 1, 400, 160)
#        self.kcell_2 = kcell_block(self.root, self.port, self.baudrate, "Kcell 2", 2, 500, 160)
#        self.kcell_3 = kcell_block(self.root, self.port, self.baudrate, "Kcell 3", 3, 600, 160)
#        self.substrate = kcell_block(self.root, self.port, self.baudrate, "Substrate", 5, 700, 160)
