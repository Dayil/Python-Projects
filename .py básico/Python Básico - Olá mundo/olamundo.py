# Olá mundo em Python após digitar 1

while True:
    entrada = input("Digite 1 para ver a mensagem 'Olá mundo': ")
    if entrada == '1':
        print("Olá mundo! 😉")
        break
    else:
        print("Entrada inválida. Por favor, tente novamente.")