import random

ordlista = ["banana", "äpple", "robot", "python", "katt", "dator"]

# Välj ett slumpmässigt ord
hemligt_ord = random.choice(ordlista)
gissade_bokstäver = []
försök_kvar = 6

print("Välkommen till Ordgissning!")
print("Gissa ordet bokstav för bokstav.")

while försök_kvar > 0:
    # Visa ordets nuvarande status
    visat_ord = ""
    for bokstav in hemligt_ord:
        if bokstav in gissade_bokstäver:
            visat_ord += bokstav
        else:
            visat_ord += "_"
    print("\nOrd:", visat_ord)

    # Om spelaren gissat hela ordet
    if "_" not in visat_ord:
        print("Grattis! Du gissade ordet:", hemligt_ord)
        break

    # Spelarens gissning
    gissning = input("Gissa en bokstav: ").lower()

    if len(gissning) != 1 or not gissning.isalpha():
        print("Skriv EN bokstav tack.")
        continue

    if gissning in gissade_bokstäver:
        print("Du har redan gissat den bokstaven.")
        continue

    gissade_bokstäver.append(gissning)

    if gissning in hemligt_ord:
        print("Rätt!")
    else:
        försök_kvar -= 1
        print("Fel! Försök kvar:", försök_kvar)

if försök_kvar == 0:
    print("\nDu förlorade! Ordet var:", hemligt_ord)