import random as rnd 

def slumpa_ord():
    
    #Returnerar ett slumpmässigt ord från en färdig lista.
    
    ord_lista = ["python", "banan", "skola", "dator", "programmering", "spel", "kod", "utveckling", "testning", "funktion", "variabel", "loop", "villkor", "lista", "sträng", "tal", "matematik", "logik", "algoritm", "data", "fil",  "nätverk", "server", "klient", "applikation", "gränssnitt", "design", "struktur", "prestanda", "säkerhet", "optimering", "debugging", "kompilering", "syntax", "semantik", "bibliotek", "ramverk", "plattform", "version", "kontroll", "repository", "gren", "sammanslagning", "utgåva", "distribution", "installation", "konfiguration", "underhåll", "support", "dokumentation", "exempel", "tutorial", "övning", "projekt", "team", "samarbete", "kommunikation", "ledning", "planering", "mål", "deadline", "kvalitet", "testfall", "bugg", "felhantering", "loggning", "övervakning", "analys", "rapportering", "feedback", "förbättring", "innovation", "teknik", "framtid", "utbildning", "karriär", "jobb", "intervju", "cv", "portfölj", "nätverkande", "evenemang", "konferens", "workshop", "seminarium", "webinar", "blogg", "artikel", "bok", "kurs", "certifiering", "examensarbete", "forskning", "utvecklare", "ingenjör", "designer", "arkitekt", "analytiker", "testare", "projektledare", "produktägare", "agil", "kanban", "sprint", "backlogg", "user", "epic", "task", "buggfix", "release", "deployment", "miljö", "produktion", "staging", "testmiljö", "utvecklingsmiljö", "kodgranskning", "parprogrammering", "devops", "cloud", "virtualisering", "container", "docker", "kubernetes", "mikrotjänster", "serverlös", "api", "rest", "json", "xml", "http", "https", "tcp", "udp", "socket", "firewall", "säkerhetshot", "kryptering", "autentisering", "auktorisering", "oauth", "jwt", "session", "cookie", "cache", "prestandaoptimering", "lastbalansering", "skalbarhet", "felövervakning", "incidenthantering", "disaster recovery", "backup", "återställning", "logghantering", "övervakningsverktyg", "analysverktyg", "testautomatisering", "enhetstest", "integrationstest", "systemtest", "acceptanstest", "regressionstest", "prestandatest", "säkerhetstest", "användbarhetstest", "testning", "funktionell" ]
    return rnd.choice(ord_lista)    

def skapa_ord(ordet):
    
    #Tar in ett ord och skapar en lista med * istället för bokstäver.
    
    return ["*"] * len(ordet)


def skriv_status(ord, antal_forsok):
    
    #Skriver aktuell status av spelet.
    
    print("\nAktuellt ord: ", " ".join(ord))
    print(f"Antal gissningar kvar: {antal_forsok}") 

def las_in_bokstav():
    
    #Läser in en bokstav från användaren.
    #Säker input: fortsätter tills användaren matar en enda bokstav.
    
    while True:
        bokstav = input("Gissa en bokstav: ").lower().strip()
        if len(bokstav) == 1 and bokstav.isalpha():
            return bokstav
        print("Felaktig inmatning! Du måste skriva EN bokstav.")

def uppdatera_gissning(ordet, golvat_ord, bokstav):
    
    #Uppdaterar ordet om bokstaven finns. Returnerar True om bokstaven finns, annars False.
    
    hittad = False
    for i in range(len(ordet)):
        if ordet[i] == bokstav:
            golvat_ord[i] = bokstav
            hittad = True
    return hittad

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