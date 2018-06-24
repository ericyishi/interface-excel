import xlrd
from xlutils.copy import copy


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

    # 写入数据至excel
    def write_value(self, row, col, value):
        # 先将原来数据读取出来，复制一份，如果直接操作原来的数据会丢失
        read_data = xlrd.open_workbook(self.filename)
        # 需要安装xlutils包,copy，write，save是其方法来做写操作
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.filename)

    # 根据对应caseID找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    # 根据对应的caseid找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_cols_data()
        # 因为会从标题开始，所以可以num为0的时候是找不到的
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num + 1

    # 根据行号，获取该行的内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某列的内容
    def get_cols_data(self, col_id=None):
        if (col_id != None):
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    opers = OperationExcel()
    # print(opers.get_data().nrows)
    # print(opers.get_data().cell_value(2, 3))
    # print(opers.get_lines())
    # print(opers.get_cell_vaule(2, 2))
    print(opers.get_row_num('Imooc-12'))
    print(opers.get_rows_data('Imooc-12'))
