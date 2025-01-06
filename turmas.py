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

def consultar_disciplinas_alocadas_em_turma(turmas):
    """Consulta as disciplinas alocadas em uma turma."""
    if not turmas:
        print("Nenhuma turma cadastrada.")
        return

    print("Turmas disponíveis:")
    for i, turma in enumerate(turmas):
        print(f"{i + 1} - {turma['nome']} (Código: {turma['codigo']})")
    turma_escolhida = int(input("Escolha uma turma (número): ")) - 1

    turma = turmas[turma_escolhida]
    if turma["disciplinas"]:
        print(f"Disciplinas alocadas na turma {turma['nome']}:")
        for disciplina in turma["disciplinas"]:
            print(f"- {disciplina['nome']} (Código: {disciplina['codigo']})")
    else:
        print(f"Não há disciplinas alocadas na turma {turma['nome']}.")

