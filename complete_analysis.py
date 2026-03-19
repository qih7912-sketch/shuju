import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import pandas as pd

# Constants
wavelength = 633e-9  # Wavelength in meters
D = 90e-3  # Distance to screen in meters
a = 0.04  # Slit width in meters
d = 0.25e-3  # Slit separation in meters

# 1. Loading uint16 sensor data from 317.cap
# Assuming the .cap file is in a readable format via Pandas or similar.
def load_data(filepath):
    # Placeholder for loading the data, assuming it’s a .csv for the purpose of this example
    data = pd.read_csv(filepath)
    return data['sensor_data'].values  # Replace with the appropriate column name

# 2. Data preprocessing and smoothing
def preprocess_data(data):
    # Applying a Savitzky-Golay filter for smoothing
    smoothed_data = savgol_filter(data, window_length=51, polyorder=3)  # Adjust as necessary
    return smoothed_data

# 3. Multi-slit interference theoretical calculations using complex number method
def multi_slit_interference(slits, angles):
    phase_diffs = 2 * np.pi / wavelength * (slits * np.sin(angles[:, None]))
    intensity = np.abs(np.sum(np.exp(1j * phase_diffs), axis=1))**2
    return intensity

# 4. Experimental vs theoretical comparison
def compare_experimental_theoretical(experimental_data, theoretical_data):
    plt.figure()
    plt.plot(experimental_data, label='Experimental Data')
    plt.plot(theoretical_data, label='Theoretical Data', linestyle='--')
    plt.legend()
    plt.title('Experimental vs Theoretical Comparison')
    plt.xlabel('Position (pixels)')
    plt.ylabel('Intensity')
    plt.show()

# 5. Fringe detection and analysis
def detect_fringe(data):
    # Placeholder for fringe detection logic
    # This could involve finding peaks in the intensity data
    return peaks  # Replace with actual peak finding logic

# 6. Visualization of results for 2-5 slits
def visualize_results(slits):
    angles = np.linspace(-0.1, 0.1, 1000)  # Angle range
    theoretical_intensity = multi_slit_interference(slits, angles)
    plt.figure()
    plt.plot(angles, theoretical_intensity, label=f'{slits} Slits')
    plt.title(f'Multi-Slit Interference with {slits} Slits')
    plt.xlabel('Angle (radians)')
    plt.ylabel('Intensity')
    plt.legend()
    plt.show()

# Main execution
if __name__ == '__main__':
    filepath = '317.cap'  # Ensure this is the correct path
    sensor_data = load_data(filepath)
    smoothed_data = preprocess_data(sensor_data)

    # Example usage for visualization
    for slits in range(2, 6):
        visualize_results(slits)

    # Comparison logic here
    # theoretical_intensity = multi_slit_interference(...)
    # compare_experimental_theoretical(smoothed_data, theoretical_intensity)