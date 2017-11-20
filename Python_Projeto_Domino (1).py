# -------------------------------------------------------------------------------
# versão não final ainda com bugs
# # -------------------------------------------------------------------------------

import random


# -------------------------------------------------------------------------------
#
# CLASSE PEÇA
#
# -------------------------------------------------------------------------------

class Peça:
    valorA = 0
    valorB = 0

    def novo ( self, valorA, valorB ):
        if valorA > valorB:
            self.valorA = valorA
            self.valorB = valorB
            self.giro = True
        else:
            self.valorA = valorA
            self.valorB = valorB
            self.giro = False

    def ver ( self ):
        print("[(", self.valorA, "-", self.valorB, ")]", ",", end="")
        return ""

    def contar ( self ):
        somaPeças = self.valorA + self.valorB
        return somaPeças


# -------------------------------------------------------------------------------
#
# CLASSE JOGADOR
#
# -------------------------------------------------------------------------------
class Jogador:
    ArrayPeças = []
    pontuação = 0
    tipo = ""
    inteligencia = 0
    PularVez = 0
    pontuaçãoGeral = 0


    def escrever ( self ):
        print("-----------------------Peças-------------------------------------------------")
        for a in self.ArrayPeças:
            a.ver()

    def somaPeças ( self ):  # retorna a somaPeças
        somaPeças = 0
        f = Peça()
        for f in self.ArrayPeças:
            somaPeças += f.valorA + f.valorB
        return somaPeças

    def contarListaDada ( self, lista ):
        somaPeças = 0
        f = Peça()
        for f in lista:
            somaPeças += 1
        return somaPeças


    def elimina ( self, PeçaBuscar ):
        for PeçaX in self.ArrayPeças:
            if PeçaX.valorA == PeçaBuscar.valorA and PeçaX.valorB == PeçaBuscar.valorB:
                self.ArrayPeças.remove(PeçaX)

    def listaPeçasQuePodemColocar ( self, tabuleiro, Valor, lugar ):
        devolver = []
        for X in self.ArrayPeças:
            if X.valorA == Valor and X.valorB == Valor:
                if lugar == "ParteDebaixo":
                    X.giro = False
                    devolver.append(X)
                    X.giro = True
                    devolver.append(X)
                    return devolver
                else:
                    X.giro = False
                    devolver.append(X)
                    X.giro = True
                    devolver.append(X)
                    return devolver
            if X.valorA == Valor:
                if lugar == "ParteDebaixo":
                    X.giro = False
                else:
                    X.giro = True
                devolver.append(X)
            elif X.valorB == Valor:
                if lugar == "ParteDeCima":
                    X.giro = False
                else:
                    X.giro = True
                devolver.append(X)
        return devolver

    def MostrarPeças ( self, lista ):
        contador = -1
        if len(lista) > 0:
            for f in lista:
                contador += 1
                print("Numero Indice: ", contador, " Peça:", f.valorA, ":", f.valorB)

    def coloca ( self, tabuleiro ):
        PeçasParteDeCima = []
        PeçasParteDebaixo = []
        #  UltimaPeça=[]
        TotalMovimentos = 0
        # criar lista de Peças que pode colocar na Parte de cima do tabuleiro
        PeçasParteDeCima = self.listaPeçasQuePodemColocar(tabuleiro, tabuleiro.ParteDeCima, "ParteDeCima")

        # criar lista de Peças que pode colocar na Parte de baixo do tabuleiro
        PeçasParteDebaixo = self.listaPeçasQuePodemColocar(tabuleiro, tabuleiro.ParteDebaixo, "ParteDebaixo")

        TotalMovimentos = self.contarListaDada(PeçasParteDeCima) + self.contarListaDada(PeçasParteDebaixo)

        # Se a somaPeças dos elementos das listas=1, então é a última Peça-> ganhador...!!


        if TotalMovimentos > 0 and self.contarListaDada(self.ArrayPeças) == 1:
            if len(PeçasParteDebaixo) == 0:
                UltimaPeça = PeçasParteDeCima[0]
                lugar = "ParteDeCima"

            else:
                UltimaPeça = PeçasParteDebaixo[0]
                lugar = "ParteDebaixo"
            self.elimina(UltimaPeça)
            return "UltimaPeça", UltimaPeça, lugar

        if TotalMovimentos == 0:
            return "PassaVez", "", ""

        if self.tipo == "CPU":
            if self.inteligencia == 1:
                # Pode escolher das listas a peça para colocar'
                if len(PeçasParteDeCima) > 0 and len(PeçasParteDebaixo) > 0:
                    if random.randint(0, 1) == 1:
                        PeçaMudada = random.sample(PeçasParteDeCima, 1)
                        self.elimina(PeçaMudada[0])
                        return "Coloca", PeçaMudada[0], "ParteDeCima"
                    else:
                        PeçaMudada = random.sample(PeçasParteDebaixo, 1)
                        self.elimina(PeçaMudada[0])
                        return "Coloca", PeçaMudada[0], "ParteDebaixo"
                        # Só pode colocar na Parte de cima
                if len(PeçasParteDeCima) > 0:
                    PeçaMudada = random.sample(PeçasParteDeCima, 1)
                    self.elimina(PeçaMudada[0])
                    return "Coloca", PeçaMudada[0], "ParteDeCima"
                else:
                    # Só pode colocar na Parte de baixo
                    PeçaMudada = random.sample(PeçasParteDebaixo, 1)
                    self.elimina(PeçaMudada[0])
                    return "Coloca", PeçaMudada[0], "ParteDebaixo"

        print(self.tipo, self.inteligencia)

        return "Error", "0", "0"


# -------------------------------------------------------------------------------
#
# CLASSE TABULEIRO
#
# -------------------------------------------------------------------------------
class tabuleiro:
    ArrayPeçasParteDeCima = []  
    ArrayPeçasParteDebaixo = []  
    ParteDebaixo = 0
    ParteDeCima = 0

    def inicia ( self, Peça ):
        ParteDebaixo = Peça.valorA
        ParteDeCima = Peça.valorB
        Peça.giro = 0
        self.ArrayPeçasParteDeCima.append(Peça)

    def Coloca ( self, Peça, lugar ):
        # A peça é colocada,e os valores da parte de cima e da parte de baixo são atualizados

        #print("Lugar no tabuleiro:", lugar)
        #print("Peça que ponho no tabuleiro:", Peça.ver())
        if lugar == "ParteDebaixo":
            self.ArrayPeçasParteDebaixo.insert(0, Peça)
            if self.ParteDebaixo == Peça.valorA:
                self.ParteDebaixo = Peça.valorB
                return
            else:
                self.ParteDebaixo = Peça.valorA
                return
        if lugar == "ParteDeCima":
            self.ArrayPeçasParteDeCima.append(Peça)
            if self.ParteDeCima == Peça.valorA:
                self.ParteDeCima = Peça.valorB
                return
            else:
                self.ParteDeCima = Peça.valorA
                return

    def ver ( self ):

        valorgiro = 0
        posinicial = 6
        contador = 0
        print
        print("\n------------------ PARTE DE BAIXO DO TABULEIRO -------------------------------")
        for f in self.ArrayPeçasParteDebaixo:
            contador -= 1
            if self.ArrayPeçasParteDebaixo[contador].giro == False:
                print("[(", self.ArrayPeçasParteDebaixo[contador].valorA, "-",
                      self.ArrayPeçasParteDebaixo[contador].valorB, ")]", ",", end="")

            else:
                print("[(", self.ArrayPeçasParteDebaixo[contador].valorB, "-",
                      self.ArrayPeçasParteDebaixo[contador].valorA, ")]",
                      ",", end="")

        valorgiro = -1
        posinicial = 6
        print
        print("\n------------------ PARTE DE CIMA DO TABULEIRO --------------------------------")
        for f in self.ArrayPeçasParteDeCima:
            if posinicial == f.valorA:
                print("[(", f.valorA, "-", f.valorB, ")]", ",", end="")
                posinicial = f.valorB
            else:
                print("[(", f.valorB, "-", f.valorA, ")]", ",", end="")
                posinicial = f.valorA

        print


# ------------------------------------------------------------
#
# FUNÇÕES DO JOGO
#
# ------------------------------------------------------------

def Quantidade ( lista ):
    contador = 0
    for a in lista:
        contador = contador + 1
    return contador


def tipoJogador ( texto ):
    JogadorSelecionado = Jogador()
    JogadorSelecionado.tipo = "CPU"
    JogadorSelecionado.inteligencia = 1

    return JogadorSelecionado


def escolherJogadores ():
    print("-----------------------------------------------------------------------")
    print("Começa o jogo.... definindo os jogadores")
    print("-------------X------------------------------X------------------X-------")
    JogadorA = tipoJogador("Jogador A")
    JogadorB = tipoJogador("Jogador B")
    return JogadorA, JogadorB


def verficarJogadorComPeça ( PeçaProcurada, jogA, jogB ):
    # Essa função serve para saber que o jogador tem una determinada peça (6:6 por exemplo)
    a = Peça()
    for a in jogA.ArrayPeças:
        if (a.valorA == PeçaProcurada.valorA) and (a.valorB == PeçaProcurada.valorB):
            return jogA, 0
    return jogB, 1


def jogo ( JogadorA, JogadorB ):
    # gear peças...

    Peça_Prototipo = Peça()
    GrupoPeça = []
    contador = 0
    possibilidades = [0, 1, 2, 3, 4, 5, 6, 7]
    for a in possibilidades:
        for b in possibilidades[a:7]:
            contador = contador + 1
            Peça_Prototipo = Peça()
            Peça_Prototipo.novo(a, b)
            GrupoPeça.append(Peça_Prototipo)

    ListaJogadores = []
    ListaJogadores = [JogadorA, JogadorB]

    # Dividir as peças aos jogadores
    aleatorio = 0
    listaOrdenadaAleatoriamente = random.shuffle(GrupoPeça)
    ListaJogadores[0].ArrayPeças = GrupoPeça[:5]
    listaOrdenadaAleatoriamente = random.shuffle(GrupoPeça)
    ListaJogadores[1].ArrayPeças = GrupoPeça[:5]

    print("As peças foram distribuídas:")
    print("-------------------------------------")
    print("Jogador A:")
    print(ListaJogadores[0].escrever())
    print(ListaJogadores[0].somaPeças())
    print("-------------------------------------")
    print("Jogador B:")
    print(ListaJogadores[1].escrever())
    print(ListaJogadores[1].somaPeças())

    # Inicio do jogo

    PeçaBuscar = Peça()
    PeçaBuscar.valorA = 6
    PeçaBuscar.valorB = 6

    jog = Jogador()
    jog, numero = verficarJogadorComPeça(PeçaBuscar, ListaJogadores[0], ListaJogadores[1])

    print("Verificando as peças e iniciando o jogo...")
    # Começa o jogo ...
    if numero == 1:
        print("Jogador A")
    else:
        print("Jogador B")

    jog.elimina(PeçaBuscar)

    Tabuleiro = tabuleiro()
    Tabuleiro.ParteDebaixo = PeçaBuscar.valorA
    Tabuleiro.ParteDeCima = PeçaBuscar.valorB
    Tabuleiro.inicia(PeçaBuscar)

    jog.escrever()

    print("")
    ListaJogadores[numero - 1].escrever()

    # Inicia as variáveis do loop principal...
    PeçaColocada = Peça()
    Lugar = ""
    resposta = ""
    print("\nNumero:", numero)
    valorAnterior = ""
    loop = True

    # loop Principal do jogo...
    while loop:
        if numero == 1:
            print("O jogador A faz a jogada...")
            resposta, PeçaColocada, lugar = ListaJogadores[0].coloca(Tabuleiro)
            nomeJogador = "A"
            if resposta == "Coloca":
                #soma 4 na pontuação ao colocar as peças
             ListaJogadores[0].pontuação = ListaJogadores[0].pontuação + 4

        else:
            print("O jogador B faz a jogada...")
            resposta, PeçaColocada, lugar = ListaJogadores[1].coloca(Tabuleiro)
            nomeJogador = "B"
            if resposta == "Coloca":
                # soma 4 na pontuação ao colocar as peças
             ListaJogadores[1].pontuação = ListaJogadores[1].pontuação + 4


        if resposta == "UltimaPeça":
            Tabuleiro.Coloca(PeçaColocada, lugar)

            print("Foi colocada a última peça do jogador!!")
            print("Fim de jogo!")
            break
        elif resposta == "Coloca":
            print("Coloca:", PeçaColocada.ver(), "Lugar:", lugar)
            Tabuleiro.Coloca(PeçaColocada, lugar)
           # if nomeJogador == "A"
            #    ListaJogadores[0].pontuação = ListaJogadores[0].pontuação + 4
            #else
             #   ListaJogadores[1].pontuação = ListaJogadores[1].pontuação + 4


            valorAnterior = ""
        elif resposta == "PassaVez":
            if numero == 1:
                ListaJogadores[0].PularVez = ListaJogadores[0].PularVez + 1

            else:
                ListaJogadores[1].PularVez = ListaJogadores[1].PularVez + 1

            print("Passou a vez.")
            if valorAnterior == "PassaVez":

                if ListaJogadores[0].somaPeças() == ListaJogadores[1].somaPeças():
                    print("Fim de jogo")
                    print("Empate, tem os mesmos pontos")

                elif ListaJogadores[0].somaPeças() < ListaJogadores[1].somaPeças():
                    print("Fim de Jogo!")
                    ListaJogadores[0].pontuação += ListaJogadores[0].somaPeças() + ListaJogadores[1].somaPeças()
                else:
                    print("Fim de Jogo!")
                    ListaJogadores[1].pontuação += ListaJogadores[0].somaPeças() + ListaJogadores[1].somaPeças()
                break
            else:

                valorAnterior = "PassaVez"

        if numero == 0:
            numero = 1
        else:
            numero = 0

        print("---Opções disponíveis: [(", Tabuleiro.ParteDebaixo,"e", Tabuleiro.ParteDeCima, ")]-")
        loop = True
    # -------------------------------------------------------------------------------
    #
    # FINAL DE JOGO!
    #
    # -------------------------------------------------------------------------------
    print("=============================================================================")
    print("=                            Fim de jogo                     =")
    print("=============================================================================")
    print("Resultado:")
    Tabuleiro.ver()
    # perde 2 pontos ao passar a vez
    ListaJogadores[0].pontuação = ListaJogadores[0].pontuação - ((ListaJogadores[0].PularVez)* 2)
    ListaJogadores[1].pontuação = ListaJogadores[1].pontuação - ((ListaJogadores[1].PularVez) * 2)
    print("\nO jogador A fez um total de ")
    print("PONTOS:", ListaJogadores[0].pontuação)
    print("Número de vezes que não colocou a peça: ", ListaJogadores[0].PularVez)
    print(ListaJogadores[0].escrever())
    print("O jogador B fez um total de ")
    print("PONTOS:", ListaJogadores[1].pontuação)
    print("Número de vezes que não colocou a peça: ", ListaJogadores[1].PularVez)
    print(ListaJogadores[1].escrever())
    if ListaJogadores[0].pontuação > ListaJogadores[1].pontuação:
        print("----------------------------------")
        print("O ganhador é: Jogador A")
        print("----------------------------------")
        print("Jogador A venceu")
    elif ListaJogadores[0].pontuação < ListaJogadores[1].pontuação:
        print("----------------------------------")
        print("O ganhador é: Jogador B")
        print("----------------------------------")
        print("Jogador B venceu")
    else:
        print("----------------------------------")
        print("EMPATE!!!!")
        print("----------------------------------")

    return ListaJogadores[0], ListaJogadores[1]

    pass


# -------------------------------------------------------------------------------
#
# MAIN
#
# -------------------------------------------------------------------------------
def main ():
    jogA = Jogador()
    jogB = Jogador()
    listaJogadores = [jogA, jogB]
    print("")
    print("-------------------------------")
    print("-        Jogo de domino     -")
    print("-------------------------------")
    print("1- Jogar dominó!")
    resposta = int(input("Digite a opção:"))

    jogA, jogB = escolherJogadores()
    if resposta == 1:
        jogA.pontuação = 10
        jogB.pontuação = 10
        print("Pontuação Inicial:\nA:", jogA.pontuação, "| B:", jogB.pontuação)
        for f in range(1):
            jogA, jogB = jogo(jogA, jogB)
            jogA.pontuaçãoGeral += jogA.pontuação
            jogB.pontuaçãoGeral += jogB.pontuação

        print("Pontuação final:\nA:", jogA.pontuaçãoGeral, "| B:", jogB.pontuaçãoGeral)


    pass


if __name__ == '__main__':
    main()
