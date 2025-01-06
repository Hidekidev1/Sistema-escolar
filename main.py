from alunos import cadastrar_aluno, matricular_aluno
from professores import cadastrar_professor
from disciplinas import cadastrar_disciplina, alocar_professor_em_disciplina
from turmas import cadastrar_turma, alunos_matriculados_em_turma

# Listas para armazenar as informações
professores = []
alunos = []
disciplinas = []
turmas = []

def main():
    while True:
        print("\nSistema de Gestão Escolar")
        print("1 - Cadastrar Professor")
        print("2 - Cadastrar Aluno")
        print("3 - Cadastrar Disciplina")
        print("4 - Cadastrar Turma")
        print("5 - Matrícula de Aluno em Turma")
        print("6 - Consultar Alunos Matriculados em Turma")
        print("7 - Alocar Professor em Disciplina")
        print("8 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_professor(professores)
        elif opcao == "2":
            cadastrar_aluno(alunos, disciplinas)
        elif opcao == "3":
            cadastrar_disciplina(disciplinas, professores)
        elif opcao == "4":
            cadastrar_turma(turmas, disciplinas, professores)
        elif opcao == "5":
            matricular_aluno(turmas, alunos)
        elif opcao == "6":
            alunos_matriculados_em_turma(turmas)
        elif opcao == "7":
            alocar_professor_em_disciplina(disciplinas, professores)
        elif opcao == "8":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
