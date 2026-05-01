import json

def carregar_db():
    with open("../banco_dados.json", "r", encoding="utf-8") as arq:
        db = json.load(arq)
        return db

def salvar_db(db_novo):
    with open("../banco_dados.json", "w", encoding="utf-8") as arq:
        json.dump(db_novo, arq, ensure_ascii=False, indent=4, default=str)
        return True

def listar_usuarios():
    db = carregar_db()
    return db

def salvar_usuario(user):
    usuarios = carregar_db()  # passa os dados .json para dict python
    usuarios["usuarios"].append(user.to_dict())  # adiciono o dict do usuario criado
    salvar_db(usuarios)
    return True

def atualizar_usuario_no_db(email_antigo, usuario_atualizado):
    db = carregar_db()
    for usuario in db["usuarios"]:
        if usuario["email"] == email_antigo:
            usuario.update(usuario_atualizado)
            salvar_db(db)
            return True
    return False

def buscar_usuario_email(email):
    db = carregar_db()
    for usuario in db["usuarios"]:
        if usuario["email"] == email:
            return usuario
    return False

def deletar_por_email(email):
    db = carregar_db()
    for usuario in db["usuarios"]:
        if usuario["email"] == email:
            db["usuarios"].remove(usuario)
            salvar_db(db)
            return True
    return False