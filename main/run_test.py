from base.RunMethod import RunMethod
from dataconfig.dependCase import DependdentData
from dataconfig.get_data import GetData
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
            is_run=self.data.get_is_run(i)
            if is_run:
                url=self.data.get_request_url(i)
                method=self.data.get_request_method(i)

                request_data=self.data.get_data_for_json(i)
                expect=self.data.get_expcet_data(i)
                header=self.data.is_header(i)
                depend_case=self.data.is_depend(i)
                if depend_case!=None:
                    self.depend_data=DependdentData(depend_case)
                    # 获取依赖响应的数据【依赖case里面的数据】
                    depend_response_data=self.depend_data.get_data_for_key(i)
                    # 获取依赖的key
                    depend_key=self.data.get_depend_field(i)
                    # 更新请求数据里面的内容
                    request_data[depend_key]=depend_response_data
                res=self.run_method.run_main(method,url,request_data,header)
                print(res)
                if self.com_util.is_contain(expect,res):
                    print("测试通过")
                    self.data.write_result(i,"pass")
                else:
                    print("测试失败")
                    self.data.write_result(i,"error")

if __name__=='__main__':
    run=RunTest()
    run.go_on_run()
