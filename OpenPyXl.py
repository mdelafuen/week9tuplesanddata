import openpyxl



def examine_income_data(excel_file_name):
    workbook_file = openpyxl.load_workbook(excel_file_name)
    worksheet = workbook_file.active
    for current_row in worksheet.rows:
        state_cell = current_row[0]
        state_name = state_cell.value
        median_income2018 = current_row[1].value
        print(f"{state_name} \t: {median_income2018}")

def main():
    examine_income_data("CensuseMedianIncome.xlsx")

main()