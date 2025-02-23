import numpy as np
import matplotlib.pyplot as plt
import pydicom
import os

# Angabe Ordner Pfad. Hier befindet sich der Ordner im gleichen Ordner wie das Skript
folder_path = "Patient_Scan"

file_names = os.listdir(folder_path)
print(file_names)

all_slices = np.zeros(shape=[256, 130, 256])
coordinates = []

# iteriere durch alle Slices und extrahiere Bild + Koordinaten
for i, file_name in enumerate(file_names):
    ds = pydicom.dcmread(f"{folder_path}/{file_name}")
    all_slices[:, i, :] = ds.pixel_array
    coordinates.append(ds.ImagePositionPatient[0])

# Berechne die Reihenfolge, um chronologisch zu sortieren
order = np.argsort(coordinates)

# Wende die Reihenfolge auf Slices an, um Slices chronologisch zu sortieren
all_slices = all_slices[:, order, :]


coordinates = np.array(coordinates)[order]
print(coordinates[:10])  # Bestätigung, dass Koordinaten richtig sortiert sind
