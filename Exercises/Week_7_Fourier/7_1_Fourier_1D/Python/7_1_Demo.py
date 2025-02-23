import numpy as np
import matplotlib.pyplot as plt

from signal_generator import generate_signal

duration = 2
sample_rate = 2000

x, y_1 = generate_signal(frequency=2, duration=duration, sample_rate=sample_rate)
_, y_2 = generate_signal(frequency=4, duration=duration, sample_rate=sample_rate)

y = y_1 + 0.3 * y_2


y_f = np.fft.fft(y)
x_f = np.fft.fftfreq(len(x), 1 / sample_rate)


y_f_filtered = y_f.copy()
y_f_filtered[x_f == 2] = 0
y_f_filtered[x_f == -2] = 0

y_filtered = np.fft.ifft(y_f_filtered)

plt.figure()
plt.plot(x, y)
plt.title("Gemischtes Signal Zeitraum")

plt.figure()
plt.plot(x_f, np.abs(y_f))
plt.title("Gemischtes Signal Frequenzraum")

plt.figure()
plt.plot(x, y_filtered)
plt.title("Gefiltertes Signal Zeitraum")
plt.plot(x, 0.3 * y_2)
plt.show()
