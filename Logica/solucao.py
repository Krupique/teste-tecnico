import sys

def readFile(arg_input):
    # abrindo arquivo
    f_input = []
    with open(arg_input, 'r') as fp:
        f_input = fp.readlines()

    # Convertendo os dados de entrada para int
    input = []
    for num in f_input:
        input.append(int(num.replace('\n', '').replace(' ', '')))

    # Separando as entradas
    ttask = input[0]
    umax = input[1]
    input = input[2:]

    return input, ttask, umax

def createMatrix(input, ttask, umax):
    lista_servidores = []
    maior_array = 0

    # Criando uma lista de lista com os servidores ativos, onde:
    # 1 é o valor ativo
    # 0 é o valor inativo
    for i in range(len(input)):
        for j in range(input[i]):
                temp = [0 for k in range(i)]

                temp.extend([1 for k in range(ttask)])

                lista_servidores.append(temp)

                if maior_array < len(temp):
                    maior_array = len(temp)
            
    # Aqui eu vou preencher os valores restantes com 0 para formar uma matriz.
    for i in range(len(lista_servidores)):
        temp = [0 for k in range(maior_array - len(lista_servidores[i]))]
        lista_servidores[i].extend(temp)

    # Realizando a transposta da matriz
    lista_t = list(map(list, zip(*lista_servidores)))

    return lista_t

def executeCalculations(lista_t):
    # Lista que armazena o resultado final de todos os usuários que ficaram ativos durante todo o período
    lista_resultado = []

    # Com base na quantidade de elementos de uma linha na matriz é possível calcular a quantidade de servidores ativos. 
    qtd_servidores_ativos = int(round(len(lista_t[0]) / umax, 0))
    # Criando a lista de custo
    lista_custo = [0 for i in range(qtd_servidores_ativos)]

    # Percorrendo cada linha da matriz transposta
    for i in range(len(lista_t)):

        resultado_linha = [] # Lista que armazena o resultando de quantos usuários estão ativos em cada linha
        contador = 0 # Quantidade de usuários ativos em cada servidor
        k = 0 # Iterador por servidor em cada linha
        c = 0 # Iterador para calcular o custo
        flag_c = True # Flag para confirmar se o servidor está ativo e já foi contado na soma do custo 

        # Percorrendo cada elemento da linha atual
        for j in range(len(lista_t[i])):
            if lista_t[i][j] == 1: # Se a célula atual for igual 1, então há usuário ativo
                contador += 1
                
                if flag_c: # Se a flag for verdade, então a lista de custo recebe mais um
                    lista_custo[c] += 1
                    flag_c = False # Seta a flag como falso, porque a partir daqui o servidor atual já foi considerado na lista de custo 
            
            if k < umax - 1: # Se k for menor umax - 1, então estamos no mesmo servidor 
                k += 1
            else: # Se não, se trata de um novo servidor
                if contador != 0: # Se o contador for diferente de zero, então armazena o resultado na lista de usuários ativos por linha 
                    resultado_linha.append(contador)
                k = 0 # Zera o k e o contador porque vamos para outro servidor
                contador =0 
                c += 1
                flag_c = True # Flag de custo recebe True para poder somar o custo do novo servidor.
                
        lista_resultado.append(resultado_linha) # Resultado final recebe o resultado da linha

    lista_resultado.extend([[sum(lista_custo)]]) # Armazena a soma total da lista de custo por servidores na lista de resultado final

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


