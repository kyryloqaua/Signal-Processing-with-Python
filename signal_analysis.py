import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import os 
import soundfile as sf
import sounddevice as sd

# Load the audio
audio_path = os.environ.get('SONG')
y, sr = librosa.load(audio_path)

# Compute various features
hop_length = 512

# Beat track on the percussive signal
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# Compute MFCC features from the raw signal
mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=40)

# And the first-order differences (delta features)
mfcc_delta = librosa.feature.delta(mfcc)

# Compute Chromagram
chromagram = librosa.feature.chroma_cqt(y=y, sr=sr, hop_length=hop_length)

# Compute Tonnetz
tonnetz = librosa.feature.tonnetz(y=librosa.effects.harmonic(y), sr=sr)

# Compute Zero Crossing Rate
zero_crossings = librosa.feature.zero_crossing_rate(y)

# Visualize Beat Frames over Waveform
plt.figure(figsize=(10, 6))
librosa.display.waveshow(y, color='b')
plt.vlines(librosa.frames_to_time(beat_frames, sr=sr), ymin=-1, ymax=1, color='r', linestyle='--', alpha=0.7, label='Beats')
plt.title('Waveform with Beats')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# Visualize MFCC
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfcc, x_axis='time', sr=sr, hop_length=hop_length)
plt.colorbar(format="%+2.0f dB")
plt.title('MFCC')
plt.xlabel('Time (s)')
plt.ylabel('MFCC Coefficient')
plt.show()

# Visualize Delta Features
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfcc_delta, x_axis='time', sr=sr, hop_length=hop_length)
plt.colorbar(format="%+2.0f dB")
plt.title('MFCC Delta Features')
plt.xlabel('Time (s)')
plt.ylabel('Delta Coefficient')
plt.show()

# Visualize Chromagram
plt.figure(figsize=(10, 4))
librosa.display.specshow(chromagram, x_axis='time', sr=sr, hop_length=hop_length, cmap='coolwarm')
plt.colorbar()
plt.title('Chromagram')
plt.xlabel('Time (s)')
plt.ylabel('Pitch Class')
plt.show()

# Visualize Tonnetz
plt.figure(figsize=(10, 4))
librosa.display.specshow(tonnetz, x_axis='time', sr=sr, hop_length=hop_length, cmap='coolwarm')
plt.colorbar()
plt.title('Tonnetz')
plt.xlabel('Time (s)')
plt.ylabel('Coefficient')
plt.show()

# Visualize Zero Crossing Rate
plt.figure(figsize=(10, 4))
librosa.display.specshow(zero_crossings, x_axis='time', sr=sr, hop_length=hop_length, cmap='coolwarm')
plt.colorbar()
plt.title('Zero Crossing Rate')
plt.xlabel('Time (s)')
plt.ylabel('Zero Crossing Rate')
plt.show()



# Play the WAV file
# sd.play(y, sr)
# sd.wait()

# Separate harmonics and percussives into two waveforms
y_harmonic, y_percussive = librosa.effects.hpss(y)

sf.write('harmonic.wav', y_harmonic, sr)
sf.write('percussive.wav', y_percussive, sr)