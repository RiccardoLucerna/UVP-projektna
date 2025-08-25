# Analiza podatkov o vrednosti najboljših nogometašev

## Projektna naloga pri predmetu UVP
Avtor: Riccardo Lucerna <br>
Datum: 25. 8. 2025

Pri tem projektu smo zajeli in obdelali podatke o najbolj vrednih nogometašev po spletni strani *Transfermarkt*. Cilj je analizirati igralce po pozicijah, starosti, klubu, itn.

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
* <kbd>matplotlib.ticker</kbd> (za boljši prikaz številk na oseh);
* <kbd>IPython.display</kbd> (za prikaz tabel in grafov hkrati).

## Struktura projekta

V glavni mapi se nahajata mapi *Izlusci_podatke* in *podatki*. V *Izlusci_podatke* se nahaja datoteka *Transfermarkt.py* v kateri sta funkciji *razclenitev_vrednosti()* in *podatki()*. V funkciji *podatki()* smo zajeli podatke iz spleta in ustvarili mapo *podatki* z datotekami *nogometasi.csv* in *nogometna_stran.html* z ostalimi html stranmi. Analizo podatkov bomo naredili prav z uporabo teh datotek. V glavni mapi imamo še tri datoteke. Ena izmed teh je prav *README.md* v kateri se tudi nahaja navodilo za zagon programa. Program, ki se požene s pomočjo druge datoteke *main.py*. Tretja pa je *analiza_podatkov.ipynb*, kjer smo s pomočjo Jupyter Notebooka analizirali podatke.

## Začetek
Uporabnik naj požene *main.py*, ki bo ustvaril vse potrebne datoteke, ki se bodo shranile v mapi *podatki*. Na koncu odpremo *analiza_podatkov.ipynb* in izvedemo analizo.