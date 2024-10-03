# shoppinglist.py

# Definiere eine leere Einkaufsliste (List)
shoppinglist = []

# Funktion zum Hinzufügen eines Artikels zur Einkaufsliste
def add_item():
    # Frage den Benutzer nach einem Artikel
    item = input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll: ")
    
    # Füge den Artikel der Liste hinzu
    shoppinglist.append(item)
    
    # Gib eine Bestätigungsmeldung aus
    print(f"{item} wurde zur Einkaufsliste hinzugefügt.")

# Test der Funktion
if __name__ == "__main__":
    add_item()
    print("Aktuelle Einkaufsliste:", shoppinglist)
