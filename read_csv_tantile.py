"""
    用途：用来读取csv文件里面的数据，使用pandas将数据做处理求出各列的汇总统计集合（describe）。
    需要注意的：
        1、将处理好的需要计算各列汇总统计集合的数据（待统计数据表）放到此程序的同级目录下；
        2、此程序只对（Product_price, Product_star, Product_review_count, Product_ask_count）几列的数据做汇总统计；
        3、注意数据类型只能是数值；
"""


import csv
import pandas as pd
import numpy as np


def read_category():
    # 读取Product_bestsellers_category的数据并去重
    with open('/Users/zhangjun/Desktop/demo/已处理.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        category_list = []
        for row in reader:
            # 读取ASIN字段数据
            column = row['Product_bestsellers_category']
            if column not in category_list:
                category_list.append(column)
    # print(category_list)
    # print(len(category_list))
    return category_list


def read_detail(category_list):
    for category in category_list:
        with open('/Users/zhangjun/Desktop/demo/已处理.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            my_list = []
            for row in reader:
                if row['Product_bestsellers_category'] == category:
                    list1 = []
                    for k, v in row.items():
                        my_dict = {}
                        # if k == 'Product_price':
                        if k != 'Category_node_id' and k != 'Product_bestsellers_category' and k != 'Product_brand':
                            if v == '':
                                v = np.nan  # numpy的缺省
                            else:
                                v = float(v)
                            list1.append(v)
                    my_list.append(list1)
        frame = pd.DataFrame(my_list)
        # print(frame)
        # print(frame.describe())
        # 求分位置、最大值、标准差
        df = frame.describe().T
        data_list1 = []
        for indexs in df.index:
            lst = list(df.loc[indexs].values[:])
            data_list1.append(lst)
        data_list1.insert(0, [category])
        print(data_list1)
        yield data_list1


def run():
    with open('已处理数据表1.csv', 'a+') as csvfile:
        writer = csv.writer(csvfile)
        table_title_name = ['category',
                            'price_count', 'price_mean', 'price_std', 'price_min', 'price_25%', 'price_50%', 'price_75%', 'price_max',
                            'star_count', 'star_mean', 'star_std', 'star_min', 'star_25%', 'star_50%', 'star_75%', 'star_max',
                            'review_count', 'review_mean', 'review_std', 'review_min', 'review_25%', 'review_50%', 'review_75%', 'review_max',
                            'ask_count', 'ask_mean', 'ask_std', 'ask_min', 'ask_25%', 'ask_50%', 'ask_75%', 'ask_max',
                            ]
        writer.writerow(table_title_name)
        category_list = read_category()
        for data_list in read_detail(category_list):
            data1 = []
            for data in data_list:
                data1 += data
            data_list = data1
            writer.writerow(data_list)


if __name__ == "__main__":
    run()