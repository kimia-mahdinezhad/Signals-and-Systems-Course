from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np


def draw_plot():
    # energy
    speaking = False
    figure1 = plt.figure(1)
    plt.plot(signal_energy)

    j = 0
    for i in signal_energy:
        if i[0] > 0.3 and not speaking:
            speaking = True
            plt.axvline(x=j, color='blue')

        if i[0] < 0.3 and speaking:
            speaking = False
            plt.axvline(x=j, color='blue')

        j += 1

    # absolute
    speaking = False
    figure2 = plt.figure(2)
    plt.plot(signal_abs)

    j = 0
    for i in signal_abs:
        if i[0] > 1 and not speaking:
            speaking = True
            plt.axvline(x=j, color='blue')

        if i[0] < 1 and speaking:
            speaking = False
            plt.axvline(x=j, color='blue')

        j += 1

    plt.show()


# reading file
recordingRate, recordingData = wavfile.read('mySpeech.wav')
length = recordingData.shape[0] / recordingRate

time = np.linspace(0., length, recordingData.shape[0])

sig = recordingData[:] / np.power(2, 15)

# calculating energy
frame = round(recordingRate / 50)
signal_energy = []
signal_abs = []

for i in range(0, len(sig) - round(frame / 2), round(frame / 2)):
    x = sig[i:i + frame]
    signal_energy.append(sum(x * x))
    signal_abs.append(sum(abs(x)))

draw_plot()