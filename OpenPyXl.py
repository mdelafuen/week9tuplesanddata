import openpyxl



def examine_income_data(excel_file_name):
    workbook_file = openpyxl.load_workbook(excel_file_name)
    worksheet = workbook_file.active
    for current_row in worksheet.rows:
        pass

def main():
    examine_income_data("CensuseMedianIncome.xlsx")

main()