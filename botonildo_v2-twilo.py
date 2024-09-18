
import os

from dotenv import load_dotenv
import time
import pandas
import json
from random import randint

# variáveis globais
ACCOUNT_SID = None
AUTH_TOKEN = None


# verificar se as variáveis foram carregadas corretamente
def check_env(sid_param, auth_token_param):
    if sid_param and auth_token_param:
        print(sid_param)
        print(auth_token_param)
    else:
        print("token de acesso não configura")
        exit('1')


def main():
    print("")

# 	EXCEL_FILE = "lista_contatos_excel.xlsx"
# 	NOME_PLANILHA = 'contatos'
# 	LOG_FILE = "log_enviados.json"
# 	MENSAGEM_FILE = "mensagem.txt"
#
# 	data = pandas.read_excel(EXCEL_FILE, sheet_name=NOME_PLANILHA)
#
# 	lista_contatos = []
#
# 	for index, row in data.iterrows():
# 		nome = row['nome'],
# 		numero = row['celular']
# 		lista_contatos.append(dict(nome=str(numero)))
#
# 	numero_destino = ""
# 	print(" -------------------------------------------------- ")
# 	print(" Carregando mensagem ...  ")
# 	try:
# 		with open(MENSAGEM_FILE, 'r', encoding='utf-8', errors="ignore") as file:
# 			mensagem = file.read()
# 			print(" -------------- Mensagem -------------------------- ")
# 			print(mensagem)
# 			print(" -------------------------------------------------- ")
#
# 	except Exception as erro:
# 		print(" Erro na leitura da mensagem: ", erro)
# 		exit(0)
#
# 	print(" -------------------------------------------------- ")
# 	print(" Carregando histórico de mensagens enviadas ... \n")
#
# 	try:
# 		with open(LOG_FILE, 'r') as file:
# 			historico = [json.loads(linha.strip()) for linha in file]
# 			print(" histórico carregado com sucesso ")
# 			print(" -------------------------------------------------- ")
#
# 	except Exception as erro:
# 		print("Erro no carregamento do histórico! Descrição: ", erro)
# 		historico = []
#
# 	count = 0
# 	print(" ")
#
# 	for contato in lista_contatos:
# 		print(" ")
# 		count += 1
#
# 		timer1 = randint(12, 22)	 # timer para envio da msg
# 		timer2 = randint(4, 8)	 # timer para fechar a janela
# 		timer3 = randint(2, 4)	 # timer para aguardar para reiniciar o ciclo
#
# 		numero_destino = "+55" + next(iter(contato.values()))
#
# 		if any(numero_destino == registro[0] and mensagem == registro[1] for registro in historico):
# 			print(" O número (%s) ja recebeu uma mensagem" % numero_destino)
# 			continue
# 		else:
# 			pass
#
# 		try:
# 			print("Enviando mensagem n (%i) para (%s) em (%i) seg" % (count, numero_destino, timer1,))

#
# 		except Exception as erro:
# 			print("Houve um erro no envio: ", erro)
# 		else:
# 			print(" Mensagem enviada com sucesso. Registrando número ")
#
# 			with open(LOG_FILE, 'a') as file:
# 				json.dump([numero_destino, mensagem], file)
# 				file.write("\n")
#
# 		time.sleep(timer3)
#
# 		print(" Aguardando %i segundos para enviar nova mensagem..." % timer3)
# 		print(" ----------------------------------------------------")
# 		print("")
#

# 	print(" ")
# 	print(" ------------------------------------------------")
# 	print(" | 				Operação finalizada             |")
# 	print(" |            Foram enviadas %i mensagens        |" % count)
# 	print(" ------------------------------------------------")
# 	print(" ")
# 	input(" ......... Pressione qualquer tecla para finalizar ..............")


if __name__ == "__main__":
    # carregar autenticação do arquivo .env
    load_dotenv()

    # acessar as variáveis do ambiente
    ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

    check_env(ACCOUNT_SID, AUTH_TOKEN)

    main()
