# Função para calcular a média de uma lista de notas
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

# Lista para armazenar informações dos alunos
alunos = []

# Loop principal do programa
while True:
    # Menu principal
    print("\n1. Cadastrar novo aluno")
    print("2. Listar todos os alunos")
    print("3. Pesquisar por aluno")
    print("4. Estatísticas da turma")
    print("5. Sair")

    # Entrada do usuário para escolher uma opção
    opcao = input("\nDigite a opção desejada: ")

    if opcao == '1':
        # Opção para cadastrar um novo aluno
        nome = input("Digite o nome do aluno: ")
        quantidade_notas = int(input("Digite a quantidade de notas do aluno: "))
        notas = []
        for i in range(quantidade_notas):
            nota = float(input("Digite a nota {}: ".format(i+1)))
            notas.append(nota)
        media = calcular_media(notas)
        aluno = {"nome": nome, "notas": notas, "media": media}
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")
    elif opcao == '2':
        # Opção para listar todos os alunos cadastrados
        print("\nLista de todos os alunos cadastrados:")
        for aluno in alunos:
            print("Nome:", aluno["nome"])
            print("Notas:", aluno["notas"])
            print("Média:", aluno["media"])
            print()
    elif opcao == '3':
        # Opção para pesquisar por um aluno pelo nome
        nome_pesquisar = input("Digite o nome do aluno que deseja pesquisar: ")
        encontrado = False
        for aluno in alunos:
            if aluno["nome"].lower() == nome_pesquisar.lower():
                print("Aluno encontrado:")
                print("Nome:", aluno["nome"])
                print("Notas:", aluno["notas"])
                print("Média:", aluno["media"])
                encontrado = True
                break
        if not encontrado:
            print("Aluno não encontrado.")
    elif opcao == '4':
        # Opção para exibir estatísticas da turma
        if not alunos:
            print("Não há alunos cadastrados.")
            continue

        # Menu para escolher o tipo de estatística a ser visualizada
        print("\nEstatísticas da turma:")
        print("1. Média da turma")
        print("2. Nota mais alta")
        print("3. Nota mais baixa")
        print("4. Quantidade de alunos cadastrados")

        # Entrada do usuário para escolher uma opção de estatística
        opcao_estatistica = input("\nEscolha a estatística desejada (1-4): ")
        if opcao_estatistica == '1':
            # Calcular e exibir a média da turma
            medias = [aluno["media"] for aluno in alunos]
            media_turma = sum(medias) / len(medias)
            print("Média da turma:", media_turma)
        elif opcao_estatistica == '2':
            # Encontrar e exibir a nota mais alta da turma
            notas_turma = [nota for aluno in alunos for nota in aluno["notas"]]
            nota_mais_alta = max(notas_turma)
            print("Nota mais alta da turma:", nota_mais_alta)
        elif opcao_estatistica == '3':
            # Encontrar e exibir a nota mais baixa da turma
            notas_turma = [nota for aluno in alunos for nota in aluno["notas"]]
            nota_mais_baixa = min(notas_turma)
            print("Nota mais baixa da turma:", nota_mais_baixa)
        elif opcao_estatistica == '4':
            # Exibir a quantidade de alunos cadastrados
            quantidade_alunos = len(alunos)
            print("Quantidade de alunos cadastrados:", quantidade_alunos)
        else:
            print("Opção inválida.")
    elif opcao == '5':
        # Opção para sair do programa
        print("Saindo do programa...")
        break
    else:
        # Mensagem de opção inválida
        print("Opção inválida. Por favor, escolha uma opção válida.")