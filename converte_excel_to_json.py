import json


JSON_FILENAME = 'datafiles/contatos_teste.json'

try:
    with open(JSON_FILENAME, "w") as file:
        data = json.load(file, indent=4)
except Exception as erro:
    print("Ocorreu um erro quando tentava salvar o arquivo %s " % erro)
