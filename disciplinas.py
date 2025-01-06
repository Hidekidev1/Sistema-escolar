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

def alocar_professor_em_disciplina(disciplinas, professores):
    nome_disciplina = input("Digite o nome da disciplina: ")
    
    disciplina = next((d for d in disciplinas if d['nome'] == nome_disciplina), None)
    if disciplina:
        print("Escolha o novo professor para a disciplina:")
        for i, p in enumerate(professores):
            print(f"{i + 1} - {p['nome']}")
        professor_escolhido = int(input("Digite o número do professor: ")) - 1
        disciplina['professor'] = professores[professor_escolhido]
        print(f"Professor {professores[professor_escolhido]['nome']} alocado na disciplina {nome_disciplina} com sucesso!")
    else:
        print("Disciplina não encontrada!")

