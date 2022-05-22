import sys


# função auxiliar  recursivo que, de fato, gera as permutacoes
# NÃO USE DIRETAMENTE ESTA FUNÇÃO; USE A FUNÇÃO permutacoes
# recebe uma lista com os valores a serem permutados (linha),
# uma lista com os itens na permutação sendo gerada (perm) e
# uma lista com as permutações geradas (perms)
def permuta(linha, perm, perms):
    # FUNCIONANDO PERFEITAMENTE
    if not linha:
        perms.append(perm)
    else:
        for lin in range(len(linha)):
            permuta(linha[0:lin] + linha[lin + 1:len(linha)], perm + [linha[lin]], perms)


# função principal para gerar permutações;
# USA A FUNÇÃO permuta, QUE NÃO DEVE SER USADA DIRETAMENTE;
# recebe uma lista com os valores a serem permutados (linha)
# retorna as permutações geradas
def permutacoes(linha):
    # FUNCIONANDO PERFEITAMENTE
    perms = []
    permuta(linha, [], perms)
    return perms


def listaOrdenadaGenerica(m):
    lista_linhas = []
    for pos in range(len(m)):
        lista_linhas.append(pos)
    return lista_linhas


def combinacoesDeLinhas2a2(m):
    ret = []
    for lin in range(len(m)):
        for col in range(lin + 1, len(m)):
            ret.append([lin, col])
    return ret


def divisao(a, b):
    if a == 0 and b == 0:
        return "indeterminado"
    elif b == 0:
        return "infinito"
    else:
        return a / b


def divDumVetorPorOutro(x, y):
    ret = []
    for i in range(len(x) - 1):
        ret.append(divisao(x[i], y[i]))
    return ret


def coeficientesPossiveis(comb, m):
    # gera um vetor com os coeficientes da divisao de quaisquer linhas
    vet = []
    for pos in range(len(comb)):
        vet.append(divDumVetorPorOutro(m[comb[pos][0]], m[comb[pos][1]]))
        print("vet:", vet)
    if tudoIgual(vet):
        return False
    else:
        return True


def tudoIgual(vet):
    for pos in range(len(vet)):
        vetComp = vet[pos]
        if all(i == vetComp[0] for i in vetComp):
            return True
        return False


def haZeroNaDiagonal(m, permL, permC):
    # verificação de há zero na diagona principal
    # retorna a quantidade de zeros na diagonal principal
    for pos in range(len(m)):
        if m[permL[pos]][permC[pos]] == 0:
            return True
    return False


def poeUmNaDiagonalPrincipalNaLinha(lin, m, permL, permC):
    # Adiciona o número 1 na diagonal principal
    # Parametros = {number}Linha / {variavel}Matriz
    # Retorna a a linha com o 1 na diagonal principal
    divisor = m[permL[lin]][permC[lin]]
    for col in range(len(m)):
        m[permL[lin]][permL[col]] /= divisor
    m[permL[lin]][len(m)] /= divisor


def seNaoETudoZero(m, col, permL, permC):
    # TODO: Implementar lógica corretamente
    # Muda todos os numeros para zero em uma determinada coluna
    # Parametro = {variavel} Matriz
    for lin in range(len(m)):
        mult = m[permL[col]][permC[col]]
        if lin != col:
            if m[permL[lin]][permC[col]] != 0:
                m[permL[lin]][permC[col]] = m[permL[lin]][permC[col]] - (mult * (m[permL[lin]][permC[col]]))


def temZeroNaColuna(m, col):
    # verifica se todos os elementos de uma coluna sao zero exceto a diagonal principal
    # Parametros: (matriz, coluna)
    for lin in range(len(m) - 1):
        if m[lin][col] == 0:
            return True
    return False


def quantosZerosTem(m, permL, permC):
    # FUNCIONANDO PERFEITAMENTE
    # retorna a quantidade de zeros na diagonal principal
    while haZeroNaDiagonal(m, permL, permC):
        count = 0
        while count < len(m):
            if m[count][count] == 0:
                return count

            count += 1


def comoSeLivrarDeZerosNaDiagonal(matriz):
    # FUNCIONANDO PERFEITAMENTE
    # Gera ordem virtual de resolução da matriz
    perms = permutacoes(list(range(len(matriz))))
    for i in range(len(perms)):
        for j in range(len(perms)):
            if not haZeroNaDiagonal(matriz, perms[i], perms[j]):
                return [perms[i], perms[j]]

    return None


def ondeTemZero(m):
    # retorna em qual linha existe zero na diagonal principal
    for lin in range(len(m) - 1):
        if m[lin][lin] == 0:
            return lin


def carregaMatriz(nomeArq):
    arq = open(nomeArq, "r")
    qtdLins = int(arq.readline())

    ret = []
    for lin in range(qtdLins):
        texto = arq.readline().split()

        linha = []
        for col in range(qtdLins + 1):
            linha.append(float(texto[col]))

        ret.append(linha)

    arq.close()
    return ret


def __main__():

    try:
        # matriz = str(input("Digite o nome do arquivo da matriz a ser lida: "))
        # carregaMatriz(matriz)
        matriz = [[0, 3, 2, 28], \
                  [4, 0, 2, 24], \
                  [2, 3, 0, 16]]
        perm = listaOrdenadaGenerica(matriz)
        print("Length:", len(matriz))
        permL = perm
        permC = perm

        print(matriz)
        comb = combinacoesDeLinhas2a2(matriz)
        print("comb:", comb)
        res = []
        for pos in range(len(matriz)):
            res.append(divDumVetorPorOutro(matriz[comb[pos][0]], matriz[comb[pos][1]]))

        if tudoIgual(res):
            print("A divisão dos coeficientes de duas ou mais linhas é idêntica! A matriz não é solucionável!")
            sys.exit()

        if haZeroNaDiagonal(matriz, permL, permC):
            vetorPerms = comoSeLivrarDeZerosNaDiagonal(matriz)
            permL = vetorPerms[0]
            permC = vetorPerms[1]

        for pos in range(len(matriz)):
            poeUmNaDiagonalPrincipalNaLinha(pos, matriz, permL, permC)
            print("Coloca 1 na diagonal", matriz)
            seNaoETudoZero(matriz, pos, permL, permC)
            print("Coloca 0 na coluna", matriz)
        print(comoSeLivrarDeZerosNaDiagonal(matriz))
        print(matriz)


    except TypeError:
        print("Não é possível resolver essa matriz!")

    # for pos in range(len(matriz)):
    #     poeUmNaDiagonalPrincipalNaLinha(pos, matriz, permL, permC)
    #     seNaoETudoZero(matriz, pos, permL, permC)
    # try:
    #     comb = combinacoesDeLinhas2a2(matriz)
    #     if not coeficientesPossiveis(comb):
    #         print("A divisão dos coeficientes de duas ou mais linhas é idêntica! A matriz não é solucionável!")
    #         sys.exit()
    #     if comoSeLivrarDeZerosNaDiagonal(matriz) is not None:
    #         print(comoSeLivrarDeZerosNaDiagonal(matriz))
    #         vetorPerms = comoSeLivrarDeZerosNaDiagonal(matriz)
    #         permL = vetorPerms[0]
    #         permC = vetorPerms[1]
    #         print("permL", permL)
    #         print("permC", permC)
    #     else:
    #         print("Não há uma maneira de organizar essa matriz de forma que "
    #               "se tire todos os zeros da diagonal principal!\n A matriz não é solucionável!")
    #         sys.exit()
    #
    #     if not haZeroNaDiagonal(matriz, permL, permC):
    #         for lin in range(len(matriz)):
    #             poeUmNaDiagonalPrincipalNaLinha(lin, matriz, permL, permC)
    #
    #         for col in range(len(matriz)):
    #             seNaoETudoZero(matriz, col)
    #     print(matriz)

__main__()


