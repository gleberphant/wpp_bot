# script para corrigir dados do excel
# separa apenas os números de celular com ddd 83

import pandas

# arquivo excel - nome_do_arquivo.xlsx

excel_file = "arquivos_excel/contatos_geral.xlsx"
planilha = "mulheres"

#  ler excel
data = pandas.read_excel(excel_file, sheet_name=planilha)

print(f" Colunas da tabela ", data.columns)

# dicionario do novo arquivo
novos_dados = {
    'nome': [],
    'celular': []
}

# loop para corrigir cada linha

for index, row in data.iterrows():
    nome = row["nome"]

    celular = ""

    telefone1 = str(row["telefone1"])
    telefone2 = str(row["telefone2"])

    if telefone1[:5] == "(83)9" or telefone1[:5] == "(83)8":
        celular = telefone1
    elif telefone2[:5] == "(83)9" or telefone2[:5] == "(83)8":
        celular = telefone2
    else:
        # print("numero errado ", telefone1, " e ", telefone2)
        continue
    # retira caracteres estranhos

    for char in celular:
        if not char.isdigit():
            celular = celular.replace(char, '')

    # verifica se o numero precisa acrescentar digito 9 a frente
    # se se tamanho eh 10
    # modelo numero 83999605757
    if len(celular) < 11:
        celular = celular[:2] + '9' + celular[2:]

    # criando nova linha no dicionario
    novos_dados['nome'] += [nome]
    novos_dados['celular'] += [celular]

print(f"..... gerando data frame ......")
novo_excel = pandas.DataFrame(novos_dados)

print(f"..... salvando arquivo ......")
novo_excel.to_excel('excel_corrigido.xlsx', sheet_name='contatos')
#
# # with open(arquivo_vcf, 'w', encoding='utf-8') as vcard_file:
# #     for index, row in data.iterrows():
# #         nome = row["nome"]
# #
# #         celular = row["celular"]
# #
# #         celular = celular.replace('(', '')
#         celular = celular.replace(')', '')
#
#         # exemplo numero 83999605757
#         if celular[2] == '8' or len(celular) == 10:
#             celular = celular[:2] + '9' + celular[2:]
#             print("\n numero ", celular)
#
#
#         # vcard_file.write('BEGIN\n')
#         # vcard_file.write('VERSION:3.0\n')
#         # vcard_file.write(f'N:{nome};;;\n')
#         # vcard_file.write(f'TEL;TYPE=CELL:{celular}\n')
#         # vcard_file.write('END:VCARD\n')
#
#     print("arquivo VCF gerado com sucesso")
#
#
