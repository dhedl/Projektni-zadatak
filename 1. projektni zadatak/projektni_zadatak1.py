from datetime import date

korisnik = {}

korisnik['Ime_korisnika'] = input('Unesite ime korisnika: ').capitalize()
korisnik['Prezime_korisnika'] = input('Unesite prezime korisnika: ').capitalize()
korisnik['Telefon'] = int(input('Unesite telefon korisnika: '))
korisnik['Email'] = input('Unesite email korisnika: ').strip()

artikl = {}

artikl['Naslov'] = input('Unesite naslov artikla: ')
artikl['Opis'] = input('Unesite opis artikla: ')
artikl['Cijena'] = float(input('Unesite cijenu artikla: '))

prodaja = {}

dan = int(input('Unesite dan isteka prodaje: '))
mjesec = int(input('Unesite mjesec isteka prodaje: '))
godina = int(input('Unesite godinu isteka prodaje: '))
prodaja['Datum'] = date(godina, mjesec, dan)
prodaja['Artikl'] = artikl
prodaja['Korisnik'] = korisnik

print(f"Informacije o artiklu: "
      f"\n\tNaslov: {prodaja['Artikl']['Naslov']}".expandtabs(8),
      f"\n\tOpis: {prodaja['Artikl']['Opis']}".expandtabs(8),
      f"\n\tCijena: {prodaja['Artikl']['Cijena']}".expandtabs(8),
      f"\nDatum isteka prodaje: "
      f"\n\tDan: {prodaja['Datum'].day}".expandtabs(8),
      f"\n\tMjesec: {prodaja['Datum'].month}".expandtabs(8),
      f"\n\tGodina: {prodaja['Datum'].year}".expandtabs(8),
      f"\nInformacije o korisniku: "
      f"\n\t{prodaja['Korisnik']['Ime_korisnika']} {prodaja['Korisnik']['Prezime_korisnika']}".expandtabs(8),
      f"\n\tTelefon: {prodaja['Korisnik']['Telefon']}".expandtabs(8),
      f"\n\tEmail: {prodaja['Korisnik']['Email']}".expandtabs(8))