# Classe Calculadora

class Calculadora:

    def soma(self, x, y):
        try:
            return x + y
        except TypeError:
            return "Erro: Tipos de dados inválidos para adição."

    def subtracao(self, x, y):
        try:
            return x - y
        except TypeError:
            return "Erro: Tipos de dados inválidos para subtração."

    def multiplicacao(self, x, y):
        try:
            return x * y
        except TypeError:
            return "Erro: Tipos de dados inválidos para multiplicação."

    def divisao(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return "Erro: O número não pode ser dividido por zero."
        except TypeError:
            return "Erro: Tipos de dados inválidos para divisão."


# Função para ler número com validação
def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print(" Erro: digite um número válido.")


#  objeto da calculadora


calc = Calculadora()

while True:
    print("\n")
    print("\n1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "0":
        print("Saindo...")
        break

    x = ler_numero("Digite o primeiro número: ")
    y = ler_numero("Digite o segundo número: ")

    if opcao == "1":
        print("Resultado:", calc.soma(x, y))
    elif opcao == "2":
        print("Resultado:", calc.subtracao(x, y))
    elif opcao == "3":
        print("Resultado:", calc.multiplicacao(x, y))
    elif opcao == "4":
        print("Resultado:", calc.divisao(x, y))
    else:
        print("Opção inválida")