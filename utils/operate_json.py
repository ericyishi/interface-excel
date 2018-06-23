import json
class OperationJson(object):
    """操作json，将请求的参数封装在json文件中"""

    def __init__(self):
        self.data = self.read_data()

    # 读取jsson文件
    def read_data(self):
        with open('../data/user.json') as fp:
            data = json.load(fp)
        return data

    # 根据关键字获取数据
    def get_data(self, id):
        return self.data[id]

if __name__ == '__main__':
    opjson = OperationJson()
    print(opjson.get_data('szlist'))