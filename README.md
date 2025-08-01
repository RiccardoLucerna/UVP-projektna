# Analiza podatkov o vrednosti najboljših nogometašev

## Projektna naloga pri predmetu UVP
Avtor: Riccardo Lucerna <br>
Datum: 

## Viri
Za analizo so bili podatki pobrani iz spletne strani:
* https://www.transfermarkt.com/marktwerte/wertvollstespieler/marktwertetop

## Knjižnice
Knjižnice, ki so bile uporabljene pri projektu in jih uporabnik potrebuje za zagon programa:
* re (za uporabo regularnih izrazov)
* csv (za ustvarjanje csv datotek)
* request (za zajem podatkov)
* os (za pot do datotek)

## Struktura
V glavni mapi se nahajata mapi *Izlusci_podatke* in *podatki*. V *Izusci_podatke* se nahaja datoteka *Transfermarkt.py* v kateri sta funkciji *razclenitev_vrednosti()* in *podatki()*. V funkciji *podatki()* smo zajeli podatke iz spleta in ustvarili mapo *podatki* z datotekami *nogometasi.csv* in *nogometna_stran.html*. Analizo podatkov bomo naredili prav z uporabo teh datotek. V glavni mapi imamo še dve datoteki. Ena izmed teh je prav *README.md* v kateri se tudi nahajo navodilo za zagon programa. Program, ki se požene s pomočjo druge datoteke *main.py*

## Začetek
Uporabnik naj požene *main.py*, ki bo ustvaril vse potrebne datoteke, ki se bojo shranile v mapi *podatki*. Na koncu odpremo analiza_podatkov.ipynb in izvedemo analizo.