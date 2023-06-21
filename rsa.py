#dicionario com os valores correspondentes a cada letra (e tambem o inverso)
dicionario = {
    'A' : 2, 'B' : 3, 'C' : 4, 'D' : 5, 'E' : 6, 'F' : 7, 'G' : 8, 'H' : 9,
    'I' : 10, 'J' : 11, 'K' : 12, 'L' : 13, 'M' : 14, 'N' : 15, 'O' : 16,
    'P' : 17, 'Q' : 18, 'R' : 19, 'S' : 20, 'T' : 21, 'U' : 22, 'V' : 23,
    'W' : 24, 'X' : 25, 'Y' : 26, 'Z' : 27, ' ': 28,

    2 : 'A', 3 : 'B', 4 : 'C', 5 : 'D', 6 : 'E', 7 : 'F', 8 : 'G', 9 : 'H',
    10 : 'I', 11 : 'J', 12 : 'K', 13 : 'L', 14 : 'M', 15 : 'N', 16 : 'O',
    17 : 'P', 18 : 'Q', 19 : 'R', 20 : 'S', 21 : 'T', 22 : 'U', 23 : 'V',
    24 : 'W', 25 : 'X', 26 : 'Y', 27 : 'Z', 28 : ' '
}

#funcao para achar o d
def calcular_d(e, z):
    return pow(e, -1, z)

#funcao para descriptografar
def descriptografar():
    p = int(input("Digite o valor de P: "))
    q = int(input("Digite o valor de Q: "))
    e = int(input("Digite o valor de E: "))

    z = (p - 1)*(q - 1)
    n = p * q

    criptografado = []

    print("Digite o texto criptografado conforme as instruções do programa\nOBS: Para encerrar a digitação dos valores criptografados, basta digitar 0 e pressionar enter.")
    while True:
        valor = int(input("Digite aqui o valor do caractere: "))
        if valor == 0:
            break
        else:
            criptografado.append(valor)
            print("Digite o proximo caractere ou 0 para encerrar")
        
    d = calcular_d(e, z)
    descriptografado = ""

    for x in criptografado:
        descriptografado = descriptografado+(dicionario[(x**d)%n])
    print(f"O texto descriptografado é:\n{descriptografado}")

    with open("texto_descript.txt", "w") as f:
        f.write(f"Texto descriptografado: \n{descriptografado}")

#funcao para encriptar
def encriptar():
    e = int(input("Digite o valor de E: "))
    n = int(input("Digite o valor de N: "))

    texto = input("Agora digite o texto a ser encriptado:\n")
    texto = texto.upper()
    encriptada = []
    criptografado = []

    for letra in texto:
        encriptada.append(dicionario[letra])
    
    for x in encriptada:
        criptografado.append((x ** e) % n)
    
    with open("texto_criptografado.txt", "w") as f:
        f.write(f"Texto criptografado: {criptografado}")
    print("Texto salvo no diretorio!")


#verifica se dois numeros sao coprimos (primos entre si)
def are_coprime(number1, number2):
    for i in range(2, min(number1, number2) + 1):
        if number1 % i == 0 and number2 % i == 0:
            return True
    return False

#verifica se o numero e primo
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

#funcao para gerar a chave publica
def chave_publica():
    p = int(input("Digite o valor de P: "))
    if is_prime(p) == False:
        print("Digite um valor válido para Q (que seja primo).")
        print("A opção será reiniciada!")
        chave_publica()
    
    q = int(input("Digite o valor de Q: "))
    if is_prime(q) == False:
        print("Digite um valor válido para Q (que seja primo).")
        print("A opção será reiniciada!")
        chave_publica()
    
    e = int(input("Digite o valor de E: "))
    z = (p - 1)*(q - 1)
    n = p * q
    
    if is_prime(e) == False:
        print("Digite um valor válido para E (que seja coprimo de (P - 1)(Q - 1)).")
        print("A opção será reiniciada!")
        chave_publica()
    elif are_coprime(e, z) == True:
        print("Digite um valor válido para E (que seja coprimo de (P - 1)(Q - 1)).")
        print("A opção será reiniciada!")
        chave_publica()
        return
    
    with open("chave.txt", "w") as x:
        x.write(f"As variaveis armazenadas no diretorio foram:\nE = {e}\nN = {n}")
    print("As variáveis foram armazenadas no diretório!")
    
    return


def main():
    print("Escolha um número referente a opção desejada:\n1 - Gerar chave pública\n2 - Encriptar um texto\n3 - Descriptografar um texto")
    operacao = int(input("OPCAO: "))
    e = 0
    n = 0
    if operacao == 1:
        print("\nConsidere que P e Q tem que ser primos e E tem que ser coprimo de (P - 1)(Q - 1)!")
        print("Agora vamos escolher as variáveis necessárias para o processo:\n")
        chave_publica()
    elif operacao == 2:
        print("OBS: Digite os valores que formam a chave pública e foram armazenados no diretório.")
        encriptar()
    elif operacao == 3:
        print("Digite os valores que formam a chave privada corretamente, ou a desencriptação não funcionará corretamente!")
        print("Nesse caso, os valores necessários serão solicitados conforme necessário.")
        descriptografar()
        print("O texto foi transformado todo para maiusulos (caixa alta)")
    else:
        print("Identificador inválido!\n")
        main()

main()