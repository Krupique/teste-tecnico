import sys

def readFile(arg_input):
    f_input = []
    with open(arg_input, 'r') as fp:
        f_input = fp.readlines()

    input = []
    for num in f_input:
        input.append(int(num.replace('\n', '').replace(' ', '')))


    ttask = input[0]
    umax = input[1]
    input = input[2:]

    return input, ttask, umax

def createMatrix(input, ttask, umax):
    lista_servidores = []
    maior_array = 0

    for i in range(len(input)):
        for j in range(input[i]):
                temp = [0 for k in range(i)]
                temp.extend([1 for k in range(ttask)])

                lista_servidores.append(temp)

                if maior_array < len(temp):
                    maior_array = len(temp)
            
    for i in range(len(lista_servidores)):
        temp = [0 for k in range(maior_array - len(lista_servidores[i]))]
        lista_servidores[i].extend(temp)

    lista_t = list(map(list, zip(*lista_servidores)))

    return lista_t

def executeCalculations(lista_t):
    lista_resultado = []
    qtd_servidores_ativos = int(round(len(lista_t[0]) / umax, 0))
    lista_custo = [0 for i in range(qtd_servidores_ativos)]

    for i in range(len(lista_t)):
        resultado_linha = []
        contador, k, c = 0 
        flag_c = True

        for j in range(len(lista_t[i])):
            if lista_t[i][j] == 1:
                contador += 1
                
                if flag_c:
                    lista_custo[c] += 1
                    flag_c = False
            
            if k < umax - 1:
                k += 1
            else:
                if contador != 0:
                    resultado_linha.append(contador)
                contador, k = 0
                c += 1
                flag_c = True
                
        lista_resultado.append(resultado_linha)

    lista_resultado.extend([[sum(lista_custo)]])

    return lista_resultado

def writeFile(arg_output, lista_resultado):
    with open(arg_output, "w") as fp:
        for linha in lista_resultado:
            s_linha = str(linha).replace('[', '').replace(']', '').replace(' ', '')

            fp.write(f'{s_linha}\n')

if __name__ == "__main__":
    arg_input = sys.argv[1]
    arg_output = sys.argv[2]

    input, ttask, umax = readFile(arg_input)
    lista_t = createMatrix(input, ttask, umax)
    lista_resultado = executeCalculations(lista_t)

    writeFile(arg_output, lista_resultado)


