# Anotações importantes sobre Python para estudo e fixação, explicando nos comentários de forma para iniciante e leigos entenderem. Como se fosse uma documentação oficial

# Para facilitar a leitura, cada seção é separada por linhas de sublinhado.
# E para fácil busca, recomendo usar Ctrl + F e digitar palavras-chave relacionadas ao que você quer encontrar.

print('________________________________________')
print("Tipos de dados básicos em Python") # Explicação dos tipos de dados básicos em Python
print("int - Números inteiros, sem parte decimal") # Explicação do tipo int
print("float - Números com parte decimal") # Explicação do tipo float
print("str - Cadeias de caracteres, textos") # Explicação do tipo str
print("bool - Valores booleanos, True ou False") # Explicação do tipo bool
print('________________________________________')


print('________________________________________')
print("Erros e exceções comuns em Python") # Explicação dos erros e exceções comuns em Python
print("SyntaxError - Erro de sintaxe, quando o código não segue as regras da linguagem") # Levantado quando o interpretador encontra um erro de sintaxe no código. Ex: esquecer de fechar um parêntese ou aspas resultaria em um SyntaxError.

print("NameError - Erro de nome, quando uma variável ou função não é definida") # Levantado quando se tenta avaliar um identificador (nome) não atribuído. Ex: tentar usar uma variável que não foi definida anteriormente resultaria em um NameError.

print("TypeError - Erro de tipo, quando uma operação é aplicada a um tipo de dado inadequado") # Levantado quando uma operação da função é aplicada a um objeto do tipo errado. Ex: tentar somar uma string com um número resultaria em um TypeError.

print("ValueError - Erro de valor, quando uma função recebe um argumento com o tipo correto, mas valor inadequado") # Ex: tentar converter uma string que não representa um número em um inteiro resultaria em um ValueError.

print("IndexError - Erro de índice, quando se tenta acessar um índice que não existe em uma lista ou string") # Quando um índice está fora de índices válidos. Ex: lista com 3 elementos (índices 0, 1, 2), tentar acessar o índice 7 resultaria em um IndexError.

print("KeyError - Erro de chave, quando se tenta acessar uma chave que não existe em um dicionário") # Ex: tentar acessar uma chave inexistente em um dicionário resultaria em um KeyError.

print("ZeroDivisionError - Erro de divisão por zero, quando se tenta dividir um número por zero") # Levantado quando se tenta dividir por 0. Ex: tentar executar 10 dividido por 0 resultaria em um ZeroDivisionError.

print("KeyboardInterrupt - Interrupção do teclado, quando o usuário interrompe a execução do programa (geralmente com Ctrl+C)") # Ex: pressionar Ctrl+C durante a execução de um programa resultaria em um KeyboardInterrupt.

print("OverflowError - Erro de estouro, quando uma operação resulta em um valor numérico muito grande para ser representado") # Ex: tentar calcular um número muito grande que excede o limite do tipo float resultaria em um OverflowError. Ex: calcular 10 elevado a 1000 pode resultar em um OverflowError.

print("ImportError - Erro de importação, quando um módulo ou pacote não pode ser encontrado ou carregado") # Ex: tentar importar um módulo que não existe resultaria em um ImportError. Ex: tentar importar um módulo chamado 'modulo_inexistente' resultaria em um ImportError.

print("IndentationError - Erro de indentação, quando a estrutura do código não está corretamente indentada") # Ex: esquecer de indentar um bloco de código dentro de uma função ou loop resultaria em um IndentationError.

print("IOError - Erro de entrada/saída, quando ocorre um problema ao ler ou escrever em um arquivo") # Levantado quando uma operação de entrada/saída falha por um motivo relacionado a isso. Ex: tentar abrir um arquivo que não existe para leitura resultaria em um IOError.
print('________________________________________')



print('________________________________________')
print("Repetição de caracteres em print") # Explicação de como repetir caracteres em Python
print("-" * 20) # Printa o conteúdo escrito multiplicando os caracteres por 20x

print('________________________________________')
print("Operadores aritméticos em Python") # Explicação dos operadores aritméticos em Python, usados para realizar operações matemáticas
print("+  - Adição") # Operador de adição
print("-  - Subtração") # Operador de subtração
print("*  - Multiplicação") # Operador de multiplicação
print("/  - Divisão") # Operador de divisão
print("// - Divisão inteira (retorna o quociente sem a parte decimal)") # Operador de divisão inteira
print("%  - Resto da divisão (retorna o resto da divisão entre dois números)") # Operador de resto da divisão
print("** - Exponenciação (eleva um número a uma potência)") # Operador de exponenciação
print('________________________________________')

print('________________________________________')
print("Operadores de comparação em Python") # Operadores de comparação em Python, usados para comparar valores e retornar um valor booleano (True ou False)
print("==  - Igual a") # Operador de igualdade
print("!=  - Diferente de") # Operador de diferença
print(">   - Maior que") # Operador maior que
print("<   - Menor que") # Operador menor que
print(">=  - Maior ou igual a") # Operador maior ou igual a
print("<=  - Menor ou igual a") # Operador menor ou igual a
print('________________________________________')

print('________________________________________')
print("Ordem de precedência") # Tabela de precedência das operações, como os calculos devem ser priorizados.
print("1 - ()") # Parênteses, primeiro a resolver o que estiver dentro deles.
print("2 - **") # Exponenciação, segundo a resolver.
print("3 - *, /, //, %") # Multiplicação, Divisão, Divisão Inteira e Resto da Divisão.
print("4 - +, -") # Adição e Subtração, por último a resolver.
print('________________________________________')

print('________________________________________')
print("Estruturas de decisão em Python") # Explicação das estruturas de decisão em Python, usadas para tomar decisões com base em condições.
print("if - Se uma condição for verdadeira, executa um bloco de código") # Explicação do if
print("else - Se a condição for falsa, executa um bloco de código alternativo") # Explicação do else
print("elif - Se a primeira condição for falsa, verifica outra condição") # Explicação do elif
print("Exemplo com if:")
idade18 = 18 # Eu defini que a variável idade com o valor 18
if idade18 >= 18:
    print("Você é maior de idade.") # Bloco de código executado se a condição for verdadeira
print("Exemplo com if e else:")
idade16 = 16 # Eu defini que a variável idade com o valor 16
if idade16 >= 18:
    print("Você é maior de idade.") # Bloco de código executado se a condição for verdadeira
else:
    print("Você é menor de idade.") # Bloco de código executado se a condição for falsa
print("Exemplo com if, elif e else:")
idade20 = 20 # Eu defini que a variável idade com o valor 20
if idade20 < 18:
    print("Você é menor de idade.") # Bloco de código executado se a primeira condição for verdadeira, se tiver menos de 18 anos
elif idade20 == 18:
    print("Você acabou de se tornar maior de idade.") # Bloco de código executado se a segunda condição for verdadeira, se tiver exatamente 18 anos
else:
    print("Você é maior de idade.") # Bloco de código executado se todas as condições anteriores forem falsas, se tiver mais de 18 anos
print('________________________________________')


print('________________________________________')
print("Estruturas de repetição em Python e instruções de loop") # Explicação das estruturas de repetição em Python, usadas para repetir blocos de código
print("while - Repete um bloco de código enquanto uma condição for verdadeira") # Explicação do while
print("for - Repete um bloco de código para cada item em uma sequência (como listas ou intervalos)") # Explicação do for
print("break - Encerra o loop atual") # Usado para sair de um loop antes que ele termine naturalmente. Utilizada para interromper as repetições dos laços for e while.
print("continue - Pula para a próxima iteração do loop") # Usado para pular o restante do código no loop e ir para a próxima iteração, pular a iteração atual de um laço e passar para a próxima iteração.
print("pass - Não faz nada, é um placeholder") # Usado quando uma declaração é necessária sintaticamente, mas você não quer executar nada, quando você precisa de uma sintaxe que exige um bloco de código, mas ainda não decidiu o que escrever no bloco
print("Exemplo com while:")
contador = 0 # Eu defini a variável contador com o valor 0
while contador < 5:
    print("Contador é:", contador) # Bloco de código executado enquanto a condição for verdadeira, enquanto o contador for menor que 5 vai printar o valor do contador
    contador += 1 # Incrementa o contador em 1 a cada iteração, adicionando 1 ao valor atual do contador.
print("Exemplo com for:")
for indice in range(5):
    print("Índice é:", indice) # Bloco de código executado para cada valor na sequência gerada por range(5), que vai de 0 a 4, então vai printar o valor do índice de 0 a 4
print("Exemplo com break:")
for numero in range(10): # Loop que vai de 0 a 9
    if numero == 5: # Quando o número chegar a 5
        break # Sai do loop quando o número for igual a 5
    print("Número é:", numero) # Bloco de código executado até o break, então vai printar os números de 0 a 4
print("Exemplo com continue:")
for numero in range(5): # Loop que vai de 0 a 4
    if numero == 2: # Quando o número chegar a 2
        continue # Pula o restante do código e vai para a próxima iteração quando o número for igual/chegar a 2
    print("Número é:", numero) # Bloco de código executado, então vai printar os números 0, 1, 3 e 4 (pulando o 2)
print("Exemplo com pass:")
for letra in 'Daniel': # Loop que percorre cada letra na string 'Daniel'
    if letra == 'a': # Quando a letra for 'a'
        pass # Não faz nada quando a letra for 'a'
    else:
        print("Letra é:", letra) # Bloco de código executado para as outras letras, então vai printar as letras D, n, i, e, l (ignorando o 'a')
print('________________________________________')


print('________________________________________')
print("Comentários em Python") # Explicação de como fazer comentários em Python
print("# - Comentário de uma linha") # Usando o símbolo de cerquilha (#) para fazer comentários de uma linha.
print('""" Comentário \n de múltiplas \n linhas """') # Usando três aspas duplas para fazer comentários de múltiplas linhas.
print("''' Comentário \n de múltiplas \n linhas '''") # Usando três aspas simples para fazer comentários de múltiplas linhas.
print('________________________________________')


print('________________________________________')
print("Print() com aspas simples, duplas e triplas") # Explicação de como usar aspas simples, duplas e triplas no print()
print("Aspas duplas - Permite incluir aspas simples dentro da string sem precisar de escape") # Explicação do uso de aspas duplas
print('Exemplo:')
print("Ele disse: 'Olá, mundo!'") # Exemplo de uso de aspas duplas
print("Aspas simples - Permite incluir aspas duplas dentro da string sem precisar de escape") # Explicação do uso de aspas simples
print('Exemplo:')
print('Ela respondeu: "Oi, tudo bem?"') # Exemplo de uso de aspas simples
print("Aspas triplas - Permite criar strings de múltiplas linhas") # Explicação do uso de aspas triplas
print('Exemplo:')
print("""Tigre tigre, tigre que flamejas
Na selva noturna sombria,
Qual imortal mão ou olho
Poderia moldar tua terrível simetria? - William Blake""") # Exemplo de uso de aspas triplas
print('________________________________________')

      
print('________________________________________')
print("Entrada de dados com input()") # Explicação de como receber entrada de dados do usuário
print("input() - Função que permite receber dados do usuário via teclado") # A função input() pausa o programa e espera o usuário digitar algo e pressionar Enter.
print("Exemplo:")
nome = input("Digite seu nome: ") # Exemplo de uso da função input()
print("Olá,", nome) # Exemplo de como usar o valor recebido
print('________________________________________')


print('________________________________________')
print(".format() vs f-strings") # Explicação sobre formatação de strings
print(".format() - Método antigo de formatação de strings") # Explicação do método .format()
print("Exemplo:")
print("Olá, {}".format(nome)) # Exemplo de uso do .método .format()
print("f-strings - Método moderno e mais fácil de formatação de strings") # Explicação das f-strings
print("Exemplo:")
print(f"Olá, {nome}") # Exemplo de uso das f-strings
print('________________________________________')


print('________________________________________')
print("Alinhamento e espaçamento em strings") # Explicação sobre alinhamento e espaçamento em strings
print("Usando .format() para alinhar texto") # Explicação do alinhamento usando .format()
print("Exemplo:")
nome = input("Digite seu nome: ")
print("Prazer te conhecer {:<11},".format(nome)) # Alinhamento à esquerda com 11 espaços
print("Prazer te conhecer {:^11},".format(nome)) # Alinhamento centralizado com 11 espaços
print("Prazer te conhecer {:>11},".format(nome)) # Alinhamento à direita com 11 espaços
print('________________________________________')
print("Usando f-strings para alinhar texto") # Explicação do alinhamento usando f-strings
print("Exemplo:")
print(f"Prazer te conhecer {nome:>11},") # Alinhamento à direita com 11 espaços
print(f"Prazer te conhecer {nome:^11},") # Alinhamento centralizado com 11 espaços
print(f"Prazer te conhecer {nome:<11},") # Alinhamento à esquerda com 11 espaços
print('________________________________________')


print('________________________________________')
print(" end='' em print()") # Explicação sobre o uso do end em print()
print("Por padrão, o print() adiciona uma nova linha após a impressão") # Explicação do comportamento padrão do print()
print("Usando end='' para evitar a nova linha") # Explicação do uso do end=''
print("Exemplo:")
print("Olá,", end=' ') # Exemplo de uso do end=''
print("mundo!") # Continuação do exemplo
print('________________________________________')

print('________________________________________')
print("Fatiamento de strings") # Explicação sobre fatiamento de strings
print("Permite acessar partes específicas de uma string usando índices") # Explicação do conceito
print("Exemplo:")
frase = "Curso em Vídeo Python"
print(frase[9]) # Acessa o caractere na posição 9 que é 'V'
print(frase[9:14]) # Acessa os caracteres da posição 9 até 13 que é 'Vídeo'
print(frase[:5]) # Acessa os primeiros 5 caracteres que é 'Curso' ignorando o indíce 5 que é o espaço
print(frase[15:]) # Acessa os caracteres a partir da posição 15 até o final da frase que é 'Python'
print(frase[9:21:2]) # Acessa os caracteres da posição 9 até 20, pulando de 2 em 2 que é 'VdoPto'
print(frase[9::3]) # Acessa os caracteres a partir da posição 9 até o final, pulando de 3 em 3 que é 'VePh'
print("No caso de fatiamento, o índice inicial é inclusivo e o índice final é exclusivo.") # Explicação do comportamento do fatiamento
print("Isso significa que o caractere na posição inicial é incluído, mas o caractere na posição final não é incluído.") # Explicação adicional
print('________________________________________')

print('________________________________________')
print("Funções úteis e análise para strings") # Explicação sobre funções úteis para manipulação de strings
print("len() - Retorna o comprimento da string") # Explicação da função len()
print("Exemplo:")
print("Curso em Vídeo Python")
print(len(frase)) # Exemplo de uso da função len()
print("count() - Conta quantas vezes um caractere ou substring aparece na string") # Explicação da função count()
print("Exemplo:")
print("Curso em Vídeo Python")
print(frase.count('o')) # Exemplo de uso da função count() no caso o resultado de Curso em Vídeo Python é 3
print("count() com fatiamento - Conta em uma parte específica da string") # Explicação do uso do count() com fatiamento
print("Exemplo:")
print("Curso em Vídeo Python")
print(frase.count('o',0,13)) # Exemplo de uso do count() com fatiamento no caso o resultado de Curso em Vídeo é 1 pois só conta até o índice 12
print("find() - Retorna o índice da primeira ocorrência de um caractere ou substring") # Explicação da função find()
print("Exemplo:")
print("Curso em Vídeo Python")
print(frase.find('deo')) # Exemplo de uso da função find() no caso o resultado de Curso em Vídeo Python é 11 pois a substring 'deo' começa no índice 11
print("Se o valor não for encontrado, retorna -1") # Explicação do comportamento quando o valor não é encontrado
print("Exemplo:")
print("Curso em Vídeo Python")
print(frase.find('Android')) # Exemplo de uso da função find() quando o valor não é encontrado no caso o resultado de Curso em Vídeo Python é -1
print("in - Verifica se uma substring está presente na string, retornando True ou False") # Explicação do operador in
print("Exemplo:")
print("Curso em Vídeo Python")
print("Curso" in frase) # Exemplo de uso do operador in no caso o resultado de Curso em Vídeo Python é True
print('________________________________________')

print('________________________________________')
print("Funções de transformação para strings") # Explicação sobre funções de transformação para strings
print("replace() - Substitui uma substring por outra") # Explicação da função replace()
print("Exemplo:")
print("Curso em Vídeo Python")
print(frase.replace('Python', 'Android')) # Exemplo de uso da função replace() no caso o resultado de Curso em Vídeo Python é Curso em Vídeo Android
print("upper() - Converte todos os caracteres da string para maiúsculas") # Explicação da função upper()
print("Exemplo:")
print("Curso em Vídeo Python")
print(frase.upper()) # Exemplo de uso da função upper() no caso o resultado de Curso em Vídeo Python é CURSO EM VÍDEO PYTHON
print("lower() - Converte todos os caracteres da string para minúsculas") # Explicação da função lower()
print("Exemplo:")
print("Curso em Vídeo Python")
print(frase.lower()) # Exemplo de uso da função lower() no caso o resultado de Curso em Vídeo Python é curso em vídeo python
print("capitalize() - Converte o primeiro caractere da string para maiúscula e o restante para minúsculas") # Explicação da função capitalize()
print("Exemplo:")
print("Curso em Vídeo Python")
print(frase.capitalize()) # Exemplo de uso da função capitalize() no caso o resultado de Curso em Vídeo Python é Curso em vídeo python
print("title() - Converte o primeiro caractere de cada palavra para maiúscula") # Explicação da função title()
print("Exemplo:")
print("Curso em Vídeo Python")
print(frase.title()) # Exemplo de uso da função title() no caso o resultado de Curso em Vídeo Python é Curso Em Vídeo Python
print('________________________________________')

print('________________________________________')
print("Funções de remoção e divisão para strings") # Explicação sobre funções de remoção e divisão para strings
print("strip() - Remove espaços em branco no início e no final da string") # Explicação da função strip()
print("Exemplo:")
frase2 = "   Aprenda Python   "
print(frase2.strip()) # Exemplo de uso da função strip() no caso o resultado de "   Aprenda Python   " é "Aprenda Python"
print("rstrip() - Remove espaços em branco no final da string") # Explicação da função rstrip()
print("Exemplo:")
print(frase2.rstrip()) # Exemplo de uso da função rstrip() no caso o resultado de "   Aprenda Python   " é "   Aprenda Python"
print("lstrip() - Remove espaços em branco no início da string") # Explicação da função lstrip()
print("Exemplo:")
print(frase2.lstrip()) # Exemplo de uso da função lstrip() no caso o resultado de "   Aprenda Python   " é "Aprenda Python   "
print("split() - Divide a string em uma lista de substrings com base em um separador") # Explicação da função split()
print("Exemplo:")
print("Curso em Vídeo Python")
print(frase.split()) # Exemplo de uso da função split() no caso o resultado de Curso em Vídeo Python é ['Curso', 'em', 'Vídeo', 'Python'] como se cada palavra fosse uma lista diferente.
print("Curso > iria resultar em uma lista com 4 elementos de 0 a 4") # Lista 0
print("em > iria resultar em um lista com 2 elementos de 0 a 1") # Lista 1
print("Vídeo > iria resultar em um lista com 5 elementos de 0 a 4") # Lista 2
print("Python > iria resultar em um lista com 6 elementos de 0 a 5") # Lista 3
print("join() - Junta uma lista de substrings em uma única string com um separador") # Explicação da função join() - oposto de split()
print("Exemplo:")
print("Curso em Vídeo Python") # Faça de conta que esse .split() resultou em uma lista de substrings onde cada palavra é um elemento diferente da lista.
print('-'.join(frase.split())) # Exemplo de uso da função join() no caso o resultado de Curso em Vídeo Python é Curso-em-Vídeo-Python
print('________________________________________')

