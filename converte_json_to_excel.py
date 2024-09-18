import pandas
import json


EXCEL_FILENAME = "/datafiles/excel_teste.xlsx"
SHEET_NAME = "contatos"

JSON_FILENAME = "/datafiles/contatos_teste.json"
#
# try:
#     with open(JSON_FILENAME, 'r') as file:
#         dados = json.load(file)
#

print("criando dataframe")
data_frame = pandas.DataFrame(dados)

print("salvando dataframe")

data_frame.to_excel(EXCEL_FILENAME, sheet_name=SHEET_NAME)