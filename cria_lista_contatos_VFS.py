## script para converter uma lista de excel em contatos para androide


import pandas

# arquivo excel - nome_do_arquivo.xlsx

excel_file = "arquivos_excel/excel_corrigido.xlsx"
planilha = "contatos"
arquivo_vcf = 'contatos_mulheres.vcf'

# ler excel
data = pandas.read_excel(excel_file, sheet_name=planilha)

print(f" Colunas da tabela ", data.columns)

print(f"..... Criando arquivo ......")

with open(arquivo_vcf, 'w', encoding='utf-8') as vcard_file:
    for index, row in data.iterrows():
        nome = row["nome"]
        telefone = row["celular"]

        vcard_file.write('BEGIN\n')
        vcard_file.write('VERSION:3.0\n')
        vcard_file.write(f'N:{nome};;;\n')
        vcard_file.write(f'TEL;TYPE=CELL:{telefone}\n')
        vcard_file.write('END:VCARD\n')

print("arquivo VCF gerado com sucesso")


