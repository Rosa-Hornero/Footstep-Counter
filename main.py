import matplotlib.pyplot as plt
import os
import numpy as np
from count_steps import count_steps

# NOTE:
# The UCI HAR Dataset consists of segmented windows rather than continuous signals.
# Windows are concatenated here to create a pseudo-continuous signal for qualitative
# analysis and visualization purposes only.

# HAR parameters
FS = 50
DATA_PATH = "UCI HAR Dataset"


# Example: load accelerometer windows (train set)
acc_x = np.loadtxt(f"{DATA_PATH}/train/Inertial Signals/body_acc_x_train.txt")
acc_y = np.loadtxt(f"{DATA_PATH}/train/Inertial Signals/body_acc_y_train.txt")
acc_z = np.loadtxt(f"{DATA_PATH}/train/Inertial Signals/body_acc_z_train.txt")

labels = np.loadtxt(f"{DATA_PATH}/train/y_train.txt", dtype=int)
subjects = np.loadtxt(f"{DATA_PATH}/train/subject_train.txt", dtype=int)

# Select subject and activity
SUBJECT_ID = 5
ACTIVITY_ID = 1  # WALKING

mask = (subjects == SUBJECT_ID) & (labels == ACTIVITY_ID)

# Select consecutive windows
acc_x_sel = acc_x[mask]
acc_y_sel = acc_y[mask]
acc_z_sel = acc_z[mask]

# Concatenate windows to form a pseudo-continuous signal
acc_x_concat = acc_x_sel.reshape(-1)
acc_y_concat = acc_y_sel.reshape(-1)
acc_z_concat = acc_z_sel.reshape(-1)

# Count steps
num_steps, peaks, filtered_signal, fig, ax = count_steps(
    acc_x_concat,
    acc_y_concat,
    acc_z_concat,
    FS,
    plot=True,
)

print(f"Estimated number of steps: {num_steps}")

plt.show() 