def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

#funcao para gerar a chave publica
def chave_publica():
    p = int(input("Digite P: "))
    if not is_prime(p):
        print("Digite um valor válido para Q (que seja primo).")
        print("A opção será reiniciada!")
        chave_publica()
    
    q = int(input("Digite Q: "))
    if not is_prime(q):
        print("Digite um valor válido para Q (que seja primo).")
        print("A opção será reiniciada!")
        chave_publica()
    
    e = int(input("Digite E: "))
    z = (p - 1)*(q - 1)
    n = q * q
    


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
        #encriptar()
    elif operacao == 3:
        print("Digite os valores que formam a chave privada corretamente, ou a desencriptação não funcionará corretamente!")
        print("Nesse caso, os valores necessários serão solicitados conforme necessário.")
        #desecriptadora()
        print("Como os identificadores para as letras maiúsculas e minúsculas são os mesmos, o texto foi impresso todo em caracteres maiúsculos.")
    else:
        print("Identificador inválido!\n")
        main()

main()