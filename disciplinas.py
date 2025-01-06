def cadastrar_disciplina(disciplinas, professores):
    nome = input("Nome da disciplina: ")
    codigo = input("Código da disciplina: ")
    carga_horaria = int(input("Carga horária: "))

    if not professores:
        print("Nenhum professor cadastrado. Cadastre um professor antes de continuar.")
        return

    print("Escolha o professor para a disciplina:")
    for i, p in enumerate(professores):
        print(f"{i + 1} - {p['nome']}")
    professor_escolhido = int(input("Digite o número do professor: ")) - 1

    if not (0 <= professor_escolhido < len(professores)):
        print("Professor inválido. Operação cancelada.")
        return

    disciplina = {
        "nome": nome,
        "codigo": codigo,
        "carga_horaria": carga_horaria,
        "professor": professores[professor_escolhido]
    }
    disciplinas.append(disciplina)
    print(f"Disciplina {nome} cadastrada com sucesso!")

def alocar_disciplina_em_turma(turmas, disciplinas):
    if not turmas:
        print("Nenhuma turma cadastrada.")
        return
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return

    codigo_turma = input("Digite o código da turma para alocar disciplinas: ")

    turma = next((t for t in turmas if t['codigo'] == codigo_turma), None)
    if turma:
        print("Escolha as disciplinas para a turma:")
        for i, d in enumerate(disciplinas):
            print(f"{i + 1} - {d['nome']}")
        try:
            disciplinas_escolhidas = list(map(int, input("Digite os números das disciplinas (separados por espaço): ").split()))
        except ValueError:
            print("Entrada inválida. Por favor, insira números separados por espaço.")
            return

        turma['disciplinas'] = [disciplinas[i - 1] for i in disciplinas_escolhidas if 0 <= i - 1 < len(disciplinas)]
        print(f"Disciplinas alocadas na turma {turma['nome']} com sucesso!")
    else:
        print("Turma não encontrada!")

def alocar_professor_em_disciplinas(disciplinas, professores):
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return
    if not professores:
        print("Nenhum professor cadastrado.")
        return

    print("\nDisciplinas disponíveis:")
    for i, d in enumerate(disciplinas):
        print(f"{i + 1} - {d['nome']}")

    try:
        escolha_disciplina = int(input("Escolha uma disciplina pelo número: ")) - 1
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return

    if not (0 <= escolha_disciplina < len(disciplinas)):
        print("Disciplina inválida. Operação cancelada.")
        return

    print("\nProfessores disponíveis:")
    for i, p in enumerate(professores):
        print(f"{i + 1} - {p['nome']}")

    try:
        escolha_professor = int(input("Escolha um professor pelo número: ")) - 1
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return

    if not (0 <= escolha_professor < len(professores)):
        print("Professor inválido. Operação cancelada.")
        return

    disciplinas[escolha_disciplina]['professor'] = professores[escolha_professor]
    print(f"Professor {professores[escolha_professor]['nome']} alocado na disciplina {disciplinas[escolha_disciplina]['nome']}.")

