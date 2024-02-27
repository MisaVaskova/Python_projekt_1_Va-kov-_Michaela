"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michaela Vašková
email: vaskova.mich@seznam.cz
discord: misav19
"""
import sys
prihlasovaci_jmeno = input("username: ")
heslo = input("password: ")
registrovani_uzivatele = {"bob": "123", "ann": "pass123", "mike": "passworld123", "liz": "pass123"}
oddelovac = "-" * 50

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]

print(oddelovac)

if registrovani_uzivatele.get(prihlasovaci_jmeno) == heslo:
    print("Welcome to the app, ", prihlasovaci_jmeno,
          "\nWe have 3 texts to be analyzed.",
          "\n" + oddelovac)
else:
    print("username:", prihlasovaci_jmeno,
          "\npassword:", heslo,
          "\nunregistred user, terminating the program.")
    sys.exit()

vyber = input("Enter a number btw. 1 and 3 to select: ")
if not vyber.isdigit() or int(vyber) < 1 or int(vyber) > 3:
    print("Invalid selection. The program will be terminated.")
    sys.exit()

print(oddelovac)

vybrany_text = TEXTS[int(vyber) - 1].split()

pocet_slov = 0
pocet_slov_s_velkym_pismenem = 0
pocet_slov_psanych_velkymi_pismeny = 0
pocet_slov_psanych_malymi_pismeny = 0
pocet_cisel = 0
suma_cisel = 0

for slova in vybrany_text:
    pocet_slov += 1
    if slova.istitle():
        pocet_slov_s_velkym_pismenem += 1
    elif slova.isupper():
        pocet_slov_psanych_velkymi_pismeny += 1
    elif slova.islower():
        pocet_slov_psanych_malymi_pismeny += 1
    elif slova.isdigit():
        pocet_cisel += 1
        suma_cisel += int(slova)

if vybrany_text == 1:
    print("There are", pocet_slov, "words in the selected text.",
          "\nThere are", pocet_slov_s_velkym_pismenem, "titlecase words.",
          "\nThere are", pocet_slov_psanych_velkymi_pismeny, "uppercase words.",
          "\nThere are", pocet_slov_psanych_malymi_pismeny, "lowercase words.",
          "\nThere are", pocet_cisel, "numeric string.",
          "\nThe sum of all the numbers", suma_cisel)
elif vybrany_text == 2:
    print("There are", pocet_slov, "words in the selected text.",
          "\nThere are", pocet_slov_s_velkym_pismenem, "titlecase words.",
          "\nThere are", pocet_slov_psanych_velkymi_pismeny, "uppercase words.",
          "\nThere are", pocet_slov_psanych_malymi_pismeny, "lowercase words.",
          "\nThere are", pocet_cisel, "numeric string.",
          "\nThe sum of all the numbers", suma_cisel)
else:
    print("There are", pocet_slov, "words in the selected text.",
          "\nThere are", pocet_slov_s_velkym_pismenem, "titlecase words.",
          "\nThere are", pocet_slov_psanych_velkymi_pismeny, "uppercase words.",
          "\nThere are", pocet_slov_psanych_malymi_pismeny, "lowercase words.",
          "\nThere are", pocet_cisel, "numeric string.",
          "\nThe sum of all the numbers", suma_cisel)

delka_slov = [len(slova) for slova in vybrany_text]
set_delka_slov = set(delka_slov)
pocitani_delky_slov = {}

for delka in set_delka_slov:
    pocitani_delky_slov[delka] = delka_slov.count(delka)

max_hodnota = max(pocitani_delky_slov.values())
max_klic = max(pocitani_delky_slov.keys())
max_delka_klice = len(str(max_klic))
delka_occ = len("OCCURENCES")
occ_vyskyt = 1

if ((max_hodnota - delka_occ) / 2 + 1) % 2 == 0:
    occ_vyskyt = 0

print(oddelovac)

print(f"{'LEN|': <{max_delka_klice + 1}}{' ': >{(max_hodnota - delka_occ) / 2 + 1}}{'OCCURENCES'}"
      f"{' ': <{(max_hodnota - delka_occ) / 2 + occ_vyskyt}}{'|NR.'}")

print(oddelovac)

for klic, hodnota in pocitani_delky_slov.items():
    print(f"{klic: >{max_delka_klice + 1}}|{'*' * hodnota: <{max_hodnota + 1}}|{hodnota}")
