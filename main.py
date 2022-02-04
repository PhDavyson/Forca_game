palavra = 'Python'.upper()

qtd_caracteres = len(palavra)
acertos = 0
erros = 0
letras_acertadas = ''
letras_erradas = ''

print('# ' * qtd_caracteres)

while acertos != qtd_caracteres and erros != 6:
    mensagem = ''
    for letra in palavra:
        if letra in letras_acertadas:
            mensagem += letra
        else:
            mensagem += '_'

    print(mensagem)
    print('Você já acertou: ' + letras_acertadas)
    print('Você já errou: ' + letras_erradas)

    letra = input('Digite uma letra: ').upper()

    if letra in palavra:
        print('Você acertou uma letra!')
        letras_acertadas += letra
        acertos += 1
    else:
        print('Você errou! Tente novamente.')
        letras_erradas += letra
        erros += 1
    