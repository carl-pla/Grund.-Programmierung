import datetime as dt

# Rechnung
class Invoice:
    tax_rate = 0.19 #Klassenatribbut ist für alle Instanzen gleich, keine Konstante (in Großbuchstaben), da es auch geändert werden kann

    def __init__(self):
        self._number = self._set_number() #darf nicht von außen mitgenommen werden (unikate nummer), __ = private, darf nicht vererbt werden
        self._date = dt.date.today()
        self._items = []
        self._net_total = 0
        self._tax = 0
        self._total = 0
        self._payment_type = None  #Muss vom Aufrufenden gesetzt werden

    def _set_number(self): # _ = proteced, nicht von außen zugreifen
        # vorübergehende Lösung: Eine Rechnungsnummer muss eindeutig sein
        return 42

    def _get_new_item_id(self):
        try:
            max_id = max(item.get_id() for item in self._items) # id wird aufsteigend zugeteilt, max id definiert
            return max_id + 1
        except:
            return 1

    def add_item(self, description, quantity, net_price_per_unit):
        item = Item(
            id=self._get_new_item_id(),
            description=description,
            quantity=quantity,
            net_price_per_unit=net_price_per_unit
        )
        self._items.append(item)
        # Update der Totals nach Hinzufügen einer neuen Position erforderlich
        self._calculate_totals()

    def get_date(self):
        return self._date

    def get_items(self):
        return self._items.copy()  #flache Kopie

    def _calculate_totals(self):
        # Initialisierung der Werte (relevant bei erneuter Berechnung)
        self._net_total = 0
        self._tax = 0
        self._total = 0
        for item in self._items:
            self._net_total += item.get_net_total()

        self._tax = self._net_total * Invoice.tax_rate
        self._total = self._net_total + self._tax

    def set_payment_type(self, payment_type):
        self._payment_type = payment_type

    def __str__(self):
        # Überschrift
        invoice_string = f"Rechnung {self._number}\nRechnungsdatum {self._date}"
        #Positionen
        invoice_string += f"\n\nPositionen:"
        for item in self._items:
            invoice_string += f"\n{item.__str__()}"
        # Totals
        # :.f sorgt für eine Ausgabe mit 2 Nachkommastellen (gerundet wird mit Banker's Rounding)
        invoice_string += f"\n\nZwischensumme (netto): {self._net_total:.2f}" \
                          f"\nSteuer: {self._tax:.2f}" \
                          f"\nGesamtbetrag: {self._total:.2f}"
        # Zahlungsbedingungen
        invoice_string += f"\n\nZahlungsbedingungen\n" \
                          f"{self._payment_type.get_payment_terms()}"

        return invoice_string
    

# Positionen
class Item:
    def __init__(self, id, description, quantity, net_price_per_unit):
        self._id = id
        self._description = description
        self._quantity = quantity
        self._net_price_per_unit = net_price_per_unit
        self._net_total = self._quantity * self._net_price_per_unit

    def get_id(self):
        return self._id

    def get_net_total(self):
        return self._net_total

    def __str__(self):
        return f"{self._id} {self._description} {self._net_price_per_unit} {self._net_total}"
    

# Zahlungsarten
class PaymentType:
    def get_payment_terms(self):
        # Muss in Subklassen implementiert werden
        # Durch Vererbung gibt es die gemeinsame Schnittstelle/Methode get_payment_terms
        return None



# Überweisung
class BankTransfer(PaymentType):
    def __init__(self, iban, due_date, account_holder):
        # Aufruf von __init__ der Superklasse hier noch irrelevant,
        # bei zukünftiger Erweiterung der Superklasse aber ggf. wichtig
        self._iban = iban
        self._due_date = due_date  #Fälligkeitsdatum
        self._account_holder = account_holder  #Kontoinhaber

    def get_payment_terms(self):
        # könnte natürlich auch in der __str__-Methode implementiert werden.
        # get_payment_terms ist allerdings ein verständlicherer Name
        payment_terms = f"Bitte überweisen Sie den Gesamtbetrag " \
                        f"bis zum {self._due_date} " \
                        f"auf das Konto\n\n" \
                        f"{self._account_holder}\n" \
                        f"IBAN: {self._iban}"
        return payment_terms



class PayPal(PaymentType):
    def get_payment_terms(self):
        return "Betrag bereits mit PayPal beglichen."
    
invoice_bank_transfer = Invoice()
invoice_bank_transfer.add_item(
    description="Kyberkristall (für Lichtschwert)",
    quantity=1,
    net_price_per_unit=3000
)
invoice_bank_transfer.add_item(
    description="Wartung Lichtschwert (Reinigung, Justage)",
    quantity=1,
    net_price_per_unit=350
)
invoice_bank_transfer.add_item(
    description="Düsentriebwerk für T-16 Skyhopper",
    quantity=2,
    net_price_per_unit=1299
)

invoice_bank_transfer.set_payment_type(
    BankTransfer(
        iban="DE12 3456 7890 1234 5678 00",
        due_date=invoice_bank_transfer.get_date() + dt.timedelta(weeks=2),  # Fälligkeitsdatum 2 Wochen später
        account_holder="Imperiale Technikhandel GmbH"
    )
)

print(invoice_bank_transfer)

invoice_paypal = Invoice()
invoice_paypal.add_item(
    description="Kyberkristall (für Lichtschwert)",
    quantity=1,
    net_price_per_unit=3000
)
invoice_paypal.add_item(
    description="Wartung Lichtschwert (Reinigung, Justage)",
    quantity=1,
    net_price_per_unit=350
)
invoice_paypal.add_item(
    description="Düsentriebwerk für T-16 Skyhopper",
    quantity=2,
    net_price_per_unit=1299
)

invoice_paypal.set_payment_type(PayPal())

print(invoice_paypal)