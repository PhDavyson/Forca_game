import config, desenho

print(f'# Bem vindo ao JOGO DA FORCA! #')
print(f'Instruções:')
print(f'1) Digite apenas uma letra por vez;')
print(f'2) Não digite números;')
print(f'3) Após digitar uma letra, pressione enter para seguir.')

while config.acertos != config.qtd_caracteres and config.erros != 7:
    for letra in config.palavra:
        if letra in config.letras_acertadas:
            config.mensagem += f'{letra} '
        else:
            config.mensagem += '_ '

    print(desenho.forca + desenho.boneco[config.erros])
    print(config.mensagem)

    letra = input('Digite uma letra: ').upper()

    if len(letra) > 1:
        print(f'Digite APENAS LETRAS e somente UMA POR VEZ!')
        continue

    if letra in  config.letras_acertadas + config.letras_erradas:
        print('Você já tentou essa letra.')
        continue
    
    if letra in config.palavra:
        print(f'Você acertou uma letra!')
        config.letras_acertadas += letra
        config.acertos += config.palavra.count(letra)
    else:
        print(f'Você errou! Tente novamente.')
        config.letras_erradas += letra
        config.erros += 1
    
    if letra not in config.palavra:
        config.chances -= 1
        print(f'Você ainda tem {config.chances} chances.')
       
    if config.chances <= 0:
        print(desenho.forca + desenho.perna_esquerda)
        print(f'A palavra era {config.palavra}.')
        print(f'GAME OVER!!!')
        break