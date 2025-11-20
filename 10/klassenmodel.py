#Modellierung eines Rechnungsbelegs 
#get = lesen , set = verändern
import datetime as dt

class Invoice: 
    def __init__(self): 
        self._nummer = self._set_number()
        self._datum = dt.date.today()
        self._items = []
       
        
    def __str__(self): 
        invoice_string = f"\nRechnungsnr: {self._nummer} Rechnungsdatum: {self._datum}"
        
        invoice_string += f"\n\nPositionen:" 
        for item in self._items:
            invoice_string += f"\n{item.__str__()}"
        return invoice_string
    
    
    def _set_number(self): 
        return 187
        
    def _get_new_items_id(self):
        try: 
            max_id = max(item.get_item_id() for item in self._items)
            return max_id + 1
        except:
            return 1
    
    def add_items(self, description, quantity, net_price_per_unit): 
        item = Item(
            items_id = self._get_new_items_id(),
            description = description,
            quantity = quantity,
            net_price_per_unit = net_price_per_unit
        )
        self._items.append(item)
        
    def get_items(self):
        return self._items.copy()


    

class Item():
    def __init__(self, items_id, description, quantity, net_price_per_unit,): 
        self._id = items_id 
        self._description = description 
        self._quantity = quantity
        self._net_price_per_unit = net_price_per_unit
        self._net_total = self._quantity * self._net_price_per_unit 
        self._total_price = self._net_total * 1.19
    
    def get_item_id(self): 
        return self._id
    
    
    def __str__(self):
        return f"{self._id} | {self._description} | {self._net_price_per_unit} | {self._net_total} | {self._total_price}\n"


invoice_bsp = Invoice()
invoice_bsp.add_items(
    description = "Porsche 964 dunkelgrün",
    quantity= 2, 
    net_price_per_unit= 80000
)
invoice_bsp.add_items(
    description = "Ferrari f40 rot",
    quantity= 1, 
    net_price_per_unit= 450000
)
invoice_bsp.add_items(
    description = "VW Polo schwarz",
    quantity= 3, 
    net_price_per_unit= 12000
)

print(invoice_bsp)

"""for item in invoice_bsp.get_items():
    print(f"{item.get_item_id()}| {item._description}| {item._net_price_per_unit}| {item._net_total}") 
"""


class Kunde: 
    def __init__(self, nummer, name, rechnungsadresse):
        self.nummer = nummer
        self.name = name 
        self.rechnungsadresse = rechnungsadresse

class Rechnungssteller(): 
    def __init__(self, ust_id, adresse):
        self.ust_id = ust_id
        self.adresse = adresse 
        


class Zahlungsart(): 
    def __init__(self, name): 
        self.name = name
    
    def bezahlen(self): 
        raise NotImplementedError()
    
    def __str__(self): 
        return f"Zahlungsart: {self.name}"


class Ueberweisung(Zahlungsart): 
    def __init__(self, iban, name):
        super().__init__(name) #self wird schon übernommen
        self.iban = iban
    
    def bezahlen(self, betrag): 
        return f"{betrag} wurde via Überweisungskonto {self.iban} gesendet"
    
    

class Kreditkarte(Zahlungsart): # methoden in  oop und funktionen in funktionsorientierprog.
    def __init__(self, nummer, name):
        super().__init__(name) 
        self.nummer = nummer
    
    def bezahlen(self, betrag): 
        return f"{betrag} wurde via Kreditkarte {self.nummer} gesendet"
       

class Paypal(Zahlungsart): 
    def __init__(self, email, name):
        super().__init__(name) 
        self.email = email
       
    
    def bezahlen(self, betrag):
        return f"{betrag} wurde via PayPal {self.email} gesendet"



zahlung1 = Ueberweisung(name="carl", iban="123445755")
print(zahlung1.bezahlen(betrag=1234))

zahlung2 = Kreditkarte(name="otto", nummer="538393462")
print(zahlung2.bezahlen(betrag=238000))

zahlung2 = Paypal(name="gustav", email="gustav.servus@icloud.com")
print(zahlung2.bezahlen(betrag=300000))    



class Absender: 
    def __init__(self):
        pass
    
class Empfaenger: 
    def __init__(self):
        pass
    