
Youtube link:-
https://youtube.com/shorts/57diVpZjQfI?si=od8-NetaQmInbqug
https://youtube.com/shorts/jg2XoWQryuA?si=FQmtl1rTDQdbs6jF
https://youtu.be/t1IxthM3fIE

## Explanation for first review:-

My contribution as an **EEE member** is to develop the vibration-sensing and embedded-electronics subsystem of the structural health monitoring system. I will select and interface a **3-axis LIS3DH accelerometer** with an **ESP32** to measure vibrations of the structure along the X, Y and Z axes. The sensor will be rigidly mounted to the test structure so that its vibrations can be accurately measured. I will first design and test the circuit in **Tinkercad**, then build the physical prototype. The ESP32 will collect the sensor readings at an appropriate sampling rate and handle the initial processing of the data.

I will also work on **signal processing**, including filtering unwanted noise and using **FFT (Fast Fourier Transform)** to convert the vibration signal from the time domain into the frequency domain. From the processed data, features such as peak acceleration and dominant frequencies can be extracted and transmitted through the ESP32's Wi-Fi to the software/AI system. The **AI team will then use these vibration patterns to identify abnormal behavior**, while the Civil Engineering team will help interpret the structural significance of those changes. Thus, my role is essentially to convert **physical structural vibrations → electrical sensor signals → processed digital data**, providing reliable input for the rest of the project.

# Hardware for seismic sensor:-

Across all three projects, every seismic sensor build uses the exact same core architecture: **Sensor → Microcontroller → Display + Alert Output**.

### Core Hardware Architecture

#### 1. Processing Unit (The Brain)

- **ESP32 Board** _(used in Video 1 & 2)_: Preferred for high-performance builds. Its higher processing speed and expanded memory allow it to plot real-time graphical seismograph waveforms on color displays.
    
- **Arduino Uno R3** _(used in Video 3)_: Ideal for entry-level setups. Simple to program and sufficient for reading sensor thresholds and printing text data.
    

#### 2. Motion Sensing Unit (The Sensor)

- **MPU6050 Accelerometer/Gyroscope Module** _(Digital/I2C)_: Used in Video 1 & 2. Measures acceleration forces and angular rotation across 3 axes via digital I2C communication.
    
- **ADXL335 / GY-61 Module** _(Analog)_: Used in Video 3. Measures 3-axis acceleration and outputs analog voltage signals directly to the microcontroller's analog pins.
    

#### 3. Visual & Audio Output

- **Display Options**:
    
    - **Built-in / External TFT LCD** (e.g., ST7735 or TTGO IPS): Used on ESP32 builds to draw continuous seismic graphs/waveforms.
        
    - **16x2 Character LCD with I2C Module**: Used on Arduino builds for simple text alerts (e.g., "Earthquake Detected!").
        
- **Alert Mechanisms**:
    
    - **5V Active Piezo Buzzer**: Triggers an audible alarm when movement crosses a set threshold.
        
    - **5mm LED (Red/Yellow) + 220Ω Resistor**: Provides visual warning signals.
        

#### 4. Supporting Accessories

- **Breadboard** (Full-size or Half-size)
    
- **Dupont Jumper Wires** (Male-to-Male and Male-to-Female)
    
- **USB Power Cable** (Micro-USB, USB-C, or USB Type-B depending on board choice)
### Combined Master Hardware List

If you want to buy the components to build any version of these projects, this single list covers everything:

|**Component Category**|**Recommended Part**|**Purpose**|
|---|---|---|
|**Microcontroller**|ESP32 Board _(or Arduino Uno R3)_|Collects sensor data, drives display, triggers alarms.|
|**Vibration Sensor**|MPU6050 6-Axis Gyro/Accelerometer|Detects physical shake/vibration along X, Y, Z axes.|
|**Display**|1.8" ST7735 SPI TFT _OR_ 16x2 LCD (I2C)|Displays graph/waveforms or warning text.|
|**Audio Alert**|5V Active Piezo Buzzer|Sounds alarm during high vibration.|
|**Visual Alert**|5mm Red LED + 220Ω Resistor|Flashes warning when threshold is exceeded.|
|**Prototyping**|Breadboard + Jumper Wire Set|Solderless connection between all components.|
