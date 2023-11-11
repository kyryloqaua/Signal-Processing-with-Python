import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Import Axes3D for 3D plotting
import os

# Load the example clip
audio_path = os.environ.get('SONG')
y, sr = librosa.load(audio_path)

# Compute the spectrogram
spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=8192, hop_length=256, n_mels=128)

# Convert to decibels (optional)
spectrogram_db = librosa.amplitude_to_db(spectrogram, ref=np.max)

# Get the time and frequency axes
times = librosa.times_like(spectrogram_db)
freqs = librosa.mel_frequencies(n_mels=128, fmin=librosa.note_to_hz('C1'), fmax=librosa.note_to_hz('C7'))

# Create a 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D spectrogram with transposed array
times_mesh, freqs_mesh = np.meshgrid(times, freqs)
ax.plot_surface(times_mesh.T, freqs_mesh.T, spectrogram_db.T, cmap='viridis')

# Set labels
ax.set_xlabel('Time (s)')
ax.set_ylabel('Frequency (Hz)')
ax.set_zlabel('Amplitude (dB)')
ax.set_title('3D Spectrogram n_fft = 8192, hop_length = 256, n_mels = 128')

plt.show()
