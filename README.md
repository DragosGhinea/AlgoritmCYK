# Algoritm CYK | Implementare

In **GramaticaChomsky.py** am implementat clasa cu acelasi nume utilizata pentru a memora gramatica pe care se va aplica algoritmul. Aceasta are urmatoarele metode:

- seteazaNeterminalStart(neterminal)
- adaugaProductieTerminal(neterminal, terminal)
- adaugaProductieNeterminal(neterminalSursa, neterminalStanga, neterminalDreapta)
- stergeProductieTerminal(neterminal, terminal)
- stergeProductieNeterminal(neterminalSursa, neterminalStanga, neterminalDreapta)
- stergeNeterminal(neterminal)
- stergeTerminal(terminal)
- neterminaliGenereazaTerminal(terminal)
- neterminaliGenereazaNeterminal(neterminalStanga, neterminalDreapta)
- listaNeterminaliGenereazaNeterminali(productii)
- produsCartezian(set1, set2)
- graficCuvantCYK(cuvant)
- verificaCuvantCYK(cuvant)
- afiseazaGramatica()

## Generalitati

Dupa cum stim, algoritmul se aplica pe o gramatica chomsky. Presupunem mereu ca input-ul este o gramatica chomsky.
Pe exemplele date presupunem ca neterminalele sunt reprezentate doar de litere mari ale alfabetului in timp ce terminalele sunt reprezentate doar de litere mici ale alfabetului.
Algoritmul permite totusi orice fel de nume pentru terminale/neterminale, format din oricate caractere. Neterminalele fiind separate prin * la nivel de input tocmai din acest motiv.

## Metode

### » seteazaNeterminalStart(neterminal)
Dupa adaugarea unor terminale si a unor neterminale trebuie ales un neterminal din care algoritmul sa poata incepe.

### » adaugaProductieTerminal(neterminal, terminal)
Adauga o productie dintr-un neterminal intr-un terminal. Observam ca productia merge in un terminal si doar unul datorita structurii chomsky.

### » adaugaProductieNeterminal(neterminalSursa, neterminalStanga, neterminalDreapta)
Adauga o productie dintr-un neterminal in doua neterminale. Observam, la fel ca in cazul anterior, ca productia merge in doua neterminale datorita structurii chomsky.

### » stergeProductieTerminal(neterminal, terminal)
Sterge o productie cu destinatia intr-un terminal.

### » stergeProductieNeterminal(neterminalSursa, neterminalStanga, neterminalDreapta)
Sterge o productie cu destinatia in doua neterminale.

### » stergeNeterminal(neterminal)
Sterge un neterminal si productiile asociate acesteia.

### » stergeTerminal(terminal)
Sterge un terminal si productiile asociate acesteia.

### » neterminaliGenereazaTerminal(terminal)
Obtine multimea tuturor neterminalelor care au productii directe in terminal.

### » neterminaliGenereazaNeterminal(neterminalStanga, neterminalDreapta)
Obtine multimea tuturor neterminalelor care au productii directe in doua neterminale.

### » listaNeterminaliGenereazaNeterminali(productii)
La fel ca metoda anterioara, doar ca obtine multimea pentru mai multe productii de cate doua neterminale.

### » produsCartezian(set1, set2)
Produsul cartezian intre doua multimi.

### » graficCuvantCYK(cuvant)
Folosind libraria **pandas** se genereaza graficul specific algoritmului CYK pentru un cuvant dat.

### » verificaCuvantCYK(cuvant)
Folosind algoritmul CYK verifica daca un cuvant apartine gramaticii.

### » afiseazaGramatica()
Afiseaza gramatica pe care o retine.

# Algoritm CYK | Exemplu Input
In **chomsky.in** avem urmatorul input:
```python
S #neterminal start
S -> B*A #productie doua neterminale
A -> B*A | C*A #productii separate prin |
B -> A*A | A*B #...
C -> B*C | B*B #...

A -> a #productie terminal
B -> b #...
C -> c #...
```

Gramatica din input-ul anterior si un cuvant de test cu tabelul CYK asociat cuvantului:

[Gramatica](https://github.com/DragosGhinea/AlgoritmCYK/blob/main/poza1.png)

[Gramatica2](https://github.com/DragosGhinea/AlgoritmCYK/blob/main/poza2.png)