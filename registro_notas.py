def registrar_notas():
    """Permite registrar as notas de uma turma e calcula a média ao final."""
    notas = []

    print("Registro de Notas da Turma")
    print("Digite as notas entre 0 e 10. Digite 'fim' para encerrar.\n")

    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ").strip()

        if entrada.lower() == 'fim':
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Erro: Nota inválida. Digite uma nota entre 0 e 10.\n")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número válido ou 'fim' para encerrar.\n")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")

if __name__ == "__main__":
    registrar_notas()
