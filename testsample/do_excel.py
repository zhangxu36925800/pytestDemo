import xlrd
import pandas
'''
通过pytest获取excel中的数据
'''


def get_case_data():
    # 读取文件
    book = xlrd.open_workbook("D:\\Document\\testdata\\pytest_case.xlsx")
    # 指定读取文件中的页面
    sheet1 = book.sheet_by_name('case1')
    case = []
    for i in range(0, sheet1.nrows):
        if i > 0:
            case.append(sheet1.row_values(i)) #row_values(i)获取每一行的数据
            # sheet1.cell(i,0) 获取每一行对应的第一列数据
            # print(case)
    return case

def  pandas_get_case_data():
     sheet1 = pandas.read_excel("D:\\Document\\testdata\\pytest_case.xlsx",header=0)
     return sheet1



if __name__ == "__main__":
    case = get_case_data()
    print("xlrd获取到的结果:{}".format(case))
    datalist = pandas_get_case_data()
    print("pandas获取到的结果:{}".format(datalist.values[1,2]))#获取第一行，索引为第三个的值；不加索引则取全部

