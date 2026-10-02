checking connection
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

## 🔧 Your EEE checklist for Review II

### 1. Finish the Tinkercad proof-of-concept

You already have most of this.

**Potentiometer → Arduino Uno → vibration value**

You should be able to demonstrate:

- potentiometer simulating vibration/displacement
- Arduino reading the analog value
- calculating vibration magnitude
- Serial Monitor displaying the readings
- LED responding to vibration level

✅ **This is your current hardware prototype.**

---

### 2. Prepare the real sensor selection

You need to research **which vibration/accelerometer sensor you will eventually use**.

For your PPT, have:

|Requirement|What you need|
|---|---|
|Sensor type|Accelerometer / vibration sensor|
|Measurement|Structural vibration/acceleration|
|Interface|I²C / SPI / analog, depending on sensor|
|Measurement range|Appropriate `±g` range|
|Sensitivity/noise|Important for small structural vibrations|
|Controller|Arduino/ESP32|
|Power|Sensor operating voltage|
|Mounting|How it will attach to the structure|

MEMS accelerometers are commonly used in SHM because they are compact and relatively low-cost, although sensor precision and noise become important for low-amplitude vibration measurements.

You **don't need to buy it yet**.

---

### 3. Make a sensor-selection table

This would be very useful for your Review II PPT.

For example:

|Sensor|Type|Interface|Advantage|Limitation|
|---|---|---|---|---|
|MPU6050|MEMS accelerometer|I²C|Cheap, easy to interface|Higher noise|
|ADXL345|MEMS accelerometer|I²C/SPI|Better suited to acceleration measurement|Still limited for very low-level precision|
|ADXL355|Low-noise MEMS accelerometer|I²C/SPI|Much lower noise|More expensive|
|Piezoelectric sensor|Vibration sensor|Analog|Good for dynamic vibration|Not ideal for static acceleration|

Then your team can explain **why the final sensor will be selected after comparing requirements**.

Don't claim a sensor is definitely your final choice until you've checked its datasheet and your project requirements.

---

### 4. Make the EEE block diagram

Your section should have something like:

```
        STRUCTURE
            ↓
     Vibration occurs
            ↓
     ┌──────────────┐
     │   SENSOR     │
     │ Accelerometer│
     └──────┬───────┘
            ↓
       Arduino/ESP32
            ↓
     Signal acquisition
            ↓
       Serial / Wi-Fi
            ↓
       Python system
```

This is basically **your EEE contribution to the overall architecture**.

---

### 5. Document the Arduino side

Put your current Arduino implementation in the project documentation.

Explain:

```
Analog sensor reading
        ↓
Equilibrium/reference
        ↓
Displacement
        ↓
Vibration magnitude
        ↓
Warning level
```

Your Tinkercad potentiometer is essentially a **sensor simulator** for this stage.

---

### 6. Connect your EEE work to the Python graph

Your eventual system should be:

```
REAL SENSOR
     ↓
ARDUINO / ESP32
     ↓
VIBRATION DATA
     ↓
PYTHON
     ↓
LIVE GRAPH
     ↓
NORMAL / CRITICAL / SEVERE
```

For Review II, you can show the **Tinkercad sensor prototype** and the **Python visualization as separate proof-of-concepts**.

Later, when you get the physical sensor, the real sensor replaces the potentiometer and the Python side can remain largely the same.

---

## 📋 So your EEE work before Review II is basically:

**Must have:**

- [x]  Tinkercad circuit
- [x]  Arduino sensor-reading logic
- [x]  Vibration calculation
- [x]  LED indication
- [x]  Serial output
- [x]  Python graph file
- [ ]  Research real accelerometer/vibration-sensor options
- [ ]  Sensor comparison table
- [ ]  Decide/propose the sensor based on requirements
- [ ]  EEE block diagram
- [ ]  Explain sensor → microcontroller → data pipeline
- [ ]  Put these into the Review II PPT

**Not required yet:**

- ❌ Physical sensor in hand
- ❌ Final hardware assembly
- ❌ Final sensor calibration
- ❌ Final AI model
- ❌ Real structural testing