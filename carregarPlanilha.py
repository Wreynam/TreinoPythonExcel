import openpyxl

book = openpyxl.load_workbook('Planilha de teste.xlsx')

Carros = book['Carros']

for rows in Carros.iter_rows(min_row=2,max_row=4):
    print(rows[0].value,rows[1].value,rows[2].value)