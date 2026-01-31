# Solicita ao usuário que informe um número e exibe o número informado como um inteiro.
while True:
    numero = float(input("Por favor, informe um número: "))
    try:
        numero_int = int(numero)
        print(f"O número informado foi {numero_int}.")
        break
    except ValueError:
        print("Isso não é um número válido. Tente novamente.")