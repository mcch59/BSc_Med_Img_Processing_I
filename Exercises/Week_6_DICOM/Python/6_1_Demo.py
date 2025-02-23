import pydicom 

ds = pydicom.dcmread("Patient_Scan/IMG0001.dcm")

print(ds.__dir__())

print(f"Patient ID: {ds.PatientID}")
print(f"Name des Patienten: {ds.PatientName}")