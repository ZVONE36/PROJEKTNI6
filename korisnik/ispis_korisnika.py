def get_korisnik(redni_broj, korisnik):
    return f"{redni_broj}. {korisnik.telefon} {korisnik.email}"

def ispis_svih_korisnika(korisnici):
    for korisnik in korisnici:
        korisnik.ispis()