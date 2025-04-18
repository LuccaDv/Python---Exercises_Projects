# Importação de módulos
from datetime  import datetime # Módulo de data

# Variáveis da identificação da criança
nome_crianca = ""
dia = ""
mes = ""
ano = ""
data_nascimento = ""
municipio = ""
mae = ""
pai = ""
telefone = ""
etnia = "" #Número da etnia escolhida que depois será traduziad na relação do dicioário 'etnias'
etnia_escolhida = "" #Etnia escolhida na lista apresentada do dicionário

# Variáveis de endereço
logradouro = ""
numeroCasa = ""
complemento = ""
bairro = ""
cidade = ""
cep = ""
estado = ""

# Apresentação do programa
print("Bem-vindo a Carteira de Saúde da Criança \n")

while True:
    print("\nMenu de opções:")
    print("a. Incluir os dados de identificação da criança")
    print("b. Incluir o endereço da criança")
    print("c. Incluir o registro de vacina da criança")
    print("d. Listar todos os dados da CSC")
    print("e. Sair do programa")

    # Recebe a escolha do usuário e armazena em uma variável
    opcoes = input("\nEscolha uma das opções abaixo em nosso menu: ").lower()

    # Bloco de execução para caso a escolha seja a 'a'
    if opcoes == "a":
        print("\nIdentificação da criança")
        print("Por gentileza, preencha os seguintes dados:\n")
        nome_crianca = input("Nome da criança: ")
        while True:
                try:
                    ano = int(input("Ano de nascimento (ex: 2015): "))
                    mes = int(input("Mês de nascimento (1 a 12): "))
                    dia = int(input("Dia de nascimento (1 a 31): "))
                    data_nascimento = datetime(ano, mes, dia).date()
                    break
                except ValueError:
                    print("\nData inválida. Por favor, digite novamente.\n")
        mae = input("Nome da mãe: ")
        pai = input("Nome do pai: ")
        telefone = input("Telefone para contato (Apenas números): ")
        etnias = {
            1: "Branca",
            2: "Negra",
            3: "Amarela",
            4: "Parda",
            5: "Indígena"
        }
        while True:
            try:
                etnia = int(input("Etnia (1)Branca (2)Negra (3)Amarela (4)Parda (5)Índigena: "))
                if etnia in etnias:
                    etnia_escolhida = etnias[etnia]
                    break
                else:
                    print("\nEscolha uma opção válida de 1 a 5.")
            except ValueError:
                print("\nEntrada inválida. Digite apenas números de 1 a 5.")

    # Bloco de execução para caso a escolha seja a 'b'  
    elif opcoes == "b":
        print("\nEndereço da criança:\n")
        logradouro = input("Digite o logradouro: ")
        numeroCasa = input("Digite o número: ")
        complemento = input("Digite o complemento: ")
        bairro = input("Digite o bairro: ")
        cidade = input("Digite a cidade: ")
        cep = input("Digite o cep: ")
        estado = input("Digite o estado: ")

    # Bloco de execução para caso a escolha seja a 'c'
    elif opcoes == "c":
        print(3)

    # Bloco de execução para caso a escolha seja a 'd'
    elif opcoes == "d":
        print("Carteira de Saúde da Criança")
        print("\nInformações da criança:\n")
        print(f'Nome da criança: {nome_crianca}')
        print(f'Data de nascimento: {data_nascimento}')
        print(f'Nome da mãe: {mae}')
        print(f'Nome do pai: {pai}')
        print(f'Telefone para contato: {telefone}')
        print(f'Etnia: {etnia_escolhida}')
        print(f'\nEndereço da criança: {logradouro}, {numeroCasa}, {bairro}')
        print(f'{complemento}, - {cep}')
        print(f'{cidade}, - {estado}')

    # Bloco de execução para caso a escolha seja a 'e'
    elif opcoes == "e":
        print("Fim da execução do programa!")
        break

    # Caso nenhuma das opções seja escolhida
    else:
        print("\nNenhuma das opções foi escolhida")

"""
Nascer = BCG ID (Única) / Hepatite B (1ª Dose)
1 mês = Hepatite B (2ª Dose)
2 meses = Tetravalente (1ª e 2ª) / VOP (1ª e 2ª) / VORH (1ª)
4 meses = VORH (2ª)
"""

# ---Pendências---
# Critérios pela idade
# Expôr vacinas pela idade

# ---Melhorias---
# Fazer loop voltar ao menu apenas se desejado pelo usuário
# Não exibir dados se incompleto
# Melhorar o recolhimento de dados (Não permitir ano vazio ou mês que não exista)