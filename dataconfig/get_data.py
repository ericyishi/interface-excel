from dataconfig import data_config
from utils.operate_excel import OperationExcel
from utils.operate_json import OperationJson


class GetData:
    """docstring for GetData"""

    def __init__(self):
        self.opera_excel = OperationExcel()

    # 去获取excel行数,就是case的数量
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取是否执行
    def get_is_run(self, row):
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_vaule(row, col)
        flag = None
        if run_model.lower() == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        col = int(data_config.get_header())
        header = self.opera_excel.get_cell_vaule(row, col)
        if header == 'yes':
            return data_config.get_header_value()
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = int(data_config.get_run_way())
        requests_method = self.opera_excel.get_cell_vaule(row, col)
        return requests_method

    # 获取url
    def get_request_url(self, row):
        col = int(data_config.get_url())
        url = self.opera_excel.get_cell_vaule(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = int(data_config.get_data())
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
        col = int(data_config.get_expect())
        expcet = self.opera_excel.get_cell_vaule(row, col)
        if expcet == '':
            return None
        else:
            return expcet

    # 封装写入数据的方法
    def write_result(self, row, value):
        # 获取实际结果的列
        col = int(data_config.get_result())
        self.opera_excel.write_value(row, col, value)

    # 获取依赖数据的key
    def get_depend_key(self, row):
        col = int(data_config.get_data_depend())
        depent_key = self.opera_excel.get_cell_vaule(row, col)
        if depent_key == "":
            return None
        else:
            return depent_key

    # 判断是否有case依赖
    def is_depend(self, row):
        col = int(data_config.get_case_depend())
        depend_case_id = self.opera_excel.get_cell_vaule(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    # 获取数据依赖字段
    def get_depend_field(self, row):
        col = int(data_config.get_field_depend())
        data=self.opera_excel.get_cell_vaule(row,col)
        if data == "":
            return None
        else:
            return data