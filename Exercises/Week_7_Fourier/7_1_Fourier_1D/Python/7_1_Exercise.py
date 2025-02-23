import numpy as np
import matplotlib.pyplot as plt


from signal_generator import generate_signal


duration = 1
sample_rate = 2000
base_frequency = 2
x, base_signal = generate_signal(
    frequency=base_frequency, duration=duration, sample_rate=sample_rate
)
_, noise_1 = generate_signal(frequency=10, duration=duration, sample_rate=sample_rate)

_, noise_2 = generate_signal(frequency=5, duration=duration, sample_rate=sample_rate)

y = base_signal + 0.3 * noise_1 - 0.5 * noise_2
y_f = np.fft.fft(y)


N = duration * sample_rate
x_f = np.fft.fftfreq(N, 1 / sample_rate)  # Berechne die Frequenzen zu dem Spektrum
# Maximale Frequenz = Nyquist Frequenz = N/2 = sample_rate/2
# Kleinste Frequenz = 1/Duration bzw. sample_rate / N


# Filtering

y_f_filtered = y_f.copy()
y_f_filtered[np.where(x_f == 10)] = 0
y_f_filtered[np.where(x_f == -10)] = 0

y_f_filtered[np.where(x_f == 5)] = 0
y_f_filtered[np.where(x_f == -5)] = 0

y_filtered = np.fft.ifft(y_f_filtered)


plt.figure()
plt.plot(x, y)
plt.title("Basis Signal mit Störsignal")

plt.figure()
plt.plot(x_f, np.abs(y_f))
plt.axis([-20, 20, 0, 1.1 * np.abs(y_f_filtered.max())])
plt.title("Frequenz-Spektrum gemischtes Signal")


plt.figure()
plt.plot(x_f, np.abs(y_f_filtered))
plt.axis([-20, 20, 0, 1.1 * np.abs(y_f_filtered.max())])
plt.title("Frequenz-Spektrum mit Filterung")

plt.figure()
plt.plot(x, y_filtered)
plt.title("Gefiltertes Signal mit Originalsignal überlagert")
plt.plot(x, base_signal)
plt.legend(["Gefiltertes Signal", "Original-Signal"])

plt.show()
