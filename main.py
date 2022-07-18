import GramaticaChomsky as gramatica

########## Explicatii extra ###############
#
# Inputul are prima linie numele neterminalului de start.
# Pe urmatoarele linii, pana la intalnirea unui rand gol,
# se dau DOAR PRODUCTIILE COMPUSE DIN NETERMNALI, de forma stanga*dreapta, * necesar pentru a separa neterminalii
# care pot avea mai multe caractere.
# Dupa linia goala, se citesc productiile care duc in terminali.
# Presupunem ca inputul este dat in forma Chomsky mereu si nu se fac filtre extra de verificare.
#
# Am incarcat 2 poze luate din seminar pentru a exemplifica algoritmul
#
############################################

with open("chomsky.in") as f:
    gr = gramatica.GramaticaChomsky()
    gr.seteazaNeterminalStart(f.readline().strip())

    linie = f.readline().strip()
    while linie != "":
        neterminal, productii = linie.split("->")
        neterminal = neterminal.strip()
        productii = productii.split("|")
        for productie in productii:
            productie = productie.strip()
            stanga, dreapta = productie.split("*")
            gr.adaugaProductieNeterminal(neterminal, stanga, dreapta)
        linie = f.readline().strip()

    for linie in f:
        neterminal, productii = linie.strip().split("->")
        neterminal = neterminal.strip()
        productii = productii.split("|")
        for productie in productii:
            productie = productie.strip()
            gr.adaugaProductieTerminal(neterminal, productie)

    print("Gramatica: ")
    print("Neterminal Start:", gr.startSymbol)
    gr.afiseazaGramatica()
    print()

    if gr.verificaCuvantCYK("baabca"):
        print("Cuvantul este generat de gramatica.")
    else:
        print("Cuvantul nu este generat de gramatica.")

    gr.graficCuvantCYK("baabca")
