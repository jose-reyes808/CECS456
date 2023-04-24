import numpy as np
import soundfile as sf
import librosa

import librosa.display
import matplotlib.pyplot as plt

import fnmatch
import os

# signal is the waveform in numpy form
def addWhiteNoise(signal, noiseFactor):
    noise = np.random.normal(0, signal.std(), signal.size)
    augmented_signal = signal + noise * noiseFactor
    return augmented_signal

# pitch scaling
def pitch_scale(signal, sr, num_semitones):
    return librosa.effects.pitch_shift(signal, sr, num_semitones)

# plot signals
def plot_signal_with_augmented(signal, augmentedSignal,sr ):
    fig, ax = plt.subplots(nrows=2)
    librosa.display.waveshow(signal, sr=sr, ax=ax[0])
    ax[0].set(title="Original Signal")
    librosa.display.waveshow(augmentedSignal, sr=sr, ax=ax[1])
    ax[1].set(title="Augmented Signal")
    plt.show()

if __name__ == "__main__":
    # signal, sampleRate = librosa.load("Track 41.wav")
    # augmented_signal = pitch_scale(signal, sampleRate, -2)
    # sf.write("Track_41_pitchScale2.wav", augmented_signal, sampleRate)
    #plot_signal_with_augmented(signal, augmented_signal, sampleRate)

    # process all files and add white  noise (10%)
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.wav'):
            signal, sampleRate = librosa.load(file)
            augmented_signal = addWhiteNoise(signal, 0.1)
            sf.write("whiteNoise_0_1_" + file, augmented_signal, sampleRate)