#def coeficienteDosPares(m):
#    for lin in range (len(m)):


#def listaComParesPossiveis():
#    range = [0]
#    for i in range(len(matriz)):
#        range.append(i + 1)
#    print(range)

def all_pairs(lst):
    if len(lst) < 2:
        yield []
        return
    if len(lst) % 2 == 1:
        # Handle odd length list
        for i in range(len(lst)):
            for result in all_pairs(lst[:i] + lst[i+1:]):
                yield result
    else:
        a = lst[0]
        for i in range(1,len(lst)):
            pair = (a,lst[i])
            for rest in all_pairs(lst[1:i]+lst[i+1:]):
                yield [pair] + rest

#def verificaSeHaDiferentes(coeficiente):
    # ************** precisa ser implementada ********************
    #verifica se há elementos diferentes entre si em uma lista

def trocaLinha(m, lin):
    # usa a função ondeTemZero para trocar de posição uma linha com zero na diagonal principal
    if haZeroNaDiagonal:
        for index_line in range(0, len(matrix)):
            for try_line in range(0, len(matrix)):
                if index_line == try_line:
                    continue
                else:
                    matrix = matrix
                    pivot_line = matrix[try_line]
                    matrix.insert(try_line, matrix[index_line])
                    matrix.pop(try_line + 1)
                    matrix.insert(index_line, pivot_line)
                    matrix.pop(index_line + 1)
                    if verify_zero_matrix(matrix) == False:
                        return matrix
    else:
        return True


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
    for lin in range(len(m)):
        mult = m[lin][col]
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

def __main__():
    print(matriz)

#    print(listaComParesPossiveis())

    for lin in range(len(matriz)):
        poeUmNaDiagonalPrincipalNaLinha(lin, matriz)

    for col in range(len(matriz)):
        seNaoETudoZero(matriz, col)
    print(matriz)


__main__()
