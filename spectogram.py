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

# Plot the spectrogram
plt.figure(figsize=(10, 6))
librosa.display.specshow(log_spectrogram, sr=sr, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('3D Spectrogram')
plt.tight_layout()
plt.show()