import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import numpy as np
import biosppy.signals.emg as emg

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADS1115 instance
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)

def read_muscle_sensor():
    return chan.voltage

# Collect some data for testing
data = []
start_time = time.time()
while time.time() - start_time < 10:  # Collect data for 10 seconds
    data.append(read_muscle_sensor())
    time.sleep(0.01)

# Process the data using BioSPPy
signals = np.array(data)
ts, filtered, onsets = emg.emg(signal=signals, sampling_rate=1000.0, show=True)

print("Filtered Signal: ", filtered)
print("Onsets: ", onsets)
