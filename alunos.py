import random

def gerar_matricula(alunos):
    
    while True:
        matricula = str(random.randint(100000, 999999))
        if all(aluno['matricula'] != matricula for aluno in alunos):
            return matricula

def cadastrar_aluno(alunos, disciplinas):
    
    nome = input("Nome do aluno: ")
    data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
    sexo = input("Sexo (M/F): ").upper()
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    matricula = gerar_matricula(alunos)

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "disciplinas": []
    }
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso! Matrícula: {matricula}")

def listar_alunos(alunos):
    
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    print("Alunos cadastrados:")
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}")
