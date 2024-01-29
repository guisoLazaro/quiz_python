perguntas = {
    'Qual o ano da Primeira Guerra Mundial?': 1914,
    'Qual o ano da Segunda Guerra Mundial?': 1939,
    'Quantos Mundiais tem o Corinthians': 2,
    'Quantos Mundiais tem o Palmeiras': 0,
    'Ano do Atentado das Torres Gêmeas': 2001,
    'Ano da tragédia da boate kiss': 2013
}

quantidade_acerto = 0
for pergunta, resposta in perguntas.items():

    try:
        resp = input(f"{pergunta}: ")
        if resp.lower() == 'sair':
            print("Você decidiu sair. Até mais!")
            break
        resp = int(resp)
        if(resp == (resposta)):
            quantidade_acerto = quantidade_acerto + 1
    except KeyboardInterrupt:
        print("Você interrompeu o quiz, para sair digite a palavra sair")

if(quantidade_acerto >= 4):
     print("Parabéns, você passou no Quiz")
else:
    print("Você não passou no Quiz :(")