def gerar_matricula_professor(professores):
    
    numero = len(professores) + 1  
    matricula = f"PROF{numero:03}"  
    return matricula

def cadastrar_professor(professores):
    
    nome = input("Nome do professor: ")
    
    
    matricula = gerar_matricula_professor(professores)

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
        "email": email,
        "disciplinas": []  # Lista de disciplinas que o professor leciona
    }
    professores.append(professor)
    print(f"Professor {nome} cadastrado com sucesso! Matrícula: {matricula}")

def listar_professores(professores):
    
    if not professores:
        print("Nenhum professor cadastrado.")
        return
    
    print("Professores cadastrados:")
    for professor in professores:
        print(f"Nome: {professor['nome']}, Matrícula: {professor['matricula']}")
        if professor['disciplinas']:
            print(f"Disciplinas: {', '.join([disciplina['nome'] for disciplina in professor['disciplinas']])}")
        else:
            print("Não leciona disciplinas.")
