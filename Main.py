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