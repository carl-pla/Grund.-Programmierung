def aussortieren():
    zahlen = {
    "A" : "4",
    "B" : "8",
    "E" : "3",
    "G" : "6",
    "I" : "1",
    "S" : "5",
    "T" : "7",
    }
    neues_zitat = ""
    
    for zeichen in zitat:
        if zeichen.upper() in zahlen:
            neues_zitat = neues_zitat + aussortieren[zeichen.upper()]
        else:
            neues_zitat = neues_zitat + zeichen
    return neues_zitat

# Test mit dem gegebenen Zitat
zitat = "The measure of Intelligence is the Ability to Change. Albert Einstein"
ergebnis = aussortieren(zitat)
print(ergebnis)



