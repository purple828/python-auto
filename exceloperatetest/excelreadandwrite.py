import xlwt

'''写excel    xlwt'''

#设置表格样式
def set_style(name,height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.colour_index = 4
    font.height = height
    style.font = font
    return style

#写 excel
def write_excel():
    #拿到工作空间
    f = xlwt.Workbook()
    #添加一个sheet
    sheet1 = f.add_sheet('student',cell_overwrite_ok=True)
    #为第一行，以及第一列 定义数据内容
    row0 = ['姓名','性别','年龄','出生日期','爱好']
    colum0 = ['张三','李四','小华','小方','小红','小明']

    #将准备的第一行数据写入excel中
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i],set_style("Times New Roman",220,True))

    # 将准备的第一列数据写入excel中
    for j in range(0,len(colum0)):
        sheet1.write(j+1,0,colum0[j],set_style("Times New Roman",220,True))

    sheet1.write(1,3,'2018/07/01')

    sheet1.write_merge()

    f.save("text.xls")

if __name__ == '__main__':
    write_excel()

