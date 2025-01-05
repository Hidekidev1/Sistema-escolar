def cadastrar_turma(turmas, nome, codigo, disciplinas, professor):
    turma = {
        "nome": nome,
        "codigo": codigo,
        "disciplinas": disciplinas,
        "professor": professor,
        "alunos": []
    }
    turmas.append(turma)