import xlrd
class OperationExcel():
    def __init__(self, filename=None, sheets=None):
        if filename:
            self.filename = filename
            self.sheet_id = sheets
        else:
            self.filename = '../data/case1.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheet的所有内容
    def get_data(self):
        data = xlrd.open_workbook(self.filename)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_vaule(self, row, col):
        return self.data.cell_value(row, col)

if __name__ == '__main__':
    opers = OperationExcel()
    # print(opers.get_data().nrows)
    # print(opers.get_data().cell_value(2, 3))
    # print(opers.get_lines())
    print(opers.get_cell_vaule(2, 2))
    