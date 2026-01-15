import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks

def bandpass_filter(signal, fs, lowcut=0.5, highcut=3.0, order=4):
    """
    Apply a Butterworth band-pass filter to a 1D signal.
    """
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, signal)


def count_steps(acc_x, acc_y, acc_z, fs, plot=False):
    """
    Count steps from triaxial accelerometer signals.

    Parameters
    ----------
    acc_x, acc_y, acc_z : np.ndarray
        Acceleration signals along x, y, and z axes.
    fs : float
        Sampling frequency in Hz.
    plot : bool, optional
        If True, create a plot of detected steps and return the matplotlib figure and axis.

    Returns
    -------
    num_steps : int
        Estimated number of steps.
    peaks : np.ndarray
        Indices of detected step peaks.
    filtered_signal : np.ndarray
        Band-pass filtered acceleration magnitude.
    fig, ax : matplotlib.figure.Figure, matplotlib.axes.Axes (optional)
        Returned only if plot and return_fig are True.
    """

    # 1) Calculate the magnitude of the signal
    magnitude = np.sqrt(acc_x**2 + acc_y**2 + acc_z**2)

    # 2) Signal Centering (eliminate the DC component)
    magnitude_centered = magnitude - np.mean(magnitude)

    # 3) Band-pass Filtering (a fourth-order Butterworth filter)
    filtered_signal = bandpass_filter(magnitude_centered, fs)

    # 4) Step Detection (Looking for the peaks)

    # Threshold adjusted according to the signal standard deviation
    threshold = 0.5 * np.std(filtered_signal)

    # Minimum physiological distance between peaks
    min_distance = int(0.35 * fs)

    # Looking for the peaks
    peaks, properties = find_peaks(
        filtered_signal,
        height=threshold,
        distance=min_distance
    )

    num_steps = len(peaks)

    fig, ax = None, None

    # 5) Optional plot
    if plot:
        time = np.arange(len(filtered_signal)) / fs
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.plot(time, filtered_signal, label="Filtered signal")
        ax.plot(time[peaks], filtered_signal[peaks], "x", label="Detected steps")
        ax.set_title(f"Detected Steps: {num_steps}")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Acceleration")
        ax.legend()
        ax.grid(True)

        return num_steps, peaks, filtered_signal, fig, ax

    return num_steps, peaks, filtered_signal


