"""
Raman Data Processor and CSV Column Extractor
---------------------------------------------

This script processes Raman spectroscopy data stored in a directory of .txt files,
and also extracts the first two columns from a separate CSV file and stores them 
as a NumPy float array.

Functionality:
- Reads all .txt files in the specified working directory (skipping the first 15 lines).
- Converts two-column data into NumPy arrays and stores them in a dictionary keyed by timestamp.
- Optionally extracts the first two columns from a given CSV file for further analysis.

Expected File Structure:
- A folder of .txt Raman data files named with timestamp info (e.g., `sample__timestamp.txt`)
- A separate CSV file located at: 
  C:\Users\sethg\BZT080-BCT020-laser-45\BZT80-BCT20-temperature_Data.csv

Requirements:
- Python 3.x
- NumPy
- Pandas
- CSV (built-in)
- Files must have consistent data formats (two float columns)
"""

import os
import numpy as np
import pandas as pd
import csv



working_directory = r'C:\Users\sethg\Text_3d_Array_data'        #Working directory with files
csv_working_directory = r'C:\Users\sethg\BZT080-BCT020-laser-45\BZT80-BCT20-temperature_Data.csv'
data_dict = {}                                                  #Initilize the dictionary


def Raman_2d_array():
    with os.scandir(working_directory) as es:                       #scans working directory 
        for e in es:
            time_stamp =e.name.split("__")[-1]
            if e.is_file() and e.name.endswith('.txt'):             #scans each file to see if it ends with .txt
                key = time_stamp.replace(".txt", "")
                with open(e.path, encoding='UTF-8') as f:           # opens .txt files
                    lines = f.readlines()[15:]                      # read from line 16 to end of file
                    Raman_file_data_array = []
                    for line in lines:                              #loop through each line and strip each /n character 
                        line = line.strip()                          #Strip any new lines and prepare for array
                        parts = line.split(maxsplit=1)
                        if len(parts) == 2:
                            Raman_file_data_array.append(parts)              #Create new array
                float_array = np.array(Raman_file_data_array, dtype=float)     #turn the array of strings into floats.
                data_dict[key]  = float_array 
    return data_dict

def store_csv():
    with open('BZT80-BCT20-temperature_Data.csv', newline='')as csvfile:
        data = list(csv.reader(csvfile))
    print(data)






    store_csv()
    
   
          




























"""
Raman_2d_array()

sorted_keys = sorted(data_dict.keys())

stacked_array = np.stack([data_dict[k] for k in sorted_keys])

print("Shape of stacked array: ", stacked_array.shape)

slice_2 = stacked_array[4,:,:]
print(slice_2)

"""