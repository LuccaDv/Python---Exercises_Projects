import random # Módulo do Python que permite gerar números aleatórios

sessao = 0 # Variável para contagem de sessões jogadas
acertos = 0 # Variável para contagem de sessões ganhas
erros = 0 # Variável para contagem de sessões perdidas
fimJogo = False # Variável para encerramento do jogo dentro do while

while fimJogo == False:

    # Apresentação do desafio
    print ("Tente adivinhar um número aleatório de 0 a 100\n")
    print ("Fácil: 10 tentativas \nMédio: 7 tentativas \nDifícil: 5 tentativas \nDesafiador: 3 tentativas")

    # Definição de variáveis
    numSecreto = random.randint(1, 100) #Número aleatório
    tentativa = 1 # Número da tentativa feita
    chances = 0 # Quantas tentativas o jogador terá

    declaracao = False # Teste de resposta da escolha da dificuldade

    # Seleção da dificuldade por parte do jogador

    while declaracao == False:
        dificuldade = str(input("\nQual o nível de dificuldade que você deseja? " ))
        if dificuldade.upper() == "FÁCIL":
            chances = 10
            declaracao = True
        elif dificuldade.upper() == "MÉDIO":
            chances = 7
            declaracao = True
        elif dificuldade.upper() == "DIFÍCIL":
            chances = 5
            declaracao = True
        elif dificuldade.upper() == "DESAFIADOR":
            chances = 3
            declaracao = True
        else:
            print("Tentativa não escolhida")

    faltam = chances # Tentativas restantes

    # Inicío das tentativas

    while tentativa <= chances:
        if faltam == 1:
            print("\nResta apenas uma chance")
        chute = int(input("\nDiga um número: "))
        if chute < numSecreto:
            print("O número é maior!")
        elif chute > numSecreto:
            print("O número é menor!")    
        else:
            print ("\nAcertou")
            print(f"Tentativas necessárias: {tentativa}")
            acertos += 1
            break
        faltam -= 1
        tentativa += 1
    else:
        print(f"\nFim das tentativas! O número secreto era {numSecreto}")
        erros += 1
    sessao += 1

    # Teste de continuidade
    resp = input("Deseja jogar novamente? [S] para Sim e [N] para Não ")

    while resp.upper() not in ['S', 'N']:
        resp = input("Não entendi a sua resposta. Deseja jogar novamente? [S] para Sim e [N] para Não ")
    if resp.upper() == 'N':
        fimJogo = True

# Resultado da sessão

if sessao == 1:
    print (f"\nFim do jogo. Você jogou uma rodada.")
else:
    print (f"\nFim do jogo. Foram jogadas {sessao} rodadas.")

if acertos == 0:
    print("Você não acertou nenhuma vez ", end="")
elif acertos == 1:
    print("Você acertou um número ", end="")
else:
    print(f"Você acertou {acertos} números", end="")

if erros == 0:
    print("e não perdeu em nenhuma rodada.")
elif erros == 1:
    print("e errou apenas uma rodada.")
else:
    print(f"e errou {erros} rodadas.")