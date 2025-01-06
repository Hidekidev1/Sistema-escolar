def cadastrar_turma(turmas, disciplinas, professores):
    nome = input("Nome da turma: ")
    codigo = input("Código da turma: ")
    
    print("Escolha os professores para a turma:")
    for i, p in enumerate(professores):
        print(f"{i + 1} - {p['nome']}")
    professor_escolhido = int(input("Digite o número do professor para a turma: ")) - 1
    
    print("Escolha as disciplinas para a turma:")
    for i, d in enumerate(disciplinas):
        print(f"{i + 1} - {d['nome']}")
    disciplinas_escolhidas = list(map(int, input("Digite os números das disciplinas (separados por espaço): ").split()))
    
    turma = {
        "nome": nome,
        "codigo": codigo,
        "disciplinas": [disciplinas[i - 1] for i in disciplinas_escolhidas],
        "professor": professores[professor_escolhido],
        "alunos": []
    }
    turmas.append(turma)
    print(f"Turma {nome} cadastrada com sucesso!")

def alunos_matriculados_em_turma(turmas):
    codigo_turma = input("Digite o código da turma para consultar os alunos: ")
    
    turma = next((t for t in turmas if t['codigo'] == codigo_turma), None)
    
    if turma:
        if turma['alunos']:
            print(f"Alunos matriculados na turma {turma['nome']}:")
            for aluno in turma['alunos']:
                print(aluno['nome'])
        else:
            print(f"Nenhum aluno matriculado na turma {turma['nome']}.")
    else:
        print("Turma não encontrada!")


    