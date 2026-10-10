https://docs.google.com/document/d/1CxlVXmJnu7xIF-7bSyADj_OPYBHaZ27YzZ73x7TiVFU/edit?usp=sharing

# # PROTOTYP CODE

import numpy as np
import matplotlib.pyplot as plt

# Time values
time = np.linspace(0, 10, 1000)

# ---------------- NORMAL VIBRATION ----------------

normal_vibration = np.sin(2 * np.pi * 5 * time)

normal_noise = np.random.normal(0, 0.2, 1000)

normal_data = normal_vibration + normal_noise


# ---------------- ABNORMAL VIBRATION ----------------

abnormal_vibration = 2 * np.sin(2 * np.pi * 5 * time)

abnormal_noise = np.random.normal(0, 0.2, 1000)

abnormal_data = abnormal_vibration + abnormal_noise


# ---------------- CALCULATE RMS ----------------

normal_rms = np.sqrt(np.mean(normal_data ** 2))

abnormal_rms = np.sqrt(np.mean(abnormal_data ** 2))

# ---------------- SEVERITY CLASSIFICATION ----------------

if normal_rms < 0.8:
    normal_status = "Normal"
elif normal_rms < 1.2:
    normal_status = "Warning"
else:
    normal_status = "Critical"


if abnormal_rms < 0.8:
    abnormal_status = "Normal"
elif abnormal_rms < 1.2:
    abnormal_status = "Warning"
else:
    abnormal_status = "Critical"


print("Normal Data Status:", normal_status)
print("Abnormal Data Status:", abnormal_status)


# ---------------- DISPLAY RESULTS ----------------

print("Normal RMS:", normal_rms)
print("Abnormal RMS:", abnormal_rms)


# ---------------- DETECTION ----------------

threshold = 1.0

if normal_rms > threshold:
    print("Normal data: Abnormal vibration")
else:
    print("Normal data: Normal vibration")


if abnormal_rms > threshold:
    print("Abnormal data: Abnormal vibration")
else:
    print("Abnormal data: Normal vibration")


# ---------------- PLOT ----------------

# Plot both signals
# Plot normal vibration
plt.figure()

plt.plot(time, normal_data, color="blue")

plt.xlabel("Time (seconds)")
plt.ylabel("Vibration")
plt.title("Normal Vibration")

plt.show()


# Plot abnormal vibration
plt.figure()

plt.plot(time, abnormal_data, color="red")

plt.xlabel("Time (seconds)")
plt.ylabel("Vibration")
plt.title("Abnormal Vibration")

plt.show()

# ---------------- RESULT SUMMARY ----------------

print("\n================ RESULT SUMMARY ================")

print("Condition        RMS Value        Severity")
print("----------------------------------------------")
print("Normal           ", round(normal_rms, 2), "        ", normal_status)
print("Abnormal         ", round(abnormal_rms, 2), "        ", abnormal_status)

print("================================================")
