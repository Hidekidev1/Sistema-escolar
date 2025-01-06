def cadastrar_professor(professores):
    """Cadastra um novo professor no sistema."""
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
    """Consulta professores que lecionam uma disciplina específica."""
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return

    print("Disciplinas disponíveis:")
    for i, disciplina in enumerate(disciplinas):
        print(f"{i + 1} - {disciplina['nome']} (Código: {disciplina['codigo']})")
    disciplina_escolhida = int(input("Escolha uma disciplina (número): ")) - 1

    disciplina = disciplinas[disciplina_escolhida]
    professor = disciplina["professor"]

    print(f"O professor responsável pela disciplina {disciplina['nome']} é {professor['nome']}.")

