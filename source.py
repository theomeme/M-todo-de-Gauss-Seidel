def haZeroNaDiagonal(m):
    qtdDeZeros = 0
    posicao = 0
    while posicao < len(m):
        if m[posicao][posicao] == 0: qtdDeZeros += 1
        posicao += 1
    return qtdDeZeros > 0


def poeUmNaDiagonalPrincipalNaLinha(lin, m):
    divisor = m[lin][lin]
    col = 0
    while col <= len(m):
        m[lin][col] /= divisor
        col += 1

def seNaoETudoZero(m):

    for col in range(len(m)):
        for lin in range(len(m)):
            if lin != col:
                if m[lin][col] != 0:
                    m[lin][col]
                    vetor_negativo = m[lin]
def ondeTemZero():
    while haZeroNaDiagonal(matriz):
        count = 0
        while count < len(matriz):
            if matriz[count][count] == 0:
                return count

            count += 1



matriz = [[5, 2, 5, 1], \
          [9, 1, 2, 7], \
          [3, 6, 2, 3]]

def __main__(matriz):
    poeUmNaDiagonalPrincipalNaLinha(1, matriz)
    print(matriz)
    #print (haZeroNaDiagonal(matriz))
    length = len(matriz)
    print(poeUmNaDiagonalPrincipalNaLinha(1, matriz))
    if not haZeroNaDiagonal(matriz):
        for i in range(length):
            poeUmNaDiagonalPrincipalNaLinha(i, matriz)

        print(matriz)


__main__(matriz)