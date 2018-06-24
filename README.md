# interface-excel
### 文件结构
```
 --- base
  |
 --- data 存放数据
  |--case1.xml 用例
  |--user.json 将请求的数据抽离出来
 --- dataconfig
  |--excelRowsConfig.py文件行的数据的设置
  |--excelColsConfig.py文件列的数据关联设置
 --- main 主流程
  |--run_test.py 入口文件
 --- utils 工具类
  |--common_util.py 公用工具类
  |--operate_excel.py 操作excel文件
  |--operate_json.py 操作json文件
  |--SendEmail.py 发送邮件
```
### 注意
1. 向excel写入数据，不能直接使用xlrt，原来内容会被清除
   * 解决：
    ```
     def write_value(self,row,col,value):
    # 先将原来数据读取出来，复制一份，如果直接操作原来的数据会丢失
	    read_data = xlrd.open_workbook(self.filename)
    # 需要安装xlutils包,copy，write，save是其方法来做写操作
	    write_data = copy(read_data)
	    sheet_data = write_data.get_sheet(0)
	    sheet_data.write(row,col,value)
	    write_data.save(self.filename)
    ```

### excel下的三个数据字段说明
 * case依赖：当前case依赖于哪一个dependentcase
 * 依赖的返回数据：取dependentcase返回相应数据里面的哪个字段的数据
   * 还需要考虑哪一层的哪一个字段【例如返回的数据有多个，需要的为第二个子集下面的name】
 * 数据依赖字段：将dependentcase获取的字段作用于当前case的哪个字段下
 
### 待优化
 * 异常处理