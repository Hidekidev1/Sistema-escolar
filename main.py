from alunos import cadastrar_aluno, listar_alunos
from professores import cadastrar_professor, listar_professores
from turmas import cadastrar_turma, listar_turmas, matricular_aluno, alocar_disciplina_em_turma, consultar_disciplinas_alocadas_em_turma, alunos_matriculados_em_turma
from disciplinas import cadastrar_disciplina, listar_disciplinas, consultar_professores_por_disciplina
from persistencia import carregar_dados, salvar_dados

def main():
    # Carregar dados dos arquivos JSON
    professores = carregar_dados("professores.json") or []
    alunos = carregar_dados("alunos.json") or []
    disciplinas = carregar_dados("disciplinas.json") or []
    turmas = carregar_dados("turmas.json") or []

    while True:
        print("\nSistema de Gestão Escolar")
        print("=== Cadastro ===")
        print("1 - Cadastrar Professor")
        print("2 - Cadastrar Aluno")
        print("3 - Cadastrar Disciplina")
        print("4 - Cadastrar Turma")

        print("\n=== Listagem ===")
        print("5 - Listar Alunos")
        print("6 - Listar Professores")
        print("7 - Listar Turmas")
        print("8 - Listar Disciplinas")

        print("\n=== Matrícula e Alocação ===")
        print("9 - Matrícula de Aluno em Turma")
        print("10 - Alocar Disciplina em Turma")

        print("\n=== Consultas ===")
        print("11 - Consultar Professores por Disciplina")
        print("12 - Consultar Alunos Matriculados em Turma")
        print("13 - Consultar Disciplinas Alocadas em Turma")

        print("\n14 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_professor(professores)
            salvar_dados("professores.json", professores)
        elif opcao == "2":
            cadastrar_aluno(alunos, disciplinas)
            salvar_dados("alunos.json", alunos)
        elif opcao == "3":
            cadastrar_disciplina(disciplinas, professores)
            salvar_dados("disciplinas.json", disciplinas)
        elif opcao == "4":
            cadastrar_turma(turmas, professores)
            salvar_dados("turmas.json", turmas)

        elif opcao == "5":
            listar_alunos(alunos)
        elif opcao == "6":
            listar_professores(professores)
        elif opcao == "7":
            listar_turmas(turmas)
        elif opcao == "8":
            listar_disciplinas(disciplinas)

        elif opcao == "9":
            matricular_aluno(turmas, alunos)
            salvar_dados("turmas.json", turmas)
            salvar_dados("alunos.json", alunos)

        elif opcao == "10":
            alocar_disciplina_em_turma(turmas, disciplinas)
            salvar_dados("turmas.json", turmas)

        elif opcao == "11":
            consultar_professores_por_disciplina(disciplinas, professores)

        elif opcao == "12":
            alunos_matriculados_em_turma(turmas)

        elif opcao == "13":
            consultar_disciplinas_alocadas_em_turma(turmas)

        elif opcao == "14":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
