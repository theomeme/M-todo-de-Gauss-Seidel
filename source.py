def haZeroNaDiagonal(m):
    #verificação de há zero na diagona principal
    #retorna a quantidade de zeros na diagonal principal
    qtdDeZeros = 0
    posicao = 0
    while posicao < len(m):
        if m[posicao][posicao] == 0: qtdDeZeros += 1
        posicao += 1
    return qtdDeZeros > 0


def poeUmNaDiagonalPrincipalNaLinha(lin, m):
    #Adiciona o número 1 na diagonal principal
    #Parametros = {number}Linha / {variavel}Matriz
    #Retorna a a linha com o 1 na diagonal principal
    divisor = m[lin][lin]
    col = 0
    while col <= len(m):
        m[lin][col] /= divisor
        col += 1

def seNaoETudoZero(m, col):
    #Verifica se há um zero na matriz , varrendo a matriz inteira por linha e coluna
    #Parametro = {variavel} Matriz
    # Retorna {boolen} True / False
    vetor_negativo = []
    for lin in range(len(m) - 1):
        if lin != col:
            if m[lin][col] != 0:
                vetor_negativo[lin][col] = m[lin][col] * (-1)
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
      #  for col in range(length-1):
        #    seNaoETudoZero(matriz, 0)
         #   print(matriz)
        seNaoETudoZero(matriz, 0)
        print(matriz)

__main__(matriz)