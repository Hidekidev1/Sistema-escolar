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

def listar_professores(professores):
    
    if not professores:
        print("Nenhum professor cadastrado.")
        return
    
    print("Professores cadastrados:")
    for professor in professores:
        print(f"Nome: {professor['nome']}, Matrícula: {professor['matricula']}")
