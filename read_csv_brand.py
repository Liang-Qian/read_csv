"""
    用途：用于读取csv中各个类别下所有的brand信息，统计数量及在当前类别下的占比情况
    需要注意的：
        1、将处理好的统计brand的数据（待统计数据表）放到此程序的同级目录下；
"""
import csv


def read_category():
    # 读取Product_bestsellers_category的数据并去重
    with open('./待统计数据表.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        category_list = []
        for row in reader:
            # 读取ASIN字段数据
            column = row['Product_bestsellers_category']
            if column not in category_list:
                category_list.append(column)
    return category_list


def read_detail(category_list):
    for category in category_list:
        with open('./待统计数据表.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            my_list = []
            for row in reader:
                if row['Product_bestsellers_category'] == category:
                    for k, v in row.items():
                        if k == 'Product_brand':
                            my_list.append(v)
        yield (my_list,category)


def run():
    with open('Sports_Outdoors_Brands.csv', 'a+') as csvfile:
        writer = csv.writer(csvfile)
        category_list = read_category()
        for data in read_detail(category_list):
            data_list = data[0]
            category = data[1]
            data_list = list(filter(None, data_list))
            my_set = set(data_list)  # my_set 是另外一个列表，里面的内容是my_list里面的无重复项
            my_list = []
            for item in my_set:
                my_list.append([category, item, data_list.count(item), len(data_list), int(data_list.count(item))/len(data_list)])
            print(my_list)
            for data in my_list:
                writer.writerow(data)


if __name__ == "__main__":
    run()
