# import benutzter Module
import os 
import csv
from datetime import datetime 

csv_datei = "training_log.csv"

#csv datei einlesen
try:
    with open("training_log.csv", "a", encoding="utf-8", newline="") as file:
        reader = csv.reader(csv_datei) 
        print("Datei wurde erkannt")
        
except:
    print("Datei nicht gefunden!")
    
#aktuellen Dateipfad auslesen   
cwd = os.getcwd()
print(cwd)