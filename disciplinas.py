def gerar_codigo_disciplina(disciplinas):
    
    numero = len(disciplinas) + 1  
    codigo = f"D{numero:03}"  
    return codigo

def cadastrar_disciplina(disciplinas, professores):
    
    nome = input("Nome da disciplina: ")
    
    # Gerar código automático para a disciplina
    codigo = gerar_codigo_disciplina(disciplinas)

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
    
    # Adiciona a disciplina à lista de disciplinas do professor
    professores[professor_escolhido]['disciplinas'].append(disciplina)

    disciplinas.append(disciplina)
    print(f"Disciplina {nome} cadastrada com sucesso!")
