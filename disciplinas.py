def cadastrar_disciplina(disciplinas, professores):
    """Cadastra uma nova disciplina no sistema."""
    nome = input("Nome da disciplina: ")
    codigo = input("Código da disciplina: ")
    carga_horaria = int(input("Carga horária (em horas): "))

    if not professores:
        print("Nenhum professor cadastrado. Cadastre um professor antes de continuar.")
        return

    print("Professores disponíveis:")
    for i, professor in enumerate(professores):
        print(f"{i + 1} - {professor['nome']}")
    professor_escolhido = int(input("Escolha um professor para a disciplina (número): ")) - 1

    disciplina = {
        "nome": nome,
        "codigo": codigo,
        "carga_horaria": carga_horaria,
        "professor": professores[professor_escolhido]
    }
    disciplinas.append(disciplina)
    print(f"Disciplina {nome} cadastrada com sucesso!")

def alocar_disciplina_em_turma(turmas, disciplinas):
    """Aloca uma disciplina em uma turma."""
    if not turmas:
        print("Nenhuma turma cadastrada.")
        return
    
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return
    
    print("Turmas disponíveis:")
    for i, turma in enumerate(turmas):
        print(f"{i + 1} - {turma['nome']} (Código: {turma['codigo']})")
    turma_escolhida = int(input("Escolha uma turma (número): ")) - 1

    print("Disciplinas disponíveis:")
    for i, disciplina in enumerate(disciplinas):
        print(f"{i + 1} - {disciplina['nome']} (Código: {disciplina['codigo']})")
    disciplina_escolhida = int(input("Escolha uma disciplina (número): ")) - 1

    turma = turmas[turma_escolhida]
    disciplina = disciplinas[disciplina_escolhida]

    turma["disciplinas"].append(disciplina)
    print(f"Disciplina {disciplina['nome']} alocada na turma {turma['nome']} com sucesso!")


