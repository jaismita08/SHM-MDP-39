#### Developments needed to make sensor more precise
[[EEE System]]

Make in tinkercad first!!!

#### 1. Sensor Hardware Upgrade (Crucial)

The MPU6050 in the YouTube video is too noisy for high-precision structural health monitoring ($400\ \mu g/\sqrt{\text{Hz}}$ noise density). Upgrading the sensor is essential for clean structural graph creation:

- **Primary Recommendation: Analog Devices ADXL355**
    
    - **Noise Density:** Extremely low ($\sim 25\ \mu g/\sqrt{\text{Hz}}$) — picks up micro-vibrations before major failure occurs.
        
    - **Resolution:** 20-bit digital output via SPI/I2C.
        
    - **Range:** Selectable $\pm 2g / \pm 4g / \pm 8g$ (ideal range for wall/structural monitoring).
        
- **Alternative Option: SW-420 or Piezoelectric Vibration Sensor Array**
    
    - Useful as an instant hardware interrupt trigger to wake the ESP32 from deep sleep.
        

#### 2. Wall Mounting & Enclosure Considerations

How you couple the sensor to the wall directly affects graph fidelity:

- **Rigid Coupling:** Glue or bolt the sensor PCB directly to a heavy aluminium mounting plate. Secure the plate directly to a structural wall or concrete column using expansion anchors. _Do not use foam tape, as it acts as a low-pass filter and distorts higher frequencies._
    
- **Orientation Alignment:** Align the X/Y axes flat against the wall plane (shear forces) and the Z axis perpendicular to the wall (out-of-plane flexure).
#### 3. EEE Signal Processing Pipeline

To generate clean graph data for the AI system, handle initial filtering and sampling on the MCU before transmission:
- **Sampling Rate:** Sample the ADXL355 at **500 Hz to 1000 Hz** to capture structural resonant modes without aliasing.
    
- **Filtering in C++(python works too) (ESP32):**
    
    - **Remove Gravity Component:** Apply a high-pass digital filter ($f_c \approx 0.1\text{ Hz}$) to remove the static $1g$ offset from gravity.
        
    - **Anti-Aliasing / High-Frequency Suppression:** Apply a low-pass Butterworth filter ($f_c \approx 50\text{ Hz}$) to filter out non-structural noise (e.g., slammed doors, nearby footsteps).
        
- **Transmission Protocol:**
    
    - Stream time-series data $(t, a_x, a_y, a_z)$ to the AI server via **WebSockets** or **MQTT** over Wi-Fi/Ethernet.
        
    - Include calculated **Peak Ground Acceleration (PGA)** and **FFT (Fast Fourier Transform)** spectral data in the payload so the AI system gets frequency-domain features ready for anomaly detection.
## SENSOR BUDJET PROPOSED
|Component|Qty.|Approx. cost|
|---|--:|--:|
|**LIS3DH accelerometer breakout**|1|₹135|
|**ESP32 NodeMCU-32**|1|₹399|
|**Breadboard**|1|₹80–150|
|**Jumper wires**|1 set|₹100–150|
|**USB cable**|1|₹100–150|
|**5V USB power adapter**|1|₹150–250|
|**Aluminium mounting plate**|1|₹300–500|
|**Screws/bolts/fasteners**|1 set|₹100–200|
|**Small plastic enclosure**|1|₹150–300|
|**Miscellaneous**|—|₹100–200|
|**TOTAL**||**≈ ₹1,600–₹2,300**|