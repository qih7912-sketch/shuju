import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load experimental data function

def load_experimental_data(filename):
    data = np.loadtxt(filename, delimiter=',')
    return data

# Load theoretical predictions function

def load_theoretical_predictions(num_slits, x):
    # Example theoretical function (to be replaced with actual computations)
    return (np.sin(num_slits * x) / x)**2

# Compare experimental and theoretical data

def compare_data(experimental_data, theoretical_data):
    # Statistical analysis (e.g., calculating R-squared)
    slope, intercept, r_value, p_value, std_err = stats.linregress(experimental_data, theoretical_data)
    return r_value**2

# Visualization function

def visualize_comparison(x, experimental_data, theoretical_data, num_slits):
    plt.figure(figsize=(10, 6))
    plt.plot(x, experimental_data, 'o', label='Experimental data')
    plt.plot(x, theoretical_data, '-', label=f'Theoretical prediction ({num_slits} slits)')
    plt.title('Experimental vs Theoretical Data Comparison')
    plt.xlabel('X-axis label')  # Replace with actual X-axis label
    plt.ylabel('Y-axis label')  # Replace with actual Y-axis label
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage

x = np.linspace(0.1, 10, 100)
num_slits = 2  # Example number of slits
experimental_data = load_experimental_data('experimental_data.csv')  # Load your experimental data

# Load theoretical predictions
 theoretical_data = load_theoretical_predictions(num_slits, x)

# Compare and visualize
r_squared = compare_data(experimental_data, theoretical_data)
print(f'R-squared value: {r_squared}')
visualize_comparison(x, experimental_data, theoretical_data, num_slits)