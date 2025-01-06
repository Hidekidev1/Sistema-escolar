def cadastrar_aluno(alunos, disciplinas):
    nome = input("Nome do aluno: ")
    matricula = input("Matrícula do aluno: ")
    data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
    sexo = input("Sexo (M/F): ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    print("Escolha a disciplina do aluno:")
    for i, d in enumerate(disciplinas):
        print(f"{i + 1} - {d['nome']}")
    disciplina_escolhida = int(input("Digite o número da disciplina: ")) - 1
    
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "disciplina": disciplinas[disciplina_escolhida]['nome']
    }
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")

def matricular_aluno(turmas, alunos):
    matricula_aluno = input("Digite a matrícula do aluno para matricular: ")
    codigo_turma = input("Digite o código da turma para matrícula: ")
    
    aluno = next((a for a in alunos if a['matricula'] == matricula_aluno), None)
    turma = next((t for t in turmas if t['codigo'] == codigo_turma), None)
    
    if aluno and turma:
        turma['alunos'].append(aluno)
        print(f"Aluno {aluno['nome']} matriculado na turma {turma['nome']} com sucesso!")
    else:
        print("Aluno ou turma não encontrado!")

