def gerar_codigo_turma(turmas):
    """Gera um código único para a turma, baseado em um número sequencial."""
    numero = len(turmas) + 1  # Incrementa 1 para gerar um código sequencial
    codigo = f"TUR{numero:03}"  # Formata o código com 3 dígitos 
    return codigo


def cadastrar_turma(turmas, professores):
    """Cadastra uma nova turma no sistema."""
    nome = input("Nome da turma: ")

    codigo = gerar_codigo_turma(turmas)

    if not professores:
        print("Nenhum professor cadastrado. Cadastre um professor antes de continuar.")
        return

    print("Escolha um professor para a turma:")
    for i, professor in enumerate(professores):
        print(f"{i + 1} - {professor['nome']}")

    while True:
        try:
            professor_escolhido = int(input("Escolha um professor (número): ")) - 1
            if 0 <= professor_escolhido < len(professores):
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, escolha um número válido.")

    turma = {
        "nome": nome,
        "codigo": codigo,
        "professor": professores[professor_escolhido],
        "disciplinas": [],
        "alunos": []
    }
    turmas.append(turma)
    print(f"Turma '{nome}' cadastrada com sucesso! Código: {codigo}")


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
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("Alunos disponíveis para matrícula:")
    for i, aluno in enumerate(alunos):
        print(f"{i + 1} - {aluno['nome']}")

    while True:
        try:
            aluno_escolhido = int(input("Escolha o aluno para matrícula (número): ")) - 1
            if 0 <= aluno_escolhido < len(alunos):
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, escolha um número válido.")

    if not turmas:
        print("Nenhuma turma cadastrada.")
        return

    print("Turmas disponíveis para matrícula:")
    for i, turma in enumerate(turmas):
        print(f"{i + 1} - {turma['nome']}")

    while True:
        try:
            turma_escolhida = int(input("Escolha a turma para matrícula (número): ")) - 1
            if 0 <= turma_escolhida < len(turmas):
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, escolha um número válido.")

    turmas[turma_escolhida]['alunos'].append(alunos[aluno_escolhido])
    print(f"Aluno {alunos[aluno_escolhido]['nome']} matriculado na turma {turmas[turma_escolhida]['nome']}!")

def alocar_disciplina_em_turma(turmas, disciplinas):
    """Aloca uma disciplina a uma turma."""
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return

    print("Disciplinas disponíveis para alocação:")
    for i, disciplina in enumerate(disciplinas):
        print(f"{i + 1} - {disciplina['nome']}")

    while True:
        try:
            disciplina_escolhida = int(input("Escolha a disciplina para alocação (número): ")) - 1
            if 0 <= disciplina_escolhida < len(disciplinas):
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, escolha um número válido.")

    if not turmas:
        print("Nenhuma turma cadastrada.")
        return

    print("Turmas disponíveis para alocação de disciplina:")
    for i, turma in enumerate(turmas):
        print(f"{i + 1} - {turma['nome']}")

    while True:
        try:
            turma_escolhida = int(input("Escolha a turma para alocar a disciplina (número): ")) - 1
            if 0 <= turma_escolhida < len(turmas):
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, escolha um número válido.")

    turmas[turma_escolhida]['disciplinas'].append(disciplinas[disciplina_escolhida])
    print(f"Disciplina {disciplinas[disciplina_escolhida]['nome']} alocada à turma {turmas[turma_escolhida]['nome']}!")


def consultar_disciplinas_alocadas_em_turma(turmas):
    
    if not turmas:
        print("Nenhuma turma cadastrada.")
        return

    print("Turmas disponíveis para consulta de disciplinas:")
    for i, turma in enumerate(turmas):
        print(f"{i + 1} - {turma['nome']}")

    while True:
        try:
            turma_escolhida = int(input("Escolha a turma para consultar disciplinas (número): ")) - 1
            if 0 <= turma_escolhida < len(turmas):
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, escolha um número válido.")

    if turmas[turma_escolhida]['disciplinas']:
        print("Disciplinas alocadas:")
        for disciplina in turmas[turma_escolhida]['disciplinas']:
            print(f"- {disciplina['nome']}")
    else:
        print("Nenhuma disciplina alocada nesta turma.")


def alunos_matriculados_em_turma(turmas):
    
    if not turmas:
        print("Nenhuma turma cadastrada.")
        return

    print("Turmas disponíveis para consulta de alunos matriculados:")
    for i, turma in enumerate(turmas):
        print(f"{i + 1} - {turma['nome']}")

    while True:
        try:
            turma_escolhida = int(input("Escolha a turma para consultar alunos (número): ")) - 1
            if 0 <= turma_escolhida < len(turmas):
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, escolha um número válido.")

    if turmas[turma_escolhida]['alunos']:
        print("Alunos matriculados:")
        for aluno in turmas[turma_escolhida]['alunos']:
            print(f"- {aluno['nome']}")
    else:
        print("Nenhum aluno matriculado nesta turma.")
