# Listas e dicionários para armazenar os dados
alunos = []
professores = []
disciplinas = []
notas = {}

# Função para cadastrar um aluno
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")
    alunos.append((nome, matricula))
    print(f"Aluno {nome} cadastrado com sucesso!")

# Função para cadastrar um professor
def cadastrar_professor():
    nome = input("Digite o nome do professor: ")
    professores.append(nome)
    print(f"Professor {nome} cadastrado com sucesso!")

# Função para cadastrar uma disciplina
def cadastrar_disciplina():
    nome = input("Digite o nome da disciplina: ")
    disciplinas.append(nome)
    print(f"Disciplina {nome} cadastrada com sucesso!")

# Função para matricular um aluno em uma disciplina
def matricular_aluno():
    nome_aluno = input("Digite o nome do aluno para matrícula: ")
    nome_disciplina = input("Digite o nome da disciplina: ")
    
    # Verificar se o aluno e a disciplina existem
    if nome_aluno not in [aluno[0] for aluno in alunos]:
        print("Aluno não encontrado.")
        return
    if nome_disciplina not in disciplinas:
        print("Disciplina não encontrada.")
        return
    
    if nome_aluno not in notas:
        notas[nome_aluno] = {}
    notas[nome_aluno][nome_disciplina] = None  # Inicializa a nota como None
    print(f"Aluno {nome_aluno} matriculado na disciplina {nome_disciplina} com sucesso!")

# Função para registrar a nota de um aluno em uma disciplina
def registrar_nota():
    nome_aluno = input("Digite o nome do aluno: ")
    nome_disciplina = input("Digite o nome da disciplina: ")
    
    # Verificar se o aluno está matriculado na disciplina
    if nome_aluno not in notas or nome_disciplina not in notas[nome_aluno]:
        print(f"Aluno {nome_aluno} não matriculado na disciplina {nome_disciplina}.")
        return
    
    try:
        nota = float(input("Digite a nota do aluno: "))
        notas[nome_aluno][nome_disciplina] = nota
        print(f"Nota registrada com sucesso para {nome_aluno} em {nome_disciplina}: {nota}")
    except ValueError:
        print("Erro: A nota deve ser um número.")

# Função para exibir as notas de um aluno
def exibir_notas():
    nome_aluno = input("Digite o nome do aluno: ")
    if nome_aluno in notas:
        print(f"Notas de {nome_aluno}:")
        for disciplina, nota in notas[nome_aluno].items():
            print(f"{disciplina}: {nota if nota is not None else 'Sem nota'}")
    else:
        print(f"Aluno {nome_aluno} não encontrado.")

# Função para listar todos os alunos
def listar_alunos():
    print("Lista de Alunos:")
    if alunos:
        for nome, matricula in alunos:
            print(f"Nome: {nome}, Matrícula: {matricula}")
    else:
        print("Nenhum aluno cadastrado.")

# Função para listar todos os professores
def listar_professores():
    print("Lista de Professores:")
    if professores:
        for professor in professores:
            print(f"Professor: {professor}")
    else:
        print("Nenhum professor cadastrado.")

# Função para listar todas as disciplinas
def listar_disciplinas():
    print("Lista de Disciplinas:")
    if disciplinas:
        for disciplina in disciplinas:
            print(f"Disciplina: {disciplina}")
    else:
        print("Nenhuma disciplina cadastrada.")

# Função para exibir o menu
def exibir_menu():
    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar aluno")
        print("2. Cadastrar professor")
        print("3. Cadastrar disciplina")
        print("4. Matricular aluno em disciplina")
        print("5. Registrar nota")
        print("6. Exibir notas de um aluno")
        print("7. Listar alunos")
        print("8. Listar professores")
        print("9. Listar disciplinas")
        print("10. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_aluno()
        elif escolha == "2":
            cadastrar_professor()
        elif escolha == "3":
            cadastrar_disciplina()
        elif escolha == "4":
            matricular_aluno()
        elif escolha == "5":
            registrar_nota()
        elif escolha == "6":
            exibir_notas()
        elif escolha == "7":
            listar_alunos()
        elif escolha == "8":
            listar_professores()
        elif escolha == "9":
            listar_disciplinas()
        elif escolha == "10":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamada inicial para exibir o menu
exibir_menu()
