import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

# Load the example clip
audio_path = os.environ.get('SONG')
y, sr = librosa.load(audio_path)

# Compute the spectrogram
spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)

# Convert to decibels (log scale)
log_spectrogram = librosa.power_to_db(spectrogram, ref=np.max)

# Plot the 3D spectrogram
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Create meshgrid for time and frequency axes
t = np.linspace(0, y.shape[0] / sr, log_spectrogram.shape[1])
f = librosa.mel_frequencies(n_mels=log_spectrogram.shape[0])

T, F = np.meshgrid(t, f)

# Plot the spectrogram on the meshgrid
ax.plot_surface(T, F, log_spectrogram, cmap='viridis')

# Set labels and title
ax.set_xlabel('Time (s)')
ax.set_ylabel('Frequency (Hz)')
ax.set_zlabel('Magnitude (dB)')
ax.set_title('3D Spectrogram')

plt.show()