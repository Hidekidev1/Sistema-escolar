def cadastrar_disciplina(disciplinas, professores):
    nome = input("Nome da disciplina: ")
    codigo = input("Código da disciplina: ")
    carga_horaria = int(input("Carga horária: "))

    print("Escolha o professor para a disciplina:")
    for i, p in enumerate(professores):
        print(f"{i + 1} - {p['nome']}")
    professor_escolhido = int(input("Digite o número do professor: ")) - 1

    disciplina = {
        "nome": nome,
        "codigo": codigo,
        "carga_horaria": carga_horaria,
        "professor": professores[professor_escolhido]
    }
    disciplinas.append(disciplina)
    print(f"Disciplina {nome} cadastrada com sucesso!")

def alocar_disciplina_em_turma(turmas, disciplinas):
    codigo_turma = input("Digite o código da turma para alocar disciplinas: ")

    turma = next((t for t in turmas if t['codigo'] == codigo_turma), None)
    if turma:
        print("Escolha as disciplinas para a turma:")
        for i, d in enumerate(disciplinas):
            print(f"{i + 1} - {d['nome']}")
        disciplinas_escolhidas = list(map(int, input("Digite os números das disciplinas (separados por espaço): ").split()))

        turma['disciplinas'] = [disciplinas[i - 1] for i in disciplinas_escolhidas]
        print(f"Disciplinas alocadas na turma {turma['nome']} com sucesso!")
    else:
        print("Turma não encontrada!")
