import serial
import matplotlib.pyplot as plt
from collections import deque

# ==============================
# ARDUINO SETTINGS
# ==============================

PORT = "COM3"       # CHANGE THIS to your Arduino COM port
BAUD_RATE = 9600

# ==============================
# WARNING LEVELS
# ==============================

NORMAL_LIMIT = 100
CRITICAL_LIMIT = 250

# Number of points visible on graph
MAX_POINTS = 150

# ==============================
# CONNECT TO ARDUINO
# ==============================

arduino = serial.Serial(PORT, BAUD_RATE, timeout=1)

# Store incoming data
vibration_data = deque(maxlen=MAX_POINTS)
time_data = deque(maxlen=MAX_POINTS)

# Interactive plotting
plt.ion()

fig, ax = plt.subplots()

line, = ax.plot([], [], linewidth=2)

ax.set_title("Structural Health Monitoring - Live Vibration")
ax.set_xlabel("Time (samples)")
ax.set_ylabel("Vibration Level")

ax.set_ylim(0, 512)
ax.set_xlim(0, MAX_POINTS)

ax.grid(True)

sample = 0

# ==============================
# LIVE MONITORING
# ==============================

while True:

    try:
        data = arduino.readline().decode().strip()

        if data == "":
            continue

        vibration = int(data)

        # Store data
        vibration_data.append(vibration)
        time_data.append(sample)

        sample += 1

        # ==============================
        # WARNING STATUS
        # ==============================

        if vibration >= CRITICAL_LIMIT:

            line.set_color("red")
            status = "SEVERE"

        elif vibration >= NORMAL_LIMIT:

            line.set_color("orange")
            status = "CRITICAL"

        else:

            line.set_color("green")
            status = "NORMAL"

        # Update graph
        line.set_data(time_data, vibration_data)

        # Move graph window
        ax.set_xlim(
            max(0, sample - MAX_POINTS),
            max(MAX_POINTS, sample)
        )

        # Update title
        ax.set_title(
            f"Structural Health Monitoring | "
            f"Status: {status} | "
            f"Vibration: {vibration}"
        )

        plt.pause(0.001)

    except ValueError:
        continue

    except KeyboardInterrupt:
        print("Monitoring stopped.")
        break

# Close Arduino connection
arduino.close()