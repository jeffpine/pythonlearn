import json
from time import localtime,sleep

try:
    with open('./turmas.json','r') as json_file:
        turmas = json.load(json_file)
except FileNotFoundError:
    turmas = {}
    print("Arquivo 'turmas.json' não encontrado.Iniciando com turmas vazias")

numero_da_turma = 0
    
def exibir_menu(): # função para exibição do menu
    print("=="*15)
    print("Bem vindo a sala de aula")
    print("=="*15)
    print("1. Cadastrar aluno")
    print("2. Lista de presença")
    print("3. Lançar nota")
    print("4. sair")
    print("=="*15)


def cadastrar_aluno(): #função para cadastrar alunos
    print("=="*15)
    print("Abrindo sistema de cadastro")
    sleep(2)
    print("Iniciando sistema")
    print("=="*15)
    sleep(2)
    
    Nome = input("Digite o nome do aluno: ")
    print("Adicionando Nome")
    sleep(2)
    print("nome adicionado com sucesso")
    print("=="*15)
    sleep(2)
    telefone = input("Digite o telefone do aluno: ")
    print("Adicionando telefone")
    sleep(2)
    print("telefone adicionado com sucesso!")
    sleep(2)
    
    
    novo_aluno = {"nome": Nome, "telefone": telefone}
    
    if f'turma_{numero_da_turma}' not in turmas:
        turmas[f'turma_{numero_da_turma}'] = [novo_aluno]
    else:
        turmas[f'turma_{numero_da_turma}'].append(novo_aluno)
        
    print("Aluno cadastrado!")

def lista_de_presença(): #função para verificação de presença
                        #logica para função EM CONSTRUÇÃO
    print(" ")
    
def lancar_nota(): #função para lancar nota
    #AINDA EM CONSTRUÇÃO
    av1 = int(input("Nota AV1: "))
    sleep(2)
    print("Nota lançada")
    av2 = int(input("Nota AV2: "))
    sleep(2)
    print("Nota lançada")
    av3 = int(input("Nota AV3: "))
    sleep(2)
    print("Nota lançada")
    
    Media = ((av1+av2+av3)/3)
    
    if Media > ("6"):
        print("Aluno aprovado!")
    elif Media == ("4","5"):
        print("Aluno em recuperação")
    else:
        print("Aluno reprovado")
    
    


while True:
        exibir_menu()
        
        Opção = input("Escolha uma opção: ")
        if Opção == "1":
            cadastrar_aluno()
        elif Opção == "2":
            lista_de_presença()
        elif Opção == "3":
            lancar_nota()
        elif Opção == "4":
            with open('./turmas.json', 'w') as json_file:
                json.dump(turmas, json_file, indent=4)
            print("dados salvos em 'turmas.json'.")
            break
        else:
            print("Opção Invalida. Tente novamente")
            