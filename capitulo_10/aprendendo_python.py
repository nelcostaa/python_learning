from pathlib import Path

path = Path("capitulo_10/aprendi_no_python.txt")
conteudo = path.read_text()

print(conteudo)

for linha in conteudo.splitlines():
    print(linha)
