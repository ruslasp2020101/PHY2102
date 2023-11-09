# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy import signal

# Define circuit parameters
# Resistance (R) in Ohms
R = 1
# Inductance (L) in Henrys (1 mH)
L = 1e-3
# Capacitance (C) in Farads (1 nF)
C = 1e-9
# Root mean square voltage (Vrms) in Volts
Vrms = 1

# Frequency range for the plot
freq_range = np.logspace(3, 7, 1000)  # Frequency range from 1 kHz to 10 MHz

# Calculate impedance of the RLC circuit as a function of frequency
omega = 2 * np.pi * freq_range
Z = R + 1j * (omega * L - 1 / (omega * C))

# Calculate current amplitude
I_amplitude = Vrms / np.abs(Z)

# Calculate power as a function of frequency (P = I^2 * R)
power = (I_amplitude ** 2) * R

# Find the resonance frequency
peaks, _ = find_peaks(power)
resonance_freq = freq_range[peaks][0]

# Calculate the half-width of the resonance peak
half_width = R / (2 * np.pi * L)

# Plot the power as a function of frequency
plt.figure(figsize=(10, 6))
plt.semilogx(freq_range, power)
plt.title('Power vs Frequency for RLC Circuit')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power (W)')
plt.grid(True)

# Highlight the resonance peak
plt.plot(freq_range[peaks], power[peaks], 'ro', label='Resonance Peak')

# Display the resonance frequency and half-width on the plot
plt.text(resonance_freq, power[peaks], f'Resonance Frequency = {resonance_freq:.2e} Hz', ha='right')
plt.text(resonance_freq, power[peaks] * 0.9, f'Half-Width = {half_width:.2e} Hz', ha='right')

plt.legend()
plt.show()

# Print the resonance frequency and half-width
print(f'Resonance Frequency: {resonance_freq:.2e} Hz')
print(f'Half-Width of Resonance Peak: {half_width:.2e} Hz')
