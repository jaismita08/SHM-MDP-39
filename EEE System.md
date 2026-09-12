
Youtube link:-
https://youtube.com/shorts/57diVpZjQfI?si=od8-NetaQmInbqug
https://youtube.com/shorts/jg2XoWQryuA?si=FQmtl1rTDQdbs6jF
https://youtu.be/t1IxthM3fIE

## Explanation for first review:-

My contribution to this project is mainly focused on the **sensor and circuit development**.

As the EEE member, I worked on creating the initial sensor prototype in **Tinkercad**, connecting the sensor circuit with the Arduino, and testing how changes in vibration or displacement can be converted into electrical readings.

My role is to provide the **hardware and sensor data** that can later be processed by the AI and other team members. This connects the physical structure with the digital analysis part of our SHM system.

Going forward, I will work on improving the sensor setup and integrating it with the complete system.
### Jaismitha (Slides 4, 9, 10)

**Slide 4 (Team Roles):**

"Let me introduce our team and our roles. We are a five-member multidisciplinary team. Madhumitha, from AIML, developed our machine learning models. Tanisha, from CSE, implemented the wireless communication protocols. Manonmani, from Civil, designed the sensor layout on the structure. I am Jaismitha, from EEE, and I managed the hardware and power systems. And Yaswanth, from AIML, handled data structuring and integration."

**Slide 9 (Supporting Data):**

"To support the real-world relevance of our problem, we referred to the IIT Bombay WEL EDL 2025 project. This project helps ground the significance of our multidisciplinary structural health monitoring problem, showing that similar wireless vibration-sensing approaches have already been explored and validated at a reputed institution — which gives us a solid technical reference point to build from."

**Slide 10 (Specific Objectives – Part 1):**

"Now to our specific objectives. The first is to design a wireless sensor node — this node needs to capture vibration and acceleration data from the structure. The second objective is wireless data transmission — we aim to transmit this sensor data wirelessly to a central unit, so it can be processed without needing physical wiring across the structure."

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
