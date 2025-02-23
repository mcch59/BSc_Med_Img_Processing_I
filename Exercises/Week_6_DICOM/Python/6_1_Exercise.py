import pydicom
import matplotlib.pyplot as plt

ds = pydicom.dcmread("Patient_Scan/IMG0050.dcm")

print(ds.__dir__())

print(f"Name des Patienten: {ds.PatientName}")
print(f"Geschlecht: {ds.PatientSex}")
print(f"Patient ID: {ds.PatientID}")
print(f"Studient-ID: {ds.StudyID}")
print(f"Bildgebungsverfahren: {ds.Modality}")
print(f"Datum Bild-Aufnahme: {ds.StudyDate}")
print(f"Uhrzeit Bildaufnahme: {ds.StudyTime}")
print(f"Pixel-Abstand: {ds.PixelSpacing}")
print(f"Scan Koordinaten: {ds.ImagePositionPatient}")
print(f"Scan Ausrichtung: {ds.ImageOrientationPatient}")

image = ds.pixel_array

plt.figure()
plt.imshow(image, cmap="gray")

plt.show()
