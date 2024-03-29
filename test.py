# Import dependencies
import numpy as np
import pandas as pd
from scipy.stats import chisquare, binom, poisson, expon, geom

# Define a function that handles the frequency test
def frequency_test(data, distribution='uniform', **dist_params):
    flattened_data = data.flatten()
    n = len(flattened_data)
    unique_values, counts = np.unique(flattened_data, return_counts=True)
    
    # Calculate expected frequencies based on the specified distribution
    if distribution == 'uniform':
        expected_freq = np.ones_like(unique_values) * (1 / len(unique_values)) * n
    elif distribution == 'binomial':
        n_trials = dist_params.get('n', 1)
        p_success = dist_params.get('p', 0.5)
        expected_freq = binom.pmf(unique_values, n_trials, p_success) * n
    elif distribution == 'poisson':
        lambda_rate = dist_params.get('lambda', 1)
        expected_freq = poisson.pmf(unique_values, lambda_rate) * n
    elif distribution == 'exponential':
        scale = dist_params.get('scale', 1)
        expected_freq = expon.pdf(unique_values, scale=scale) * n
    elif distribution == 'geometric':
        p_success = dist_params.get('p', 0.5)
        expected_freq = geom.pmf(unique_values, p_success) * n
    else:
        raise ValueError("Unsupported distribution type!")
    
    # Normalize expected frequencies to match the total count of observed frequencies
    expected_freq_sum = np.sum(expected_freq)
    observed_freq_sum = np.sum(counts)
    if expected_freq_sum == 0:
        raise ValueError("Expected frequency sum is zero, check distribution parameters and data.")
    normalization_factor = observed_freq_sum / expected_freq_sum
    normalized_expected_freq = expected_freq * normalization_factor

    normalized_expected_freq = np.nan_to_num(expected_freq * normalization_factor)

    # Perform chi-square test with normalized expected frequencies
    chi2_stat, p_value = chisquare(counts, normalized_expected_freq)
    return chi2_stat, p_value

# Read data from CSV without headers
data = pd.read_csv('randomNumbers.csv', header=None)

# Convert the data to a NumPy array for analysis
random_numbers = data.values

# Ask user for distribution type
distribution = input("Enter the distribution type (uniform, binomial, poisson, exponential, geometric): ")

# Perform frequency test
chi2_stat, p_value = frequency_test(random_numbers, distribution)

print("Chi-square statistic:", chi2_stat)
print("p-value:", p_value)

# Interpret the results
if p_value < 0.05:
    print("The data does not appear to be consistent with the specified distribution (i.e., it is not random).")
else:
    print("The data appears to be consistent with the specified distribution (i.e., it is random).")