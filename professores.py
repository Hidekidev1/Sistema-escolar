def cadastrar_professor(professores):
    nome = input("Nome do professor: ")
    matricula = input("Matrícula do professor: ")
    data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
    sexo = input("Sexo (M/F): ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    professor = {
        "nome": nome,
        "matricula": matricula,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email
    }
    professores.append(professor)
    print(f"Professor {nome} cadastrado com sucesso!")

def consultar_professores_por_disciplina(disciplinas, professores):
    nome_disciplina = input("Digite o nome da disciplina para filtrar os professores: ")

    disciplina = next((d for d in disciplinas if d['nome'] == nome_disciplina), None)
    if disciplina:
        print(f"Professores alocados na disciplina {nome_disciplina}:")
        print(f"Professor: {disciplina['professor']['nome']}")
    else:
        print("Disciplina não encontrada!")
