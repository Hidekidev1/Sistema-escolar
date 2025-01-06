# turmas.py

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
