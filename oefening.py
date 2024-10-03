# Oefening PROG1.1: Expressions

# expressie #uitkomst #type
# 5          5       int
# 5.0        5.0     float
# 5 % 2      2       int
# 5>1        False   Boolean
# "5"        "5"     string
# 5*2        10       int

# Oefening PROG1.2: Strings

# 1. Hoeveel letters zijn er in 'Supercalifragilisticexpialidocious'?
word = "Supercalifragilisticexpialidocious"
hoeveel_letters_in_word = len(word)

# 2 .Komt in 'Supercalifragilisticexpialidocious' de tekst 'ice' voor?
is_ice_in_word = word.find("ice")

# 3. Is het woord 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'?

word_two = "Antidisestablishmentarianism"
word_three = "Honorificabilitudinitatibus"

is_word_two_longer_than_word_three = len(word_two) > len(word_three)


# 4. Welke componist komt in alfabetische volgorde het eerst: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'?
componisten = [
    "Berlioz",
    "Borodin",
    "Brian",
    "Bartok",
    "Bellini",
    "Buxtehude",
    "Bernstein",
]
componisten.sort()

first_componist = componisten[0]

last_componist = componisten[len(componisten) - 1]

# Oefening PROG1.3: Statements
# 1.Ken de waarde 6 toe aan variabele a, en waarde 7 aan variabele b.
a = 6
b = 7

# 2. Ken aan variabele c als waarde het gemiddelde van a en b
c = (a + b) / 2

# 3. Ken aan variabelen voornaam, tussenvoegsel en achternaam je eigen naamgegevens toe.
voornaam = "Gilbert"
tussenvoegsel = ""
achternaam = "Sssempijja"

# 4. Ken aan variabele mijnnaam de variabelen van opdracht 3 (met spaties er tussen) toe.
mijnnaam = f"{voornaam} {tussenvoegsel} {achternaam}"


# Oefening PROG1.4: Boolean expressions

# 1. 6.75 groter is dan a en kleiner b.
oefening_een = 6.75 > a and 6.75 < b

# 2.de lengte van mijnnaam even groot is als de som van de lengtes van voornaam, tussenvoegsel en achternaam.
oefening_twee = len(mijnnaam) == sum(
    (len(voornaam), len(tussenvoegsel), len(achternaam))
)

# 3. de lengte van mijnnaam minstens 5 keer zo groot is als variabele c.
oefening_drie = len(mijnnaam) > (5 * c)


# 4. de waarde van variabele tussenvoegsel voorkomt in de waarde van variabele achternaam.
oefening_vier = achternaam.find(tussenvoegsel) > -1

# Oefening PROG1.5: Lists & strings
# 1.een nieuwe list met 1 artiest aan te maken met de naam favorieten
favorite_artists = ["Brent Faiyaz"]

# 2. de lijst uit te breiden met een tweede artiest.
favorite_artists.extend(["Frank", "Ocean"])

# 3. de tweede artiest te vervangen door een andere naam.
favorite_artists[1] = "Jimmy WOO"

# Oefening PROG1.6: Lists & numbers
lijst_met_nummers = [0, 24, 43, 3434, 342, -2, 34, -55]
lijst_met_nummers.sort()
verschil_tussen_kleinste_en_grootste_getal = (
    lijst_met_nummers[(len(lijst_met_nummers) - 1)] - lijst_met_nummers[0]
)


# Oefening PROG1.7: Tuples
letters = ("A", "C", "B", "B", "C", "A", "C", "C", "B")

# sorten van letters
sorted(letters)

# letters sorten
aantaal_voorkomens = []
for letter in letters:
    occurence_letter = letters.count(letter)
    if occurence_letter not in aantaal_voorkomens:
        aantaal_voorkomens.append(occurence_letter)

print("aantaal_voorkomens", aantaal_voorkomens)
