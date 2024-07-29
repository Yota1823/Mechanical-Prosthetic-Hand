# scripts/live_monitoring.py
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADS1115 instance
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)  # Assuming muscle sensor is connected to A0

# Initialize the plot
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'b-')

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    return ln,

def update(frame):
    voltage = chan.voltage
    xdata.append(time.time() - start_time)
    ydata.append(voltage)

    xdata_trimmed = [x - xdata[0] for x in xdata]  # Adjust xdata to start from 0
    if len(xdata_trimmed) > 100:
        xdata_trimmed = xdata_trimmed[-100:]
        ydata_trimmed = ydata[-100:]
    else:
        ydata_trimmed = ydata

    ax.set_xlim(xdata_trimmed[0], xdata_trimmed[-1] if len(xdata_trimmed) > 0 else 10)
    ln.set_data(xdata_trimmed, ydata_trimmed)
    return ln,

start_time = time.time()
ani = FuncAnimation(fig, update, init_func=init, blit=True, interval=100)

plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Live Muscle Sensor Data')
plt.show()
