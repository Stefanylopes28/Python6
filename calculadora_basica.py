def obter_numero(prompt: str) -> float:
    """Solicita um número ao usuário, tratando entradas inválidas."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número válido.")

def obter_operacao() -> str:
    """Solicita uma operação válida ao usuário."""
    operacoes_validas = ['+', '-', '*', '/']
    while True:
        operacao = input("Digite a operação desejada (+, -, *, /): ").strip()
        if operacao in operacoes_validas:
            return operacao
        else:
            print("Erro: Operação inválida. Tente novamente.")

def calcular(num1: float, num2: float, operacao: str) -> float:
    """Executa a operação matemática escolhida."""
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return num1 / num2

def calculadora():
    """Função principal da calculadora."""
    print("Bem-vindo à Calculadora Python!")
    
    while True:
        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")
        operacao = obter_operacao()
        
        try:
            resultado = calcular(num1, num2, operacao)
            print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
            break  # Encerrar o programa após sucesso
        except ZeroDivisionError as e:
            print(f"Erro: {e}")
            print("Tente novamente.\n")

if __name__ == "__main__":
    calculadora()
