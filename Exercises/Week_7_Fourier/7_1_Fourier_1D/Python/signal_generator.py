import numpy as np


def generate_signal(frequency, duration, sample_rate):
    """Generate a sine signal with varying frequency, duration and sample rate

    credits go to: https://realpython.com/python-scipy-fft/

    Args:
        frequency (_type_): frequency of the sine signal
        duration (_type_): duration of signal in seconds
        sample_rate (_type_): sample rate of the signal in Hz

    Returns:
        x: time points
        y: sin(x)
    """
    x = np.linspace(0, duration, sample_rate * duration)
    y = np.sin(2 * np.pi * frequency * x)

    return x, y
