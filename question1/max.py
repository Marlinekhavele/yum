import xlrd
book = xlrd.open_workbook("data_test.xlsx")
sheet = book.sheet_by_index(0)

def follow_up():
  col = 11
  maximum_kg=max(sheet.col_values(col, start_rowx=1, end_rowx=12))
  
  return maximum_kg

print(follow_up())