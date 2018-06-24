import json

from base.RunMethod import RunMethod
from dataconfig.get_data import GetData
from utils.operate_excel import OperationExcel
from jsonpath_rw import jsonpath,parse

class DependdentData:
    # 通过caseID获取其整行数据
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()

    # 通过case_id 去获取该case_id的整行数据
    def get_case_line_data(self, case_id):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    # 执行依赖测试，获取结果集
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = run_method.run_main(method, url, request_data)
        return json.loads(res)

    # 根据依赖的key去获取执行依赖测试case的响应,然后找到需要数据!
    def get_data_for_key(self, row):
        # 获取依赖的值
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        print("----------》")
        print(type(depend_data))
        print(depend_data)
        print(type(response_data))
        print(response_data)
        # 需要jsonpath_rw,解析为json格式
        json_exe = parse(depend_data)
        # 在相应数数据里面去寻找指定的key对应的值
        madle = json_exe.find(response_data)
        # 相当于for i in madle
        return [math.value for math in madle][0]




if __name__ == "__main__":
	order = {
		"data": {
			"_input_charset": "utf-8",
			"body": "慕课网订单-1710141907182334",
			"it_b_pay": "1d",
			"notify_url": "http://order.imooc.com/pay/notifyalipay",
			"out_trade_no": "1710141907182334",
			"partner": "2088002966755334",
			"payment_type": "1",
			"seller_id": "yangyan01@tcl.com",
			"service": "mobile.securitypay.pay",
			"sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D",
			"sign_type": "RSA",
			"string": "_input_charset=utf-8&body=慕课网订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=慕课网订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA",
			"subject": "慕课网订单-1710141907182334",
			"total_fee": 299
			},
			"errorCode": 1000,
			"errorDesc": "成功",
			"status": 1,
			"timestamp": 1507979239100
		}
	res = "data.out_trade_no"
	json_exe = parse(res)
	madle = json_exe.find(order)
	print([math.value for math in madle][0])
