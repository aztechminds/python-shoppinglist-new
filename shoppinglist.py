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

# Funktion zum Anzeigen der Einkaufsliste

def show_shoppinglist():
    # prüfe, ob die Liste leer ist
    if  shoppinglist:
        print("Deine Einkaufsliste:")
        
        # for loop zum Anzeigen der Artikel in der Einkaufsliste
        for item in shoppinglist:
            print(f"- {item}")
    else: 
        print ("Deine Einkaufsliste ist leer.")

# Hauptfunktion
def main():
    while True:
        # Anzeige des Menüs
        print("\n----- Einkaufsliste -----")
        print("1. Artikel zur Einkaufsliste hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Programm beenden")
        
        # Frage den Benutzer nach seiner Wahl
        choice = input("Bitte wähle eine Option (1, 2 oder 3): ")
        
        # Prüfe die Auswahl
        if choice == "1":
            add_item()
        elif choice == "2":
            show_shoppinglist()
        elif choice == "3":
            print("Programm wird beendet! Auf Wiedersehen")
            break  # Beende die Schleife und das Programm
        else:
            print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3")

# Starte das Programm nur, wenn dieses Skript direkt ausgeführt wird
if __name__ == "__main__":
    main()

