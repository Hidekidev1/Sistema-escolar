def cadastrar_turma(turmas, disciplinas, professores):
    """Cadastra uma nova turma no sistema."""
    nome = input("Nome da turma: ")
    codigo = input("Código da turma: ")

    print("Escolha um professor para a turma:")
    for i, professor in enumerate(professores):
        print(f"{i + 1} - {professor['nome']}")
    professor_escolhido = int(input("Escolha um professor (número): ")) - 1

    turma = {
        "nome": nome,
        "codigo": codigo,
        "professor": professores[professor_escolhido],
        "disciplinas": [],
        "alunos": []
    }
    turmas.append(turma)
    print(f"Turma {nome} cadastrada com sucesso!")

def listar_turmas(turmas):
    """Lista todas as turmas cadastradas."""
    if not turmas:
        print("Nenhuma turma cadastrada.")
        return
    
    print("Turmas cadastradas:")
    for turma in turmas:
        print(f"Nome: {turma['nome']}, Código: {turma['codigo']}")

def matricular_aluno(turmas, alunos):
    """Matrícula um aluno em uma turma."""  
    # Exibir lista de alunos
    print("Alunos disponíveis para matrícula:")
    for i, aluno in enumerate(alunos):
        print(f"{i + 1} - {aluno['nome']}")
    
    aluno_escolhido = int(input("Escolha o aluno para matrícula (número): ")) - 1
    
    # Exibir lista de turmas
    print("Turmas disponíveis para matrícula:")
    for i, turma in enumerate(turmas):
        print(f"{i + 1} - {turma['nome']}")
    
    turma_escolhida = int(input("Escolha a turma para matrícula (número): ")) - 1
    
    # Matrícula o aluno na turma escolhida
    turmas[turma_escolhida]['alunos'].append(alunos[aluno_escolhido])
    print(f"Aluno {alunos[aluno_escolhido]['nome']} matriculado na turma {turmas[turma_escolhida]['nome']} com sucesso!")
