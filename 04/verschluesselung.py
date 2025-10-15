# Aufgabe 2 
def verschluesseln(text): 
  
    aussortieren = {
    "A": "4",
    "B": "8",
    "E": "3",
    "G": "6",
    "I": "1",
    "S": "5",
    "T": "7"
}
    neuer_text = ""
    for zeichen in text:
        # Großbuchstaben in zeichen prüfen
        if zeichen.upper() in aussortieren:
            neuer_text = neuer_text + aussortieren[zeichen.upper()]
        else:
            neuer_text = neuer_text + zeichen
    return neuer_text


# Test mit dem gegebenen Zitat
zitat = "The measure of Intelligence is the Ability to Change. Albert Einstein"
ergebnis = verschluesseln(zitat)
print(ergebnis)


