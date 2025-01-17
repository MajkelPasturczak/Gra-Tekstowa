import random

class Ciezarowka:
    def __init__(self, nazwa, paliwo=100, pieniadze=500, lokalizacja=0):
        self.nazwa = nazwa
        self.paliwo = paliwo
        self.pieniadze = pieniadze
        self.lokalizacja = lokalizacja

    def pokaz_status(self, miasta):
        print("\n--- Status Twojej ciężarówki ---")
        print(f"Nazwa: {self.nazwa}")
        print(f"Paliwo: {self.paliwo} l")
        print(f"Pieniądze: ${self.pieniadze}")
        print(f"Lokalizacja: {miasta[self.lokalizacja]}\n")

def losowa_awaria():
    return random.randint(1, 100) <= 10  # 10% szansa na awarię

def zle_warunki_pogodowe():
    return random.randint(1, 100) <= 20  # 20% szansa na złe warunki pogodowe

def oblicz_trase(ciezarowka, miasta, odleglosci):
    lokalizacja = ciezarowka.lokalizacja
    if lokalizacja >= len(miasta) - 1:
        return 0, 0  # Gra zakończona

    odleglosc = odleglosci[lokalizacja]
    koszt_paliwa = odleglosc * 0.1  # Załóżmy zużycie paliwa: 10 l na 100 km
    if zle_warunki_pogodowe():
        print("Złe warunki pogodowe! Zużycie paliwa wzrasta.")
        koszt_paliwa *= 1.5
    print(f"Trasa: {odleglosc} km, Zużycie paliwa: {koszt_paliwa:.1f} l.")
    return odleglosc, koszt_paliwa

def wyrusz_w_trase(ciezarowka, odleglosc, koszt_paliwa, miasta):
    if ciezarowka.paliwo < koszt_paliwa:
        print("Nie masz wystarczająco paliwa, aby wyruszyć w trasę! Zatankuj.")
        return False

    print(f"Wyruszasz w trasę do {miasta_docelowe(ciezarowka.lokalizacja + 1, miasta)}.")

    if losowa_awaria():
        print("Twoja ciężarówka uległa awarii! Straciłeś $200 na naprawę.")
        ciezarowka.pieniadze -= 200
        return False

    ciezarowka.paliwo -= koszt_paliwa
    ciezarowka.lokalizacja += 1
    zarobek = odleglosc * 1  # $1 za kilometr
    ciezarowka.pieniadze += zarobek
    print(f"Dotarłeś do {miasta_docelowe(ciezarowka.lokalizacja, miasta)} i zarobiłeś ${zarobek:.2f}!")

    if ciezarowka.lokalizacja >= len(miasta) - 1:
        print("\n--- Gratulacje! ---")
        print("Dotarłeś do ostatniego miasta i wygrałeś grę!")
        return True
    return False

def zatankuj(ciezarowka):
    cena_paliwa = 5  # Cena za litr paliwa (przykład)
    max_paliwo = 100 - ciezarowka.paliwo

    print(f"Stacja benzynowa. Cena paliwa: ${cena_paliwa} za litr.")
    litry = int(input(f"Ile litrów chcesz zatankować? (maksymalnie {max_paliwo}): "))

    if litry > max_paliwo:
        litry = max_paliwo

    koszt = litry * cena_paliwa

    if ciezarowka.pieniadze >= koszt:
        ciezarowka.paliwo += litry
        ciezarowka.pieniadze -= koszt
        print(f"Zatankowałeś {litry} litrów paliwa za ${koszt}.")
    else:
        print("Nie masz wystarczająco pieniędzy, aby zatankować tyle paliwa.")

def zapytaj_tak_nie(pytanie):
    while True:
        odpowiedz = input(f"{pytanie} (tak/nie): ").strip().lower()
        if odpowiedz in ["tak", "nie"]:
            return odpowiedz == "tak"
        print("Nieprawidłowa odpowiedź. Wpisz 'tak' lub 'nie'.")

def miasta_docelowe(lokalizacja, miasta):
    if lokalizacja < len(miasta):
        return miasta[lokalizacja]
    return "nieznane miejsce"

def main():
    miasta = [
        "Gdańsk, Polska", "Berlin, Niemcy", "Amsterdam, Holandia", 
        "Bruksela, Belgia", "Paryż, Francja", "Londyn, Wielka Brytania", 
        "Luksemburg, Luksemburg", "Zurych, Szwajcaria", "Monachium, Niemcy", 
        "Wiedeń, Austria", "Praga, Czechy", "Budapeszt, Węgry", 
        "Bratysława, Słowacja", "Zagrzeb, Chorwacja", "Lublana, Słowenia", 
        "Wenecja, Włochy", "Rzym, Włochy", "Florencja, Włochy", 
        "Marsylia, Francja", "Barcelona, Hiszpania", "Madryt, Hiszpania", 
        "Lizbona, Portugalia", "Sewilla, Hiszpania", "Nicea, Francja", 
        "Mediolan, Włochy"
    ]

    odleglosci = [
        577, 654, 211, 320, 465, 344, 270, 612, 313, 293, 
        185, 201, 60, 369, 136, 157, 283, 275, 506, 621, 
        636, 531, 222, 348
    ]

    print("--- Gra: Kierowca Ciężarówki ---")
    print("Witaj, kierowco! Twoim zadaniem jest dostarczać ładunki i zarządzać zasobami.")
    
    nazwa_ciezarowki = input("Nadaj nazwę swojej ciężarówce: ")
    ciezarowka = Ciezarowka(nazwa_ciezarowki)
    print(f"Twoja ciężarówka została nazwana: {ciezarowka.nazwa}!")

    gra_trwa = True
    while gra_trwa:
        ciezarowka.pokaz_status(miasta)

        print("Obliczanie długości trasy i zużycia paliwa...")
        odleglosc, koszt_paliwa = oblicz_trase(ciezarowka, miasta, odleglosci)

        if ciezarowka.lokalizacja >= len(miasta) - 1:
            gra_trwa = False
            continue

        print("\nCo chcesz zrobić?")
        print("1. Wyrusz w trasę")
        print("2. Zatankuj")
        print("3. Zakończ grę")
        wybor = input("Twój wybór: ")

        if wybor == "1":
            wyjazd = zapytaj_tak_nie("Czy na pewno chcesz wyruszyć w trasę?")
            if wyjazd:
                if wyrusz_w_trase(ciezarowka, odleglosc, koszt_paliwa, miasta):
                    gra_trwa = False  # Zwycięstwo
        elif wybor == "2":
            zatankuj(ciezarowka)
        elif wybor == "3":
            gra_trwa = not zapytaj_tak_nie("Czy na pewno chcesz zakończyć grę?")
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

        if ciezarowka.pieniadze < 0:
            print("Zbankrutowałeś! Gra kończy się.")
            gra_trwa = False

if __name__ == "__main__":
    main()