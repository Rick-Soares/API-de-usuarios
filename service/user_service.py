from SecureAuthApi.models.user_model import Usuario
from SecureAuthApi.repository.user_repostiory import *

def criar_usuario(nome, senha, email):
    if buscar_usuario_email(email):
        raise FileExistsError("Email já existente.")

    user = Usuario(nome=nome, senha=senha, email=email) #cria usuári
    salvar_usuario(user)
    return True

def apagar_usuario(email, senha):
    usuario = buscar_usuario_email(email)
    if not usuario:
        raise ValueError("Usuário não encontrado.")
    if usuario.senha != senha:
        raise PermissionError("Senha incorreto.")

    return deletar_por_email(email)

def atualizar_usuario(email, senha, novo_email, nova_senha, novo_nome):
    usuario = buscar_usuario_email(email)
    if not usuario:
        raise ValueError("Usuário não encontrado.")
    if usuario["senha"] != senha:
        raise PermissionError("Senha incorreto.")

    usuario_atualizado = {
        "nome": novo_nome,
        "email": novo_email,
        "senha": nova_senha,
         }
    atualizar_usuario_no_db(email, usuario_atualizado)
    return True


