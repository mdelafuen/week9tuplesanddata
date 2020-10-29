import openpyxl
import numbers
import openpyxl.utils


def examine_income_data(excel_file_name):
    workbook_file = openpyxl.load_workbook(excel_file_name)
    worksheet = workbook_file.active
    for current_row in worksheet.rows:
        state_cell = current_row[0]
        state_name = state_cell.value
        median_income2018 = current_row[1].value
        if not isinstance(median_income2018, numbers.Number):
            continue # if not number, continue the loop
        #print(f"{state_name}\t: {median_income2018}")
        median2016col_number = openpyxl.utils.cell.column_index_from_string('H')-1
        median2016_income = current_row[median2016col_number].value
        change_in_income = median_income2018 - median2016_income
        if change_in_income <0:
            print(f"{state_name}\t: {change_in_income}")


def main():
    examine_income_data("CensuseMedianIncome.xlsx")

main()