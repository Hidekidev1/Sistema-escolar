def cadastrar_aluno(alunos, nome, matricula, data_nascimento, sexo, endereco, telefone, email, disciplina):
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "disciplina": disciplina
    }
    alunos.append(aluno)
