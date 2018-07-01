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
def write_excel1():
    #拿到工作空间
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
    row0 = ['业务', '状态', '北京','上海', '广州', '深圳','状态小计', '合计']
    column0 = ['机票', '船票', '火车票', '汽车票', '其它']
    status = ['预订', '出票', '退票', '业务小计']

    #生成第一行
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i],set_style("Times New Roman",220,True))

    # 生成第一列和最后一列（合并4行）
    i,j = 1,0
    while i < 4*len(column0) and j < len(column0):
        sheet1.write_merge(i,i+3,0,0,column0[j],set_style('Arial',220,True))
        sheet1.write_merge(i,i+3,7,7)
        i += 4
        j += 1
    sheet1.write_merge(21, 21, 0, 1, u'合计', set_style('Times New Roman', 220, True))
    # 生成第二列
    m = 0
    while m <4*len(column0):
        for i in range(0,len(status)):
            sheet1.write(i+m+1,1,status[i])
        m += 4
    f.save("simpledemo.xls")

if __name__ == '__main__':
    write_excel1()