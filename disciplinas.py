def gerar_codigo_disciplina(disciplinas):
    
    numero = len(disciplinas) + 1
    codigo = f"D{numero:03}"
    return codigo

def cadastrar_disciplina(disciplinas, professores):
    
    nome = input("Nome da disciplina: ")

    # Gerar código automático para a disciplina
    codigo = gerar_codigo_disciplina(disciplinas)

    # Solicita a carga horária da disciplina
    carga_horaria = int(input("Carga horária (em horas): "))

    if not professores:
        print("Nenhum professor cadastrado. Cadastre um professor antes de continuar.")
        return

    # Exibe a lista de professores e solicita a escolha
    print("Professores disponíveis:")
    for i, professor in enumerate(professores):
        print(f"{i + 1} - {professor['nome']}")

    while True:
        try:
            professor_escolhido = int(input("Escolha um professor para a disciplina (número): ")) - 1
            if 0 <= professor_escolhido < len(professores):
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, escolha um número válido.")

    # Cria a disciplina e a associa ao professor escolhido
    disciplina = {
        "nome": nome,
        "codigo": codigo,
        "carga_horaria": carga_horaria,
        "professor": professores[professor_escolhido]
    }

    # Adiciona a disciplina à lista de disciplinas do professor
    professores[professor_escolhido]['disciplinas'].append(disciplina)

    # Adiciona a disciplina à lista de disciplinas
    disciplinas.append(disciplina)
    print(f"Disciplina {nome} cadastrada com sucesso!")

def listar_disciplinas(disciplinas):
    
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return

    print("Disciplinas cadastradas:")
    for disciplina in disciplinas:
        print(f"Nome: {disciplina['nome']}, Código: {disciplina['codigo']}, Carga Horária: {disciplina['carga_horaria']} horas")

def consultar_professores_por_disciplina(disciplinas, professores):
    
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return

    print("Disciplinas disponíveis para consulta:")
    for i, disciplina in enumerate(disciplinas):
        print(f"{i + 1} - {disciplina['nome']}")

    while True:
        try:
            disciplina_escolhida = int(input("Escolha a disciplina (número): ")) - 1
            if 0 <= disciplina_escolhida < len(disciplinas):
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, escolha um número válido.")

    disciplina = disciplinas[disciplina_escolhida]
    print(f"Professores que lecionam a disciplina {disciplina['nome']}:")
    for professor in professores:
        if disciplina['codigo'] in [d['codigo'] for d in professor['disciplinas']]:
            print(f"- {professor['nome']}")
