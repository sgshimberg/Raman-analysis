import serial
import time

class PowerRelay:
    def __init__(self, port='COM6', baudrate=9600):
        self.arduino = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2) 
    
    def heater_on(self):
        self.arduino.write(b'ON\n')
        print("ON")

    def heater_off(self):
        self.arduino.write(b'OFF\n')
        print("OFF")

    # set temp SET,<ramp>,<set_temp>
    def set_temperature(self, ramp, set_temp):
        ramp_rate = f"{ramp}"
        set_temperature = f"{set_temp}"
        self.arduino.write(f'SET,{ramp_rate},{set_temperature}\n'.encode())

    # temp,<current_temp>
    def Current_temp(self, temp):
        temperature_current = f"{temp}"
        self.arduino.write(f"temp,{temperature_current}\n".encode())
        


    def close(self):
        self.arduino.close()


