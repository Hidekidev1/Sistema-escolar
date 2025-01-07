def gerar_codigo_turma(turmas):
    
    numero = len(turmas) + 1  
    codigo = f"TUR{numero:03}"  
    return codigo

def cadastrar_turma(turmas, professores):
    
    nome = input("Nome da turma: ")
    
    
    codigo = gerar_codigo_turma(turmas)

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
    print(f"Turma {nome} cadastrada com sucesso! Código: {codigo}")

def listar_turmas(turmas):
    
    if not turmas:
        print("Nenhuma turma cadastrada.")
        return
    
    print("Turmas cadastradas:")
    for turma in turmas:
        print(f"Nome: {turma['nome']}, Código: {turma['codigo']}")
