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

def spela():
    """
    Huvudfunktion som styr spelet.
    """
    ordet = slumpa_ord()
    golvat_ord = skapa_golvat_ord(ordet)
    antal_forsok = 7
    gissade_bokstaver = []

    # Spelloop
    while antal_forsok > 0 and "_" in golvat_ord:
        skriv_status(golvat_ord, antal_forsok)
        bokstav = las_in_bokstav()

        if bokstav in gissade_bokstaver:
            print("Den bokstaven har du redan gissat!")
            continue

        gissade_bokstaver.append(bokstav)

        if uppdatera_gissning(ordet, golvat_ord, bokstav):
            print("Rätt gissat!")
        else:
            print("Fel gissning!")
            antal_forsok -= 1

    # Spelresultat
    if "_" not in golvat_ord:
        print(f"\nGrattis! Du gissade rätt ord: {ordet}")
    else:
        print(f"\nTyvärr, du förlorade! Ordet var: {ordet}")


# Starta spelet
if __name__ == "__main__":
    spela()