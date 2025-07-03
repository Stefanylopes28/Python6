def verificar_paridade(numero: int) -> str:
    """Retorna se o número é par ou ímpar."""
    return "par" if numero % 2 == 0 else "ímpar"

def coletar_numeros():
    """Solicita números ao usuário até que digite 'fim'."""
    quantidade_pares = 0
    quantidade_impares = 0

    print("Digite números inteiros. Quando quiser parar, digite 'fim'.\n")

    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ").strip()

        if entrada.lower() == 'fim':
            break

        try:
            numero = int(entrada)
            paridade = verificar_paridade(numero)
            print(f"O número {numero} é {paridade}.\n")

            if paridade == "par":
                quantidade_pares += 1
            else:
                quantidade_impares += 1

        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro ou 'fim'.\n")

    print("\nResumo:")
    print(f"Quantidade de números pares: {quantidade_pares}")
    print(f"Quantidade de números ímpares: {quantidade_impares}")

if __name__ == "__main__":
    coletar_numeros()
