import random

def gerar_matricula(alunos):
    """Gera um número de matrícula único e aleatório com 6 dígitos."""
    while True:
        matricula = str(random.randint(100000, 999999))
        if all(aluno['matricula'] != matricula for aluno in alunos):
            return matricula

def cadastrar_aluno(alunos, disciplinas):
    """Cadastra um novo aluno no sistema."""
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

def matricular_aluno(turmas, alunos):
    """Matricula um aluno em uma turma."""
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    if not turmas:
        print("Nenhuma turma cadastrada.")
        return
    
    print("Alunos disponíveis:")
    for i, aluno in enumerate(alunos):
        print(f"{i + 1} - {aluno['nome']} (Matrícula: {aluno['matricula']})")
    aluno_escolhido = int(input("Escolha um aluno (número): ")) - 1

    print("Turmas disponíveis:")
    for i, turma in enumerate(turmas):
        print(f"{i + 1} - {turma['nome']} (Código: {turma['codigo']})")
    turma_escolhida = int(input("Escolha uma turma (número): ")) - 1

    aluno = alunos[aluno_escolhido]
    turma = turmas[turma_escolhida]

    turma["alunos"].append(aluno)
    aluno["disciplinas"].extend(turma["disciplinas"])
    print(f"Aluno {aluno['nome']} matriculado na turma {turma['nome']} com sucesso!")

def alunos_matriculados_em_turma(turmas):
    """Exibe os alunos matriculados em uma turma."""
    if not turmas:
        print("Nenhuma turma cadastrada.")
        return
    
    print("Turmas disponíveis:")
    for i, turma in enumerate(turmas):
        print(f"{i + 1} - {turma['nome']} (Código: {turma['codigo']})")
    turma_escolhida = int(input("Escolha uma turma (número): ")) - 1

    turma = turmas[turma_escolhida]
    if turma["alunos"]:
        print(f"Alunos matriculados na turma {turma['nome']}:")
        for aluno in turma["alunos"]:
            print(f"- {aluno['nome']} (Matrícula: {aluno['matricula']})")
    else:
        print(f"Não há alunos matriculados na turma {turma['nome']}.")


