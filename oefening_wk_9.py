def oefening_9_4() -> str:
    while True:
        try:
            # Wat verdien je per uur: 3.80
            # Hoeveel uur heb je gewerkt: 20
            # 20 uur werken levert €76.0 op

            uur_loon: float = float(input("Wat verdien je per uur: "))
            gewerkte_uur: float = float(input("Hoeveel uur heb je gewerkt: "))
            print(f"{gewerkte_uur} uur werken levert €{gewerkte_uur * uur_loon} op")

        except ValueError:
            print(f"Fout! voer een getal in")


def oefening_9_2() -> None:
    lijst = ["a", "b", "c"]

    # Waarom kun je in de functie niet de opdracht lijst = ['d', 'e', 'f'] geven?
    def wijzig(list):
        # Je kan de waardes in de de lijst aanpassen maar niet de lijst zelf door de scopes
        list[0] = "d"
        list[1] = "e"
        list[2] = "f"

    print(lijst)
    wijzig(lijst)
    print(lijst)

#Werkt jouw functie ook met een string-parameter? Probeer dit! Waarom werkt het wel/niet?
#nee dit werkt niet omdat een een string kan bekijken met een index maar kan dat niet aanpassem
#de string is unmutable 
def oefening_9_2_1() -> None:
    parameter = "programeren"
    
    def wijzig(parameter):
        parameter = "John Jones"

    print(parameter)
    wijzig(parameter)
    print(parameter)   



if __name__ == "__main__":
    results = oefening_9_2_1()
    print(results)
