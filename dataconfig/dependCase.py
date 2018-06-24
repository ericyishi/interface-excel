from dataconfig.excelRowsConfig import GetData
from utils.operate_excel import OperationExcel


class DependdentData:
    # 通过caseID获取其整行数据
	def __init__(self,case_id):
		self.case_id = case_id
		self.opera_excel = OperationExcel()
		self.data = GetData()