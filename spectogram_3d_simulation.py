import numpy as np
import librosa.display
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import os

# Load the audio file
audio_path = os.environ.get('SONG')
audio, sr = librosa.load(audio_path)

# Compute the spectrogram
spectrogram = librosa.feature.melspectrogram(y=audio, sr=sr, n_fft=2048, hop_length=256, n_mels=128)

# Convert to decibels (optional)
spectrogram_db = librosa.amplitude_to_db(spectrogram, ref=np.max)

# Get the time and frequency axes
times = librosa.times_like(spectrogram_db)
freqs = librosa.mel_frequencies(n_mels=128, fmin=librosa.note_to_hz('C1'), fmax=librosa.note_to_hz('C7'))

# Create a 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Initialize the plot with an empty surface
times_mesh, freqs_mesh = np.meshgrid(times, freqs)
plot = ax.plot_surface(times_mesh.T, freqs_mesh.T, np.zeros_like(spectrogram_db.T), cmap='viridis')

# Set labels and title with white color
ax.set_xlabel('Time (s)', color='white')
ax.set_ylabel('Frequency (Hz)', color='white')
ax.set_zlabel('Amplitude (dB)', color='white')
ax.set_title('Real-time 3D Spectrogram (Without Playback)', color='white')

# Set the viewing angle
ax.view_init(elev=25, azim=-50)

# Add color bar
cbar = fig.colorbar(plot, ax=ax, pad=0.1)
cbar.set_label('Intensity (dB)', color='white')
cbar.ax.yaxis.set_tick_params(color='white')
cbar.outline.set_edgecolor('white')

# Initialize variables for real-time updating
frame_count = 0
frame_width = 3  # Adjust frame width as needed

# Update function for animation
def update(frame):
    global frame_count, plot
    
    # Compute the new spectrogram frame
    start_frame = frame * 256  # Adjust hop_length as needed
    end_frame = (frame + frame_width) * 256
    current_spectrogram = spectrogram_db[:, start_frame:end_frame]
    times_mesh, freqs_mesh = np.meshgrid(times[start_frame:end_frame], freqs)

    # Update the existing plot data
    plot.remove()
    plot = ax.plot_surface(times_mesh.T, freqs_mesh.T, current_spectrogram.T, cmap='viridis')

    ax.set_xlabel('Time (s)', color='white')
    ax.set_ylabel('Frequency (Hz)', color='white')
    ax.set_zlabel('Amplitude (dB)', color='white')
    ax.set_title('Real-time 3D Spectrogram (Without Playback)', color='white')

    frame_count += 1

# Create animation
duration_in_seconds = 1
num_frames = int((duration_in_seconds * sr) / 256)
ani = FuncAnimation(fig, update, frames=num_frames, interval=50)

# Set the background color to black
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Save the animation as a video file (adjust the filename and codec as needed)
ani.save('real_time_spectrogram_animation.mp4', writer='ffmpeg', fps=30, codec='h264', bitrate=1800)

# Show the plot
plt.show()
