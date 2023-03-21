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

print('Informacije o artiklu: ',
      '\n\tNaslov: '.expandtabs(8), prodaja['Artikl']['Naslov'],
      '\n\tOpis: '.expandtabs(8), prodaja['Artikl']['Opis'],
      '\n\tCijena: '.expandtabs(8), prodaja['Artikl']['Cijena'],
      '\nDatum isteka prodaje: ',
      '\n\tDan: '.expandtabs(8), prodaja['Datum'].day,
      '\n\tMjesec: '.expandtabs(8), prodaja['Datum'].month,
      '\n\tGodina: '.expandtabs(8), prodaja['Datum'].year,
      '\nInformacije o korisniku: ',
      '\n\t'.expandtabs(7), prodaja['Korisnik']['Ime_korisnika'], prodaja['Korisnik']['Prezime_korisnika'],
      '\n\tTelefon: '.expandtabs(8), prodaja['Korisnik']['Telefon'],
      '\n\tEmail: '.expandtabs(8), prodaja['Korisnik']['Email'])


