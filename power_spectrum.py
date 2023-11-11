import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

# Load the audio
audio_path = os.environ.get('SONG')
audio, sr = librosa.load(audio_path)

# Calculate the STFT
stft = librosa.stft(audio)

# Calculate the power spectrum (squared magnitude of the STFT)
power_spectrum = np.abs(stft)**2

# Convert power spectrum to decibels (optional)
power_spectrum_db = librosa.amplitude_to_db(power_spectrum, ref=np.max)

# Display the power spectrum
plt.figure(figsize=(12, 8))
librosa.display.specshow(power_spectrum_db, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Power Spectrum')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()
