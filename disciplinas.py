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
    
    while True:
        try:
            professor_escolhido = int(input("Escolha um professor para a disciplina (número): ")) - 1
            if 0 <= professor_escolhido < len(professores):
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, escolha um número válido.")
    
    disciplina = {
        "nome": nome,
        "codigo": codigo,
        "carga_horaria": carga_horaria,
        "professor": professores[professor_escolhido]
    }
    disciplinas.append(disciplina)
    print(f"Disciplina {nome} cadastrada com sucesso!")

def listar_disciplinas(disciplinas):
    """Lista todas as disciplinas cadastradas."""
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return
    
    print("Disciplinas cadastradas:")
    for disciplina in disciplinas:
        print(f"Nome: {disciplina['nome']}, Código: {disciplina['codigo']}")
