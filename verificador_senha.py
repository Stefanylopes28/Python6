import re

def senha_forte(senha: str) -> bool:
    """Verifica se a senha é forte: pelo menos 8 caracteres e contém pelo menos um número."""
    return len(senha) >= 8 and any(char.isdigit() for char in senha)

def validar_senha():
    """Solicita senhas até que uma senha forte seja inserida ou o usuário digite 'sair'."""
    print("Digite uma senha forte (mínimo 8 caracteres e pelo menos um número).")
    print("Digite 'sair' para encerrar.\n")

    while True:
        senha = input("Digite a senha: ").strip()

        if senha.lower() == 'sair':
            print("Encerrando o programa.")
            break

        if senha_forte(senha):
            print("Senha forte cadastrada com sucesso!")
            break
        else:
            print("Senha fraca. A senha deve ter no mínimo 8 caracteres e conter pelo menos um número.\n")

if __name__ == "__main__":
    validar_senha()
