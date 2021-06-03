import os

import xlrd
import time


def main(file_list):
    for file in file_list:
        deal_file(file)


# 读取文件，并生成新的TXT文件
def deal_file(file_path):
    # 打开excel文件，创建一个workbook对象,book对象也就是fruits.xlsx文件,表含有sheet名
    rbook = xlrd.open_workbook(file_path)
    # xls默认有3个工作簿,Sheet1,Sheet2,Sheet3
    rsheet = rbook.sheet_by_index(0)  # 取第一个工作簿
    file = create_file()
    for row in rsheet.get_rows():
        code = row[0]  # 品名所在的列
        product_value = code.value  # 项目名
        if product_value != '股票代码':  # 排除第一行
            price_column = row[1]  # 价格所在的列
            price_value = price_column.value
            if isinstance(product_value, float):
                temp = str(product_value)
                product_value = temp.split('.')[0]
            # 打印
            print("股票代码", product_value, "股票名称", price_value)
            file.write(product_value + '==' + price_value)
            file.write('\n')
    delete_file(file_path)

# 创建写出文件
def create_file():
    file_name = time.strftime("%Y%m%d%H%M%S", time.localtime())
    file_path = 'C:/test/' + file_name + '.txt'
    file = open(file_path, 'w')
    return file


# 获取指定目录下的文件
def get_file_list(file_path):
    file_list = []
    for top, dirs, nondirs in os.walk(file_path):
        for item in nondirs:
            file_list.append(os.path.join(top, item))
    return file_list


# 删除文件
def delete_file(path):
    if os.path.exists(path):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(path)
    else:
        print('no such file:%s',path)  # 则返回文件不存在


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_list = get_file_list('C:/input/')
    main(file_list)
