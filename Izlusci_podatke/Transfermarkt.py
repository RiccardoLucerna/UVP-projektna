import re
import csv
import requests
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

def razclenitev_vrednosti(cena):
    """Iz niza cifre, kot je '€120.00m' ali '€850k' spremeni v število.
    Vrne število (npr. 120_000_000) ali None, če ni mogoče razčleniti."""
    if not cena:
        return None
    cena = cena.strip()
    # Odstrani simbol evra in presledke
    if cena.startswith("€"):
        cena = cena[1:]
    cena = cena.replace(".", "").replace(",", ".")  # izenači decimalke
    veckratnik = 1
    if cena.lower().endswith("m"):
        veckratnik = 1_000_000
        cena = cena[:-1]
    elif cena.lower().endswith("k"):
        veckratnik = 1_000
        cena = cena[:-1]
    try:
        vrednost = float(cena)
        return int(vrednost * veckratnik)
    except ValueError:
        return None

absolutna_pot = os.path.dirname(os.path.abspath(__file__))

def podatki():
    glavni_url = 'https://www.transfermarkt.com/marktwerte/wertvollstespieler/marktwertetop'
    page = 1
    igralci = {}

    while True:
        url = glavni_url if page == 1 else f"{glavni_url}?page={page}"
        print(f"{page}. stran v teku ...")

        r = requests.get(url, headers=headers)
        vsebina = r.text

        # Pridobivanje HTML datoteke
        pot_html = os.path.join(absolutna_pot, "..", "podatki", f"nogometna_stran_{page}.html")
        with open(pot_html, "w", encoding='utf-8') as dat:
            dat.write(vsebina)
        
        stevilo_pred_stranjo = len(igralci)
    
        # Osnovni vzorec: Pridobiva ime, pozicijo, starost in ostale vrstice za nadaljne regularne izraze
        vzorec = re.compile(
            r'<tr[^>]*?>'                                            # začetna vrstica
            r'.*?<td class="hauptlink">.*?'
            r'<a[^>]*?title="([^"]+)"[^>]*?>.*?</a>.*?</td>'         # group1: ime
            r'.*?<td[^>]*?>\s*([^<\n\r]+?)\s*</td>'                  # group2: pozicija
            r'.*?<td class="zentriert">\s*(\d{1,2})\s*</td>'         # group3: starost
            r'(.*?)</tr>',                                           # group4: preostalo
            re.DOTALL | re.MULTILINE
        )

        # Državljanstva
        drzava_2_re = re.compile(
            r'<img[^>]+title="([^"]+)"[^>]*?><br\s*/?>\s*<img[^>]+title="([^"]+)"',
            re.DOTALL
        )
        drzava_1_re = re.compile(
            r'<td class="zentriert">\s*<img[^>]+title="([^"]+)"',
            re.DOTALL
        )

        # Klub
        klub_re = re.compile(
            r'<td class="zentriert">\s*<a\s+title="([^"]+)"\s+href="[^"]*">\s*<img[^>]*?\/>\s*</a>\s*</td>',
            re.DOTALL
        )

        # Cena (market value)
        cena_re = re.compile(
            r'<td class="rechts hauptlink">\s*<a[^>]*?>([^<]+)</a>&nbsp;',
            re.DOTALL
        )

        for match in vzorec.finditer(vsebina):
            ime = match.group(1).strip()
            pozicija = match.group(2).strip()
            starost = match.group(3).strip()
            neobdelani_podatki = match.group(4)

            # Državljanstva
            drzava_1, drzava_2 = None, None
            dvojna = drzava_2_re.search(neobdelani_podatki)
            if dvojna:
                drzava_1 = dvojna.group(1).strip()
                drzava_2 = dvojna.group(2).strip()
            else:
                ena = drzava_1_re.search(neobdelani_podatki)
                if ena:
                    drzava_1 = ena.group(1).strip()

            # Klub
            klub = None
            klub_m = klub_re.search(neobdelani_podatki)
            if klub_m:
                klub = klub_m.group(1).strip()

            # Cena (neobdelana + razčlenjena)
            cena = None
            cena_m = cena_re.search(neobdelani_podatki)
            if cena_m:
                cena = cena_m.group(1).strip()
            stevilna_cena = razclenitev_vrednosti(cena) if cena else None

            # Zapolnimmo slovar podatkov
            if ime:
                igralci[ime] = {
                "pozicija": pozicija,
                "starost": starost,
                "drzava_1": drzava_1,
                "drzava_2": drzava_2,
                "klub": klub,
                "cena": cena,
                "stevilna_cena_eur": stevilna_cena
                }

        if len(igralci) == stevilo_pred_stranjo:
            print("Nobenih novih igralcev, končujem")
            break

        page += 1

    print(igralci)

    # Pridobivanje HTML datoteke
    pot_csv = os.path.join(absolutna_pot, "..", "podatki", "nogometasi.csv")
    with open(pot_csv, "w", newline='', encoding='utf-8') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow([
            "ime",
            "pozicija",
            "starost",
            "drzava_1",
            "drzava_2",
            "klub",
            "cena",
            "stevilna_cena_eur"
        ])
        for ime, info in igralci.items():
            pisatelj.writerow([
                ime,
                info["pozicija"],
                info["starost"],
                info["drzava_1"],
                info["drzava_2"],
                info["klub"],
                info["cena"],
                info["stevilna_cena_eur"]
            ])
    return igralci