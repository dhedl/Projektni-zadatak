from utilities import unos_pozitivnog_cijelog_broja, unos_emaila, unos_teksta
from .Korisnik import Korisnik

def unos_korisnika(redni_broj):
    ime = unos_teksta(f"Unesite ime {redni_broj}. korisnika: ").capitalize()
    prezime = unos_teksta(f"Unesite prezime {redni_broj}. korisnika: ").capitalize()
    email = unos_emaila(f"Unesite email {redni_broj}. korisnika: ").strip()
    telefon = unos_pozitivnog_cijelog_broja(f"Unesite telefon {redni_broj}. korisnika: ")
    return Korisnik(ime, prezime, email, telefon)
