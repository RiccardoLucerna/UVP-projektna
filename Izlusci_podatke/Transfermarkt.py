import re
import csv
import requests
import os
from unidecode import unidecode

#nogometasi_frontpage_url ='https://www.transfermarkt.com/marktwerte/wertvollstespieler/marktwertetop'
#nogometni_directory = 'nogometni_podatki_'
#frontpage_filename = 'transfermarkt.html'
#csv_filename = 'nogometasi.csv'
#
#def download_url_to_string(url):
#    """Funkcija kot argument sprejme niz in poskusi vrniti vsebino te spletne
#    strani kot niz. V primeru, da med izvajanje pride do napake vrne None.
#    """
#    try:
#        # del kode, ki morda sproži napako
#        headers = {"User-agent": "Chrome/136.0.7103.114"}
#        response = requests.get(url, headers=headers)
#        if response.status_code != 200:
#            print("Prišlo je do napake pri zajemu podatkov")
#            return None
#        page_content = response.text
#    except requests.exceptions.RequestException:
#        # koda, ki se izvede pri napaki
#        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
#        print("Prišlo je do napake")
#        return None
#    # nadaljujemo s kodo če ni prišlo do napake
#    return page_content
#
#def save_string_to_file(text, directory, filename):
#    """Funkcija zapiše vrednost parametra "text" v novo ustvarjeno datoteko
#    locirano v "directory"/"filename", ali povozi obstoječo. V primeru, da je
#    niz "directory" prazen datoteko ustvari v trenutni mapi.
#    """
#    os.makedirs(directory, exist_ok=True)
#    path = os.path.join(directory, filename)
#    with open(path, 'w', encoding='utf-8') as file_out:
#        file_out.write(text)
#
#def save_frontpage(page, directory, filename):
#    """Funkcija shrani vsebino spletne strani na naslovu "page" v datoteko
#    "directory"/"filename"."""
#    text = download_url_to_string(page)
#    text = read_file_to_string(directory, "stran.html")
#    save_string_to_file(text, directory, filename)
#    return text
#
#def read_file_to_string(directory, filename):
#    """Funkcija vrne celotno vsebino datoteke "directory"/"filename" kot niz."""
#    os.makedirs(directory, exist_ok=True)
#    path = os.path.join(directory, filename)
#    with open(path, 'r', encoding='utf-8') as file_in:
#        text = file_in.read()
#    return text    
#
#def page_to_player(page_content):
#    """Funkcija poišče posamezne igralce, ki se nahajajo v spletni strani in
#    vrne seznam igralcev."""
#    return re.findall(r'<td class="hauptlink">.*?<td class="rechts hauptlink"><a href=".*">.*</a>&nbsp;</td></tr>', page_content, flags=re.DOTALL)
#
#def get_dict_from_player_block(block):
#    """Funkcija iz niza za posamezen oglasni blok izlušči podatke o imenu, poziciji
#    in opisu ter vrne slovar, ki vsebuje ustrezne podatke."""
#    ime = re.search(r'/<td class="hauptlink"><a title="([a-zA-Zéáí]* [a-zA-Zéáí]*)"|<td class="hauptlink"><a title="([a-zA-Zéáí]*)"|<td class="hauptlink"><a title="([a-zA-Zéáí]* [a-zA-Zéáí]* [a-zA-Zéáí]*)"/gm', block)
#    pozicija = re.search(r'/<td class="hauptlink"><a title=".*" href=".*">.*<\/a><\/td><\/tr><tr><td>(.*)<\/td><\/tr><\/table><\/td>/gm', block)
#    starost = re.search(r'/<td class="zentriert">(\d*)<\/td><td class="zentriert">/gm', block)
#    drzava_1 = re.search(r'/<\/td><td class="zentriert"><img src=".{6,100}" title="(.{2, 25})" alt=".*" class="flaggenrahmen"/gm', block)
#    drzava_2 = re.search(r'/<img src=".*" title=".*" alt=".*" class="flaggenrahmen" \/><br \/><img src=".*" title="(.*)" alt=".*" class="flaggenrahmen" \/>/gm', block)
#    klub = re.search(r'/<td class="zentriert"><a title="(.*)" href=".*"><img src=".*" title=".*" alt=".*" class="" \/><\/a><\/td>/gm', block)
#    cena = re.search(r'/<td class="rechts hauptlink"><a href=".*">(.*)<\/a>&nbsp;<\/td><\/tr>/gm', block)
#    if ime == None or pozicija == None or starost == None or drzava_1 == None or drzava_2 == None or klub == None or cena == None:
#        return None
#    return {
#        'ime': ime.group(1),
#        'pozicija': pozicija.group(1),
#        'starost': starost.group(1),
#        'drzava_1': drzava_1.group(1),
#        'drzava_2': drzava_2.group(1),
#        'klub': klub.group(1),
#        'cena': cena.group(1)
#    }
#
#def players_from_file(filename, directory):
#    """Funkcija prebere podatke v datoteki "directory"/"filename" in jih
#    pretvori (razčleni) v pripadajoč seznam slovarjev za vsak nogometaš posebej."""
#    page_content = read_file_to_string(directory, filename)
#    blocks = page_to_player(page_content)
#    players = [get_dict_from_player_block(block) for block in blocks]
#    return [player for player in players if player != None]
#
#def write_csv(fieldnames, rows, directory, filename):
#    """
#    Funkcija v csv datoteko podano s parametroma "directory"/"filename" zapiše
#    vrednosti v parametru "rows" pripadajoče ključem podanim v "fieldnames"
#    """
#    os.makedirs(directory, exist_ok=True)
#    path = os.path.join(directory, filename)
#    with open(path, 'w', encoding='utf-8', newline='') as csv_file:
#        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#        writer.writeheader()
#        for row in rows:
#            writer.writerow(row)
#    return
#
#def write_players_to_csv(players, directory, filename):
#    """Funkcija vse podatke iz parametra "players" zapiše v csv datoteko podano s
#    parametroma "directory"/"filename". Funkcija predpostavi, da so ključi vseh
#    slovarjev parametra players enaki in je seznam players neprazen."""
#    # Stavek assert preveri da zahteva velja
#    # Če drži se program normalno izvaja, drugače pa sproži napako
#    # Prednost je v tem, da ga lahko pod določenimi pogoji izklopimo v
#    # produkcijskem okolju
#    assert players and (all(j.keys() == players[0].keys() for j in players))
#    fieldnames = list(players[0].keys())
#    write_csv(fieldnames, players, directory, filename)
#
#def main(redownload=True, reparse=True):
#    """Funkcija izvede celoten del pridobivanja podatkov:
#    1. Igralce prenese iz transfermarkta
#    2. Lokalno html datoteko pretvori v lepšo predstavitev podatkov
#    3. Podatke shrani v csv datoteko
#    """
#    # Najprej v lokalno datoteko shranimo glavno stran
#    if redownload:
#        save_frontpage(nogometasi_frontpage_url, nogometni_directory, frontpage_filename)
#
#    # Iz lokalne (html) datoteke preberemo podatke
#    # Podatke preberemo v lepšo obliko (seznam slovarjev)
#    # Podatke shranimo v csv datoteko
#    if reparse:
#        players = players_from_file(frontpage_filename, nogometni_directory)
#        write_players_to_csv(players, nogometni_directory, csv_filename)
#
#    # Dodatno: S pomočjo parametrov funkcije main omogoči nadzor, ali se
#    # celotna spletna stran ob vsakem zagon prenese (četudi že obstaja)
#    # in enako za pretvorbo
#
#if __name__ == '__main__':
#    main()

absolutna_pot = os.path.dirname(os.path.abspath(__file__))

def podatki_o_pozicijah():
    url = 'https://www.transfermarkt.com/marktwerte/wertvollstespieler/marktwertetop'
    r = requests.get(url)
    vsebina = r.text

    pot = os.path.join(absolutna_pot, "..", "podatki", "nogometna_stran.html")
    with open(pot, "w") as dat:
        dat.write(vsebina)
    
    vzorec = re.compile(
        r'/<td class="hauptlink"><a title="([a-zA-Zéáí]* [a-zA-Zéáí]*)"|<td class="hauptlink"><a title="([a-zA-Zéáí]*)"|<td class="hauptlink"><a title="([a-zA-Zéáí]* [a-zA-Zéáí]* [a-zA-Zéáí]*)"/gm'
        r'/<td class="hauptlink"><a title=".*" href=".*">.*<\/a><\/td><\/tr><tr><td>(.*)<\/td><\/tr><\/table><\/td>/gm'
    #    r'/<td class="zentriert">(\d*)<\/td><td class="zentriert">/gm'
    #    r'/<\/td><td class="zentriert"><img src=".{6,100}" title="(.{2, 25})" alt=".*" class="flaggenrahmen"/gm'
    #    r'/<img src=".*" title=".*" alt=".*" class="flaggenrahmen" \/><br \/><img src=".*" title="(.*)" alt=".*" class="flaggenrahmen" \/>/gm'
    #    r'/<td class="zentriert"><a title="(.*)" href=".*"><img src=".*" title=".*" alt=".*" class="" \/><\/a><\/td>/gm'
    #    r'/<td class="rechts hauptlink"><a href=".*">(.*)<\/a>&nbsp;<\/td><\/tr>/gm'
    )

    igralci_po_pozicijah = {}
    for match in vzorec.finditer(vsebina):
        ime = match.groups(1)
        pozicija = match.groups(2)
        #starost = int(match.group(3))
        #drzava_1 = match.group(4)
        #drzava_2 = match.group(5)
        #klub = match.group(6)
        #cena = int(match.group(7))
        igralci_po_pozicijah[ime] = pozicija

    pot = os.path.join(absolutna_pot, "..", "podatki", "nogometasi_po_pozicijah.csv")
    with open(pot, "w", newline='') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["ime", "pozicija"])
        for ime, pozicija in igralci_po_pozicijah.items():
            pisatelj.writerow([ime, pozicija])
    return igralci_po_pozicijah

def podatki_o_starosti():
    url = 'https://www.transfermarkt.com/marktwerte/wertvollstespieler/marktwertetop'
    r = requests.get(url)
    vsebina = r.text

    pot = os.path.join(absolutna_pot, "..", "podatki", "nogometna_stran.html")
    with open(pot, "w") as dat:
        dat.write(vsebina)
    
    vzorec = re.compile(
        r'/<td class="hauptlink"><a title="([a-zA-Zéáí]* [a-zA-Zéáí]*)"|<td class="hauptlink"><a title="([a-zA-Zéáí]*)"|<td class="hauptlink"><a title="([a-zA-Zéáí]* [a-zA-Zéáí]* [a-zA-Zéáí]*)"/gm'
    #    r'/<td class="hauptlink"><a title=".*" href=".*">.*<\/a><\/td><\/tr><tr><td>(.*)<\/td><\/tr><\/table><\/td>/gm'
        r'/<td class="zentriert">(\d*)<\/td><td class="zentriert">/gm'
    #    r'/<\/td><td class="zentriert"><img src=".{6,100}" title="(.{2, 25})" alt=".*" class="flaggenrahmen"/gm'
    #    r'/<img src=".*" title=".*" alt=".*" class="flaggenrahmen" \/><br \/><img src=".*" title="(.*)" alt=".*" class="flaggenrahmen" \/>/gm'
    #    r'/<td class="zentriert"><a title="(.*)" href=".*"><img src=".*" title=".*" alt=".*" class="" \/><\/a><\/td>/gm'
    #    r'/<td class="rechts hauptlink"><a href=".*">(.*)<\/a>&nbsp;<\/td><\/tr>/gm'
    )

    igralci_po_starosti = {}
    for match in vzorec.finditer(vsebina):
        ime = match.groups(1)
        #pozicija = match.groups(2)
        starost = int(match.group(3))
        #drzava_1 = match.group(4)
        #drzava_2 = match.group(5)
        #klub = match.group(6)
        #cena = int(match.group(7))
        igralci_po_starosti[ime] = starost

    pot = os.path.join(absolutna_pot, "..", "podatki", "nogometasi_po_starosti.csv")
    with open(pot, "w", newline='') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["ime", "starost"])
        for ime, starost in igralci_po_starosti.items():
            pisatelj.writerow([ime, starost])
    return igralci_po_starosti

def podatki_o_drzavljastvu():
    url = 'https://www.transfermarkt.com/marktwerte/wertvollstespieler/marktwertetop'
    r = requests.get(url)
    vsebina = r.text

    pot = os.path.join(absolutna_pot, "..", "podatki", "nogometna_stran.html")
    with open(pot, "w") as dat:
        dat.write(vsebina)
    
    vzorec = re.compile(
        r'/<td class="hauptlink"><a title="([a-zA-Zéáí]* [a-zA-Zéáí]*)"|<td class="hauptlink"><a title="([a-zA-Zéáí]*)"|<td class="hauptlink"><a title="([a-zA-Zéáí]* [a-zA-Zéáí]* [a-zA-Zéáí]*)"/gm'
    #    r'/<td class="hauptlink"><a title=".*" href=".*">.*<\/a><\/td><\/tr><tr><td>(.*)<\/td><\/tr><\/table><\/td>/gm'
    #    r'/<td class="zentriert">(\d*)<\/td><td class="zentriert">/gm'
        r'/<\/td><td class="zentriert"><img src=".{6,100}" title="(.{2, 25})" alt=".*" class="flaggenrahmen"/gm'
    #    r'/<img src=".*" title=".*" alt=".*" class="flaggenrahmen" \/><br \/><img src=".*" title="(.*)" alt=".*" class="flaggenrahmen" \/>/gm'
    #    r'/<td class="zentriert"><a title="(.*)" href=".*"><img src=".*" title=".*" alt=".*" class="" \/><\/a><\/td>/gm'
    #    r'/<td class="rechts hauptlink"><a href=".*">(.*)<\/a>&nbsp;<\/td><\/tr>/gm'
    )

    igralci_po_drzavljanstvu = {}
    for match in vzorec.finditer(vsebina):
        ime = match.groups(1)
        #pozicija = match.groups(2)
        #starost = int(match.group(3))
        drzava_1 = match.group(4)
        #drzava_2 = match.group(5)
        #klub = match.group(6)
        #cena = int(match.group(7))
        igralci_po_drzavljanstvu[ime] = drzava_1

    pot = os.path.join(absolutna_pot, "..", "podatki", "nogometasi_po_drzavljanstvu.csv")
    with open(pot, "w", newline='') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["ime", "drzava_1"])
        for ime, drzava_1 in igralci_po_drzavljanstvu.items():
            pisatelj.writerow([ime, drzava_1])
    return igralci_po_drzavljanstvu

def podatki_o_drzavljastvu_2():
    url = 'https://www.transfermarkt.com/marktwerte/wertvollstespieler/marktwertetop'
    r = requests.get(url)
    vsebina = r.text

    pot = os.path.join(absolutna_pot, "..", "podatki", "nogometna_stran.html")
    with open(pot, "w") as dat:
        dat.write(vsebina)
    
    vzorec = re.compile(
        r'/<td class="hauptlink"><a title="([a-zA-Zéáí]* [a-zA-Zéáí]*)"|<td class="hauptlink"><a title="([a-zA-Zéáí]*)"|<td class="hauptlink"><a title="([a-zA-Zéáí]* [a-zA-Zéáí]* [a-zA-Zéáí]*)"/gm'
    #    r'/<td class="hauptlink"><a title=".*" href=".*">.*<\/a><\/td><\/tr><tr><td>(.*)<\/td><\/tr><\/table><\/td>/gm'
    #    r'/<td class="zentriert">(\d*)<\/td><td class="zentriert">/gm'
    #    r'/<\/td><td class="zentriert"><img src=".{6,100}" title="(.{2, 25})" alt=".*" class="flaggenrahmen"/gm'
        r'/<img src=".*" title=".*" alt=".*" class="flaggenrahmen" \/><br \/><img src=".*" title="(.*)" alt=".*" class="flaggenrahmen" \/>/gm'
    #    r'/<td class="zentriert"><a title="(.*)" href=".*"><img src=".*" title=".*" alt=".*" class="" \/><\/a><\/td>/gm'
    #    r'/<td class="rechts hauptlink"><a href=".*">(.*)<\/a>&nbsp;<\/td><\/tr>/gm'
    )

    igralci_po_drzavljanstvu_2 = {}
    for match in vzorec.finditer(vsebina):
        ime = match.groups(1)
        #pozicija = match.groups(2)
        #starost = int(match.group(3))
        #drzava_1 = match.group(4)
        drzava_2 = match.group(5)
        #klub = match.group(6)
        #cena = int(match.group(7))
        igralci_po_drzavljanstvu_2[ime] = drzava_2

    pot = os.path.join(absolutna_pot, "..", "podatki", "nogometasi_po_drzavljanstvu_2.csv")
    with open(pot, "w", newline='') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["ime", "drzava_2"])
        for ime, drzava_2 in igralci_po_drzavljanstvu_2.items():
            pisatelj.writerow([ime, drzava_2])
    return igralci_po_drzavljanstvu_2

def podatki_o_klubu():
    url = 'https://www.transfermarkt.com/marktwerte/wertvollstespieler/marktwertetop'
    r = requests.get(url)
    vsebina = r.text

    pot = os.path.join(absolutna_pot, "..", "podatki", "nogometna_stran.html")
    with open(pot, "w") as dat:
        dat.write(vsebina)
    
    vzorec = re.compile(
        r'/<td class="hauptlink"><a title="([a-zA-Zéáí]* [a-zA-Zéáí]*)"|<td class="hauptlink"><a title="([a-zA-Zéáí]*)"|<td class="hauptlink"><a title="([a-zA-Zéáí]* [a-zA-Zéáí]* [a-zA-Zéáí]*)"/gm'
    #    r'/<td class="hauptlink"><a title=".*" href=".*">.*<\/a><\/td><\/tr><tr><td>(.*)<\/td><\/tr><\/table><\/td>/gm'
    #    r'/<td class="zentriert">(\d*)<\/td><td class="zentriert">/gm'
    #    r'/<\/td><td class="zentriert"><img src=".{6,100}" title="(.{2, 25})" alt=".*" class="flaggenrahmen"/gm'
    #    r'/<img src=".*" title=".*" alt=".*" class="flaggenrahmen" \/><br \/><img src=".*" title="(.*)" alt=".*" class="flaggenrahmen" \/>/gm'
        r'/<td class="zentriert"><a title="(.*)" href=".*"><img src=".*" title=".*" alt=".*" class="" \/><\/a><\/td>/gm'
    #    r'/<td class="rechts hauptlink"><a href=".*">(.*)<\/a>&nbsp;<\/td><\/tr>/gm'
    )

    igralci_po_klubu = {}
    for match in vzorec.finditer(vsebina):
        ime = match.groups(1)
        #pozicija = match.groups(2)
        #starost = int(match.group(3))
        #drzava_1 = match.group(4)
        #drzava_2 = match.group(5)
        klub = match.group(6)
        #cena = int(match.group(7))
        igralci_po_klubu[ime] = klub

    pot = os.path.join(absolutna_pot, "..", "podatki", "nogometasi_po_klubu.csv")
    with open(pot, "w", newline='') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["ime", "klub"])
        for ime, klub in igralci_po_klubu.items():
            pisatelj.writerow([ime, klub])
    return igralci_po_klubu

def podatki_o_ceni():
    url = 'https://www.transfermarkt.com/marktwerte/wertvollstespieler/marktwertetop'
    r = requests.get(url)
    vsebina = r.text

    pot = os.path.join(absolutna_pot, "..", "podatki", "nogometna_stran.html")
    with open(pot, "w") as dat:
        dat.write(vsebina)
    
    vzorec = re.compile(
        r'/<td class="hauptlink"><a title="([a-zA-Zéáí]* [a-zA-Zéáí]*)"|<td class="hauptlink"><a title="([a-zA-Zéáí]*)"|<td class="hauptlink"><a title="([a-zA-Zéáí]* [a-zA-Zéáí]* [a-zA-Zéáí]*)"/gm'
    #    r'/<td class="hauptlink"><a title=".*" href=".*">.*<\/a><\/td><\/tr><tr><td>(.*)<\/td><\/tr><\/table><\/td>/gm'
    #    r'/<td class="zentriert">(\d*)<\/td><td class="zentriert">/gm'
    #    r'/<\/td><td class="zentriert"><img src=".{6,100}" title="(.{2, 25})" alt=".*" class="flaggenrahmen"/gm'
    #    r'/<img src=".*" title=".*" alt=".*" class="flaggenrahmen" \/><br \/><img src=".*" title="(.*)" alt=".*" class="flaggenrahmen" \/>/gm'
    #    r'/<td class="zentriert"><a title="(.*)" href=".*"><img src=".*" title=".*" alt=".*" class="" \/><\/a><\/td>/gm'
        r'/<td class="rechts hauptlink"><a href=".*">(.*)<\/a>&nbsp;<\/td><\/tr>/gm'
    )

    igralci_po_ceni = {}
    for match in vzorec.finditer(vsebina):
        ime = match.groups(1)
        #pozicija = match.groups(2)
        #starost = int(match.group(3))
        #drzava_1 = match.group(4)
        #drzava_2 = match.group(5)
        #klub = match.group(6)
        cena = int(match.group(7))
        igralci_po_ceni[ime] = cena

    pot = os.path.join(absolutna_pot, "..", "podatki", "nogometasi_po_ceni.csv")
    with open(pot, "w", newline='') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["ime", "cena"])
        for ime, cena in igralci_po_ceni.items():
            pisatelj.writerow([ime, cena])
    return igralci_po_ceni