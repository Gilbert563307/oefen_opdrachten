# Schrijf een functie namen()
def namen():
    names = {}
    # die de gebruiker steeds opnieuw vraagt om de voornaam van een student in de klas
    while True:
        voornaam = input("Wat is je voornaam: ")
        # Plaats de namen als sleutel (key) in een dict, en hou als waarde (value) bij hoe vaak ze zijn voorgekomen.
        if voornaam != "":
            occurence = 0
            if names.get(voornaam) == None:
                names[voornaam] = occurence
            for key in names.keys():
                if key == voornaam:
                    names[voornaam] = names[voornaam] + 1

        # als de gebruiker een lege tekst invoert, stopt het programma en moet van elke naam geprint worden hoe vaak de naam in de klas voorkomt.
        if voornaam == "":
            for key in names:
                str_occurence = names.get(key)
                if str_occurence > 1:
                    print(f"Er zijn {str_occurence} studenten met de naam {key}")
                else:
                    print(f"Er is {str_occurence} student met de naam {key}")
            break


namen()
