continuar_prompt = "Gostaria de deixar outra pessoa continuar a pesquisa?"
continuar_prompt += "\n(sim|nao)"
nome_prompt = "Qual seu nome? "
lugar_prompt = "Se pudesse escolher um lugar do mundo, para onde iria? "

respostas = {}
pesquisa_ativa = True

while pesquisa_ativa:
    nome = input(nome_prompt)

    nome_prompt = [nome] = lug
continuar_nome, lugar in respostas.items():

    continuar = input(continuar
    respostas[nome] = lugar
continuar_
continuar_nome, lugar in respostas.items():

    continuar = input(continuar_prompt)
    if continuar == "nao":
        pesquisa_ativa = False

for nome, lugar in respostas.items():
    print(f"O {nome.title()} gostaria de ir para {lugar.title()}")