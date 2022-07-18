import pandas

class GramaticaChomsky:
    def __init__(self):
        self.startSymbol = "S"
        self.terminali = set()
        self.neterminali = set()
        self.productiiTerminali = {}
        self.productiiNeterminali = {}

    def seteazaNeterminalStart(self, neterminal):
        self.startSymbol = neterminal

    def adaugaProductieTerminal(self, neterminal, terminal):
        self.neterminali.add(neterminal)
        self.terminali.add(terminal)
        generare = self.productiiTerminali.get(neterminal, [])
        generare += terminal
        self.productiiTerminali[neterminal] = generare

    def adaugaProductieNeterminal(self, neterminalSursa, neterminalStanga, neterminalDreapta):
        self.neterminali.add(neterminalSursa)
        self.neterminali.add(neterminalStanga)
        self.neterminali.add(neterminalDreapta)
        generare = self.productiiNeterminali.get(neterminalSursa, [])
        generare.append((neterminalStanga, neterminalDreapta))
        self.productiiNeterminali[neterminalSursa] = generare

    def stergeProductieTerminal(self, neterminal, terminal):
        self.productiiTerminali.get(neterminal).remove(terminal)
        if len(self.productiiTerminali.get(neterminal)) == 0:
            self.productiiTerminali.pop(neterminal)

    def stergeProductieNeterminal(self, neterminalSursa, neterminalStanga, neterminalDreapta):
        self.productiiNeterminali.get(neterminalSursa).remove(tuple((neterminalStanga, neterminalDreapta)))
        if len(self.productiiNeterminali.get(neterminalSursa)) == 0:
            self.productiiNeterminali.pop(neterminalSursa)

    def stergeNeterminal(self, neterminal):
        self.neterminali.remove(neterminal)
        if neterminal in self.productiiNeterminali:
            self.productiiNeterminali.pop(neterminal)

        for lista in self.productiiNeterminali.values():
            for productie in lista:
                if neterminal in productie:
                    lista.remove(productie)

    def stergeTerminal(self, terminal):
        self.terminali.remove(terminal)

        if terminal in self.productiiTerminali:
            self.productiiTerminali.pop(terminal)

        for productii in self.productiiNeterminali.values():
            if terminal in productii:
                productii.remove(terminal)

    def neterminaliGenereazaTerminal(self, terminal):
        deReturnat = []
        for neterminal, terminali in self.productiiTerminali.items():
            if terminal in terminali:
                deReturnat += neterminal
        return set(deReturnat)

    def neterminaliGenereazaNeterminal(self, neterminalStanga, neterminalDreapta):
        deReturnat = []
        for neterminalSursa, neterminali in self.productiiNeterminali.items():
            if (neterminalStanga, neterminalDreapta) in neterminali:
                deReturnat += neterminalSursa
        return set(deReturnat)

    def listaNeterminaliGenereazaNeterminali(self, productii):
        deReturnat = set()
        for stanga, dreapta in productii:
            deReturnat = deReturnat | self.neterminaliGenereazaNeterminal(stanga, dreapta)
        return deReturnat

    def produsCartezian(self, set1, set2):
        return set([(x, y) for x in set1 for y in set2])

    def graficCuvantCYK(self, cuvant):
        m = [[set() for x in range(len(cuvant))] for y in range(len(cuvant))]
        for i in range(len(cuvant)):
            m[0][i] = self.neterminaliGenereazaTerminal(cuvant[i])

        n = len(cuvant)
        for j in range(1, n):
            for i in range(n - j):
                for k in range(j):
                    m[j][i] = m[j][i] | self.listaNeterminaliGenereazaNeterminali(
                        self.produsCartezian(m[k][i], m[j - k - 1][i + k + 1])
                    )

        coloane = ["i="+str(i) for i in range(1, n+1)]
        randuri = ["j="+str(j) for j in range(1, n+1)]

        df = pandas.DataFrame(m, randuri, coloane)
        print(df)

    def verificaCuvantCYK(self, cuvant):
        m = [[set() for x in range(len(cuvant))] for y in range(len(cuvant))]
        for i in range(len(cuvant)):
            m[0][i] = self.neterminaliGenereazaTerminal(cuvant[i])

        n = len(cuvant)
        #indexare de la 0
        for j in range(1, n):
            for i in range(n - j):
                for k in range(j):
                    m[j][i] = m[j][i] | self.listaNeterminaliGenereazaNeterminali(
                        self.produsCartezian(m[k][i], m[j - k - 1][i + k + 1])
                    )

        return self.startSymbol in m[n-1][0]

    def afiseazaGramatica(self):
        for neterminal in self.neterminali:
            productiiNeterminali = self.productiiNeterminali.get(neterminal, [])
            productiiTerminali = self.productiiTerminali.get(neterminal, [])
            if len(productiiTerminali) != 0 or productiiTerminali != 0:
                print(neterminal, "->", end=" ")

            endChar = ""
            if len(productiiTerminali) != 0:
                endChar = " | "
            print(" | ".join([x[0] + "*" + x[1] for x in productiiNeterminali]), end=endChar) #se citeste si afiseaza cu *
                                                                             #in caz de neterminali cu nume mai mari de un simbol
            print(" | ".join(productiiTerminali))
