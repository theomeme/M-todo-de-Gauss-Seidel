#def coeficienteDosPares(m):
    #************** precisa ser implementada ********************
    # retorna a divisão dos coeficientes de qualquer par de linhas da matriz dada


#def verificaSeHaDiferentes(coeficiente):
    # ************** precisa ser implementada ********************
    #verifica se há elementos diferentes entre si em uma lista

#def trocaLinha()
# usa a função ondeTemZero para trocar de posição uma linha com zero na diagonal principal

def haZeroNaDiagonal(m):
    # verificação de há zero na diagona principal
    # retorna a quantidade de zeros na diagonal principal
    qtdDeZeros = 0
    posicao = 0
    while posicao < len(m):
        if m[posicao][posicao] == 0: qtdDeZeros += 1
        posicao += 1
    return qtdDeZeros > 0


def poeUmNaDiagonalPrincipalNaLinha(lin, m):
    # Adiciona o número 1 na diagonal principal
    # Parametros = {number}Linha / {variavel}Matriz
    # Retorna a a linha com o 1 na diagonal principal
    divisor = m[lin][lin]
    col = 0
    for col in range(0, len(m) + 1):
        m[lin][col] /= divisor
        col += 1


def seNaoETudoZero(m, col):
    # Verifica se há um zero na matriz , varrendo a matriz inteira por linha e coluna
    # Parametro = {variavel} Matriz
    # Retorna {boolen} True / False
    linha_negativa = []
    print('entrou na seNaoETudoZero')
    print(len(m))
    for lin in range(len(m)):
        mult = m[lin][col]
        print('tamanho da linha', len(m) - 1)
        print(lin)
        if lin != col:
            if m[lin][col] != 0:
                m[lin][col] = m[lin][col] - (mult * (m[col][col]))


def temZeroNaColuna(m, col):
    for lin in range(len(m) - 1):
        if m[lin][col] == 0:
            return True
    return False


def quantosZerosTem():
    while haZeroNaDiagonal(matriz):
        count = 0
        while count < len(matriz):
            if matriz[count][count] == 0:
                return count

            count += 1

def ondeTemZero():
    #retorna em qual linha existe zero na diagonal principal
    for lin in range(len(matriz) - 1):
        if matriz[lin][lin] == 0:
            return lin

matriz = [[5, 2, 5, 1], \
          [9, 1, 2, 7], \
          [3, 6, 2, 3]]


# def __main__(matriz):
#     poeUmNaDiagonalPrincipalNaLinha(1, matriz)
#     print(matriz)
#     #print (haZeroNaDiagonal(matriz))
#     length = len(matriz)
#     print(poeUmNaDiagonalPrincipalNaLinha(1, matriz))
#     if not haZeroNaDiagonal(matriz):
#         for i in range(length):
#             poeUmNaDiagonalPrincipalNaLinha(i, matriz)
#         for col in range(length-1):
#             seNaoETudoZero(matriz, 0)
#             print(matriz)
#         seNaoETudoZero(matriz, 0)
#         print(matriz)

def __main__():
    print(matriz)
    poeUmNaDiagonalPrincipalNaLinha(0, matriz)
    print(matriz)
    seNaoETudoZero(matriz, 0)
    print(matriz)
    poeUmNaDiagonalPrincipalNaLinha(1, matriz)
    print(matriz)
    seNaoETudoZero(matriz, 1)
    print(matriz)
    poeUmNaDiagonalPrincipalNaLinha(2, matriz)
    print(matriz)
    seNaoETudoZero(matriz, 2)
    print(matriz)


__main__()
