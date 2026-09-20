import openpyxl
import os

class ExcelReader:
    @staticmethod
    def get_row_data(sheet_name, tc_id):
        file_path = os.path.join(os.path.dirname(__file__), '../data/test_data.xlsx')
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]
        
        header = [cell.value for cell in sheet[1]]
        
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if row[0] == tc_id:
                return dict(zip(header, row))
        
        raise ValueError(f"Test case ID '{tc_id}' not found in sheet '{sheet_name}'")
