def cadastrar_disciplina(disciplinas, nome, codigo, carga_horaria, professor):
    disciplina = {
        "nome": nome,
        "codigo": codigo,
        "carga_horaria": carga_horaria,
        "professor": professor
    }
    disciplinas.append(disciplina)
