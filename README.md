# Analiza podatkov o vrednosti najboljših nogometašev

## Projektna naloga pri predmetu UVP
Avtor: Riccardo Lucerna <br>
Datum: 25/08/2025

Pri tem projektu se je zajelo in obdelalo podatke o najbolj vrednih nogometašev po spletni strani *Transfermarkt*. Cilj je analizirati igralce po pozicijah, starosti, klubu, itn.

## Viri
Za analizo so bili podatki pobrani iz spletne strani:
* https://www.transfermarkt.com/marktwerte/wertvollstespieler/marktwertetop

## Knjižnice
Knjižnice, ki so bile uporabljene pri projektu in jih uporabnik potrebuje za zagon programa:
* <kbd>re</kbd> (za uporabo regularnih izrazov);
* <kbd>csv</kbd> (za ustvarjanje csv datotek);
* <kbd>request</kbd> (za zajem podatkov);
* <kbd>html</kbd> (za pomoč pri branju znakov kot so <kbd>&</kbd>);
* <kbd>os</kbd> (za pot do datotek).

Knjižnice, ki so bile uporabljene pri projektu in jih uporabnik potrebuje za analizo podatkov:
* <kbd>pandas</kbd> (za analizo podatkov);
* <kbd>matplotlib.pyplot</kbd> (za risanje grafov);
* <kbd>matplotlib.ticker</kbd> (za boljšo prikazo številk na oseh);
* <kbd>IPython.display</kbd> (za prikaz tabel in grafov hkrati).

## Struktura projekta
UVP-projektna/
├── izlusci_podatke/
│ ├── init.py
│ ├── .gitignore
│ ├── Transfermarkt.py
├── podatki/
| ├── nogometasi.csv
| ├── nogometna_stran_1.html
| ├── nogometna_stran_2.html
| ├── nogometna_stran_3.html
| ├── nogometna_stran_4.html
| ├── nogometna_stran_5.html
| ├── nogometna_stran_6.html
| ├── nogometna_stran_7.html
| ├── nogometna_stran_8.html
| ├── nogometna_stran_9.html
| ├── nogometna_stran_10.html
| ├── nogometna_stran_12.html
| ├── nogometna_stran_13.html
| ├── nogometna_stran_14.html
| ├── nogometna_stran_15.html
| ├── nogometna_stran_16.html
| ├── nogometna_stran_17.html
| ├── nogometna_stran_18.html
| ├── nogometna_stran_19.html
| ├── nogometna_stran_20.html
| ├── nogometna_stran_21.html
| └── nogometna_stran.html
├── .gitignore
├── analiza_podatkov.ipynb
├── main.py
└── README.md

V glavni mapi se nahajata mapi *Izlusci_podatke* in *podatki*. V *Izusci_podatke* se nahaja datoteka *Transfermarkt.py* v kateri sta funkciji *razclenitev_vrednosti()* in *podatki()*. V funkciji *podatki()* smo zajeli podatke iz spleta in ustvarili mapo *podatki* z datotekami *nogometasi.csv* in *nogometna_stran.html* z ostalimi html stranmi. Analizo podatkov bomo naredili prav z uporabo teh datotek. V glavni mapi imamo še tri datoteke. Ena izmed teh je prav *README.md* v kateri se tudi nahajo navodilo za zagon programa. Program, ki se požene s pomočjo druge datoteke *main.py*. Tretja pa je *analiza_podatkov.ipynb*, kjer smo s pomočjo Jupyter Notebooka analizirali podatke.

## Začetek
Uporabnik naj požene *main.py*, ki bo ustvaril vse potrebne datoteke, ki se bojo shranile v mapi *podatki*. Na koncu odpremo *analiza_podatkov.ipynb* in izvedemo analizo.