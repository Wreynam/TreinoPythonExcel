from ast import Import

import openpyxl


book = openpyxl.Workbook();
book.create_sheet('Carros');

get_test = book['Carros'];
get_test.append(['Modelo Lamborghini','Cavalos','Lançamento'])
get_test.append(['HURACAN','640','09/2014'])
get_test.append(['URUS','650','03/2018'])
get_test.append(['AVENTADOR','740','01/2018'])
book.save('Planilha de teste.xlsx')

