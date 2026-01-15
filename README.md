# Footstep-Counter. Step Counting from Smartphone Accelerometer Signals
This repository presents a **step counting algorithm** based on **smartphone accelerometer data**, using signals from the **UCI Human Activity Recognition (HAR) Dataset**.
The goal is to design a **simple, explainable, and reproducible pipeline** that detects walking steps from triaxial accelerometer signals, avoiding dependency on smartphone orientation.

---

## Project Overview
The proposed approach follows a classical signal-processing pipeline:
1) **Acceleration magnitude computation** to remove orientation dependency.
2) **DC component removal** to center the signal around zero.
3) **Band-pass filtering** to isolate the walking frequency band.
4) **Peak detection** to identify individual steps.

The implementation is designed to be:
* Modular
* Easy to understand
* Suitable for educational and research purposes

---

## Project Structure
- **`notebook/`**
  - **`step_counter_analysis.ipynb/`**: Exploratory analysis and signal visualization.
- **`count_steps.py  /`**: Step counting function (core logic).
- **`main.py`**: Example usage with UCI HAR data.
- `requirements.txt`: Project dependencies.
- `README.md`: Project documentation.
- `LICENSE`: MIT License
  
---

## Dataset
This project uses the **UCI Human Activity Recognition Dataset**:
* Sampling frequency: 50 Hz
* Window length: 2.56 s
* Signals: triaxial body acceleration
* Activities include: WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, etc.
* Dataset link: [UCI Human Activity Recognition Dataset](https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones)
> [!NOTE]
> The UCI HAR Dataset consists of segmented windows rather than continuous signals.
> In this project, windows belonging to the same subject and activity are concatenated
> to create a pseudo-continuous signal for qualitative analysis and visualization purposes.
> Therefore, the estimated step count should not be interpreted as ground truth..

---

## Methodology
### 1) Acceleration Magnitude
To eliminate orientation dependence, the acceleration magnitude is computed as:

$Magnitude=\sqrt{a_x^2 + a_y^2 + a_z^2}$

### 2) DC Component Removal
The mean value of the magnitude signal is removed to eliminate the DC component and center the signal around zero, facilitating peak detection.

### 3) Band-pass Filtering
A 4th-order Butterworth band-pass filter is applied with cutoff frequencies: 0.5 Hz – 3.0 Hz. This range covers typical human walking cadence while removing low-frequency drift and high-frequency noise

### 4) Step Detection
Steps are detected using peak detection with:

* An adaptive threshold based on the signal standard deviation
* A minimum inter-peak distance corresponding to physiological constraints

Each detected peak corresponds to one walking step.

---

## Usage

### Requirements
```bash
pip install -r requirements.txt
```

### Example with UCI HAR data

   ```bash
   python main.py
   ```
This script:
* Loads accelerometer windows from the HAR dataset
* Selects a subject and walking activity
* Concatenates windows to create a pseudo-continuous signal
* Applies the step counting algorithm
* Visualizes detected steps

### Example Output
Here is a small example of what you can see as an output.
![OutputExample](Output_example.jpg)

---

## Limitations

> [!WARNING]
> * The HAR dataset is window-based and not continuous.
> * Ground-truth step annotations are not available.
> * Results are intended for demonstration and analysis, not for clinical use.

---

## Contributing

This project focuses on clarity, interpretability, and reproducibility, serving as a baseline for more advanced gait and activity analysis methods. We welcome contributions! Please feel free to submit pull requests or report issues.

## Contact
If you have any questions or suggestions about this project, feel free to reach out:

- Email: [rosa.hornero1@gmail.com](rosa.hornero1@gmail.com)
- LinkedIn: [Rosa Hornero](https://www.linkedin.com/in/rosa-hornero/)
- Twitter: [@hornero_rosa](https://x.com/hornero_rosa)
