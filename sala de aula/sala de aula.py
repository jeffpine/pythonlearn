import json
from time import sleep
import pandas as pd


# Função para carregar os dados do arquivo JSON
def carregar_dados():
    try:
        with open('./turmas.json', 'r') as json_file:
            turmas = json.load(json_file)
    except FileNotFoundError:
        turmas = {}
        salvar_dados(turmas)  # Salva um arquivo vazio se não existir
        print("Arquivo 'turmas.json' não encontrado. Iniciando com turmas vazias.")
    return turmas


# Função para salvar os dados no arquivo JSON
def salvar_dados(turmas):
    with open('./turmas.json', 'w') as json_file:
        json.dump(turmas, json_file, indent=4)
    print("Dados salvos em 'turmas.json'.")


turmas = carregar_dados()


def exibir_menu():  # função para exibição do menu
    print("==" * 15)
    print("Bem vindo à sala de aula")
    print("==" * 15)
    print("1. Cadastrar aluno")
    print("2. Lista de presença")
    print("3. Lançar nota")
    print("4. Exportar para Excel")
    print("5. Sair")
    print("==" * 15)


def cadastrar_aluno():  # função para cadastrar alunos
    print("==" * 15)
    print("Abrindo sistema de cadastro")
    sleep(1)
    print("Iniciando sistema")
    print("==" * 15)
    sleep(1)

    nome = input("Digite o nome do aluno: ")
    print("Adicionando nome...")
    sleep(1)
    print("Nome adicionado com sucesso!")
    print("==" * 15)
    telefone = input("Digite o telefone do aluno: ")
    print("Adicionando telefone...")
    sleep(1)
    print("Telefone adicionado com sucesso!")

    novo_aluno = {"nome": nome, "telefone": telefone, "notas": []}

    numero_da_turma = input("Digite o número da turma: ")
    if f'turma_{numero_da_turma}' not in turmas:
        turmas[f'turma_{numero_da_turma}'] = [novo_aluno]
    else:
        turmas[f'turma_{numero_da_turma}'].append(novo_aluno)

    print("Aluno cadastrado!")
    salvar_dados(turmas)  # Salva os dados após cada cadastro


def lista_de_presença():  # função para verificação de presença
    numero_da_turma = input("Digite o número da turma: ")
    if f'turma_{numero_da_turma}' in turmas:
        print(f"Lista de presença da turma {numero_da_turma}:")
        for aluno in turmas[f'turma_{numero_da_turma}']:
            print(f"Nome: {aluno['nome']}, Telefone: {aluno['telefone']}")
    else:
        print("Turma não encontrada.")


def lancar_nota():  # função para lançar nota
    numero_da_turma = input("Digite o número da turma: ")
    if f'turma_{numero_da_turma}' in turmas:
        nome_aluno = input("Digite o nome do aluno: ")
        for aluno in turmas[f'turma_{numero_da_turma}']:
            if aluno['nome'] == nome_aluno:
                av1 = float(input("Nota AV1: "))
                av2 = float(input("Nota AV2: "))
                av3 = float(input("Nota AV3: "))

                media = (av1 + av2 + av3) / 3
                aluno['notas'] = [av1, av2, av3]

                print("Notas lançadas!")
                print(f"Média: {media:.2f}")

                if media >= 6:
                    print("Aluno aprovado!")
                elif 4 <= media < 6:
                    print("Aluno em recuperação.")
                else:
                    print("Aluno reprovado.")

                salvar_dados(turmas)  # Salva os dados após lançar as notas
                return
        print("Aluno não encontrado.")
    else:
        print("Turma não encontrada.")


def exportar_para_excel(turmas):
    lista_turmas = []
    for turma, alunos in turmas.items():
        for aluno in alunos:
            alunos_info = {
                "Turma": turma,
                "Nome": aluno["nome"],
                "Telefone": aluno["telefone"],
                "AV1": aluno["notas"][0] if len(aluno["notas"]) > 0 else None,
                "AV2": aluno["notas"][1] if len(aluno["notas"]) > 1 else None,
                "AV3": aluno["notas"][2] if len(aluno["notas"]) > 2 else None,
                "Média": sum(aluno["notas"]) / len(aluno["notas"]) if aluno["notas"] else None
            }
            lista_turmas.append(alunos_info)

            df = pd.DataFrame(lista_turmas)
            df.to_excel(r'C:\users\Jeff Pine\OneDrive\projetos\pythonlearn\sala de aula', index=False)
            print("Dados exportados para 'turmas.xlsx'.")


while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        lista_de_presença()
    elif opcao == "3":
        lancar_nota()
    elif opcao == "4":
        exportar_para_excel(turmas)
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
