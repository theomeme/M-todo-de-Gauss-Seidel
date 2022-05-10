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
        print(m)

def seNaoETudoZero(m):
    #Verifica se há um zero na matriz , varrendo a matriz inteira por linha e coluna
    #Parametro = {variavel} Matriz
    # Retorna {boolen} True / False
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



matriz = [[5, 2, 0, 1], \
          [9, 1, 2, 7], \
          [3, 6, 2, 3]]

print(matriz)


