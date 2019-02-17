import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('excel-709026db8bec.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open("test").sheet1

wks.update_acell('A1', "TEST")
wks.update_acell('B2', "it's down there somewhere, let me take another look.")

# Fetch a cell range
cell_list = wks.range('A7:C11')
for cell in cell_list:
    cell.value = 'O_o'
# Update in batch
wks.update_cells(cell_list)


val = wks.acell('B2').value
print(val)


list_of_lists = wks.get_all_values()
for row in list_of_lists:
    for col in row:
        print (col)
 
