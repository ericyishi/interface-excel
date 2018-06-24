from base.RunMethod import RunMethod
from dataconfig.excelRowsConfig import GetData
from utils.common_util import CommonUtil


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util=CommonUtil()

    def go_on_run(self):
        # 获取case的行数

        rows_count = self.data.get_case_lines()
        print(rows_count)
        for i in range(1,rows_count):
            # 获取需要的列的内容
            url=self.data.get_request_url(i)
            method=self.data.get_request_method(i)
            is_run=self.data.get_is_run(i)
            data=self.data.get_data_for_json(i)
            expect=self.data.get_expcet_data(i)
            header=self.data.is_header(i)
            if is_run:
             print(method,is_run,url,header)
             res=self.run_method.run_main(method,url,data,header)
             if self.com_util.is_contain(expect,res):
                print("测试通过")
                self.data.write_result(i,"pass")
             else:
                 print("测试失败")
                 self.data.write_result(i,"error")
             print(res)
if __name__=='__main__':
    run=RunTest()
    run.go_on_run()
