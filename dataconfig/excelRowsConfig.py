from dataconfig import excelColsConfig
from utils.operate_excel import OperationExcel
from utils.operate_json import OperationJson


class GetData(object):
    """docstring for GetData"""

    def __init__(self):
        self.opera_excel = OperationExcel()

    # 去获取excel行数,就是case的数量
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取是否执行
    def get_is_run(self, row, low):
        col = excelColsConfig.get_run()
        run_model = self.opera_excel.get_cell_vaule(row, col)
        flag = None
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        col = excelColsConfig.get_header()
        header = self.opera_excel.get_cell_vaule(row, col)
        if header == 'yes':
            return excelColsConfig.get_header_value()
        else:
            return None

    # 获取请求方式
    def data_request_method(self, row):
        col = excelColsConfig.get_request_way()
        requests_method = self.opera_excel.get_cell_vaule(row, col)
        return requests_method

    # 获取url
    def get_request_url(self, row):
        col = excelColsConfig.get_url()
        url = self.opera_excel.get_cell_vaule(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = excelColsConfig.get_data()
        data = self.opera_excel.get_cell_vaule(row, col)
        if data == '':
            return None
        else:
            return data

    # 通过获取关键字拿到data数据
    # 获取json配置中的值
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    # 获取预期结果
    def get_expcet_data(self, row):
        col = excelColsConfig.get_expect()
        expcet = self.opera_excel.get_cell_vaule(row, col)
        if expcet == '':
            return None
        else:
            return expcet