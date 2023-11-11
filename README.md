# Signal Processing with Python

## Overview

This project focuses on signal processing using Python, particularly analyzing the audio track "b1. stranno neobjatno" by Nina Kraviz. Various signal processing characteristics have been explored, and visualizations have been generated to better understand the underlying sound properties.

## Table of Contents

- [Installation](#installation)
- [Libraries Used](#libraries-used)
- [Project Structure](#project-structure)
- [Graphs](#graphs)
- [Theoretical Background](#theoretical-background)
  - [Sound Processing](#sound-processing)
  - [Signals](#signals)
  - [Frequency Analysis](#frequency-analysis)
  - [FFT (Fast Fourier Transform)](#fft-fast-fourier-transform)
  - [Spectrogram](#spectrogram)
  - [Harmonic and Percussive Components](#harmonic-and-percussive-components)
- [PyQT5 Visualization](#pyqt5-visualization)

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/Signal-Processing-with-Python.git
cd Signal-Processing-with-Python
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Libraries Used

The project utilizes the following Python libraries:

- NumPy
- Matplotlib
- Librosa
- PyQt5
- Pyqtgraph

Make sure to install these libraries before running the scripts.

## Project Structure

```plaintext
Signal-Processing-with-Python/
│
├── scripts/
│   ├── script1.py
│   ├── script2.py
│   └── ...
│
├── visualization/
│   ├── pyqt5_visualizer.py
│   └── ...
│
└── pngs/
    ├── 2d_spectogram.png
    ├── 3D_spectrogram_fft.png
    ├── 3d_spectrogram.png
    ├── Chromagram.png
    ├── MFCC Delta Coefficient.png
    ├── MFCC.png
    ├── Power spectrum.png
    ├── Tonnetz.png
    ├── Waveform with Beats.png
    └── Waveform.png
```

## Graphs

- **2d_spectogram.png:** A two-dimensional representation of the frequency content of the audio signal over time.
- **3D_spectrogram_fft.png:** A three-dimensional representation of the spectrogram with emphasis on the Fast Fourier Transform (FFT).
- **3d_spectrogram.png:** A three-dimensional visualization of the frequency content of the audio signal.
- **Chromagram.png:** A representation of the pitch content of the audio signal.
- **MFCC Delta Coefficient.png:** Mel-frequency cepstral coefficients (MFCC) delta coefficient visualization.
- **MFCC.png:** Visualization of Mel-frequency cepstral coefficients, providing information about the audio's spectral characteristics.
- **Power spectrum.png:** Displaying the distribution of power in the frequency spectrum.
- **Tonnetz.png:** Visualization of tonnetz features, capturing harmonic relationships in the audio signal.
- **Waveform with Beats.png:** Audio waveform with beats highlighted, showcasing rhythmic components.
- **Waveform.png:** Standard representation of the audio signal waveform.

## Theoretical Background

### Sound Processing

Sound processing involves the manipulation, analysis, and synthesis of audio signals. It plays a crucial role in various applications such as speech recognition, music production, and telecommunications.

### Signals

In the context of audio processing, signals represent variations in air pressure over time. These variations are captured and processed to extract meaningful information from sound.

### Frequency Analysis

Frequency analysis is essential for understanding the distribution of frequencies within an audio signal. It aids in identifying key features, such as pitch and timbre.

### FFT (Fast Fourier Transform)

The Fast Fourier Transform is an algorithm used to efficiently compute the discrete Fourier transform, providing insights into the frequency components of a signal.

### Spectrogram

A spectrogram is a visual representation of the spectrum of frequencies in a signal as they vary with time. It's a valuable tool for identifying patterns and trends in audio signals.

### Harmonic and Percussive Components

Harmonic components represent pitched elements, while percussive components capture non-pitched, rhythmic elements. Distinguishing between these components provides insights into the structure of the audio.

## PyQT5 Visualization

A subpart of this project involves a PyQt5 visualization using pyqtgraph. The `pyqt5_visualizer.py` script creates an interactive 3D plot with evolving step functions. This visualization provides a dynamic representation of the audio signal's characteristics.

```python
# [Insert the code for PyQt5 visualization here]
```

---

Feel free to adjust the descriptions and content based on your project's specific details.
>>>>>>> c9eda0fe (Initial commit)
