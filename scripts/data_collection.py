import os
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import csv

# Ensure the directory exists
os.makedirs('../data/raw', exist_ok=True)

# Print the current working directory for debugging
print("Current Working Directory:", os.getcwd())

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADS1115 instance
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)  # Assuming muscle sensor is connected to A0

# File to save the data
data_file_path = '../data/raw/muscle_data_raw.csv'
print(f"Saving data to: {data_file_path}")
data_file = open(data_file_path, 'w', newline='')
csv_writer = csv.writer(data_file)
csv_writer.writerow(['timestamp', 'muscle_voltage'])

def read_muscle_sensor():
    return chan.voltage

try:
    while True:
        muscle_voltage = read_muscle_sensor()
        timestamp = time.time()
        print(f"Time: {timestamp}, Muscle Voltage: {muscle_voltage}")

        # Save data to CSV
        csv_writer.writerow([timestamp, muscle_voltage])
        data_file.flush()  # Ensure data is written to the file

        time.sleep(0.1)  # Adjust based on your needs

except KeyboardInterrupt:
    pass

finally:
    # Properly close the file
    data_file.close()
    print("Data file closed successfully.")
