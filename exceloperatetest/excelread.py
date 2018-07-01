import xlrd
from datetime import date,datetime

filename = "text.xls"

def read_excel():
    #打开文件
    wb = xlrd.open_workbook(filename=filename)
    print(wb.sheet_names())
    sheets = wb.sheet_names()
    sheets_count = len(sheets)
    sheet_list = []
    for i in range(0,sheets_count):
        sheet = wb.sheet_by_index(i)
        sheet_list.append(sheet)
    print('------sheet_list-----',sheet_list)

    for sheet in sheet_list:
        rows = sheet.nrows
        cols = sheet.ncols
        print(rows,cols)
        for i in range(1,rows):
            temp_row_list = []
            for j in range(0,cols):
                print(sheet.cell(i,j).ctype)
                value= sheet.cell(i,j).value
                if sheet.cell(i,j).ctype == 3:
                    value = xlrd.xldate_as_tuple(value,wb.datemode)
                    value = date(*value[:3]).strftime('%Y/%m/%d')
                temp_row_list.append(value)
            print(temp_row_list)

if __name__=="__main__":
    read_excel()
