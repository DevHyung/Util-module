from openpyxl import  load_workbook

tEx = load_workbook(filename='test.xlsx')
sheet1 = tEx['Sheet1']

sheet2 = tEx.active

ts = []
for i in sheet1.rows:
    num = i[0].value
    keyword = i[1].value
    domain = i[2].value
    address = i[3].value
    #작업번호 비어있으면 ? ?
    if num == None:
        num = 'X'
    t = (num, keyword, domain, address)
    ts.append(t)

print(ts)
