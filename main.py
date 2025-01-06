from alunos import cadastrar_aluno, matricular_aluno, alunos_matriculados_em_turma
from professores import cadastrar_professor, consultar_professores_por_disciplina
from disciplinas import cadastrar_disciplina, alocar_disciplina_em_turma, alocar_professor_em_disciplinas
from turmas import cadastrar_turma, consultar_disciplinas_alocadas_em_turma


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
        print("7 - Alocar Professor em Disciplinas")
        print("8 - Alocar Disciplina em Turma")
        print("9 - Consultar Disciplinas Alocadas em Turma")
        print("10 - Consultar Professores por Disciplina")
        print("11 - Sair")

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
            alocar_professor_em_disciplinas(disciplinas, professores)
        elif opcao == "7":
            consultar_disciplinas_alocadas_em_turma(turmas)
        elif opcao == "8":
            alocar_disciplina_em_turma(turmas, disciplinas)
        elif opcao == "9":
            consultar_disciplinas_alocadas_em_turma(turmas)
        elif opcao == "10":
            consultar_professores_por_disciplina(disciplinas, professores)
        elif opcao == "11":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
