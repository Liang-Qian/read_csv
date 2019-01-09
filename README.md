# read_csv

This is a program that processes CSV tables and uses pandas to calculate the bitwise values of the data

**一、用途：**

​	1、[read_csv_tantile.py](https://github.com/zhangjun0827/read_csv/blob/master/read_csv_tantile.py)将amazon的Best sellers下的指定类别下各小类别下的整理好的数据使用pandas进行统计，计算各列的分位值、标准差、最大、小值等。

​	2、[read_csv_brand.py](https://github.com/zhangjun0827/read_csv/blob/master/read_csv_brand.py)将amazon的Best sellers下的指定类别下各小类别下的品牌进行统计，计算出不同品牌在不同类别下的占比。	



**二、注意：**

​	1、将amazon的Best sellers下的指定类别的产品详情数据进行处理统计，处理的模版如下：

| **Category_node_id** | **Product_bestsellers_category** | **Product_brand** | **Product_price** | **Product_star** | **Product_review_count** | **Product_ask_count** |
| -------------------- | -------------------------------- | ----------------- | ----------------- | ---------------- | ------------------------ | --------------------- |
| **1_4619352011_1**   | /Patio, Lawn & Garden            | Nature's Blossom  | 19.99             | 3.7              | 953                      | 121                   |
| **1_4619352011_1**   | /Patio, Lawn & Garden            | Twinkle Star      | 17.99             | 4.4              | 2071                     | 318                   |
| **1_4619352011_1**   | /Patio, Lawn & Garden            | ThermoPro         | 59.99             | 4.4              | 4706                     | 352                   |
| **1_4619352011_1**   | /Patio, Lawn & Garden            | Bug-A-Salt        | 39.95             | 4.4              | 3770                     | 524                   |
| **1_4619352011_1**   | /Patio, Lawn & Garden            | ThermoPro         | 30.59             | 4.3              | 3560                     | 191                   |
| **1_4619352011_1**   | /Patio, Lawn & Garden            | Traeger           | 36.395            | 4.5              | 1113                     | 56                    |
| **1_4619352011_1**   | /Patio, Lawn & Garden            | advion            | 26.65             | 4.3              | 14030                    | 744                   |
| **1_4619352011_1**   | /Patio, Lawn & Garden            | Nature's Blossom  | 19.99             | 4                | 277                      | 28                    |
| **1_4619352011_1**   | /Patio, Lawn & Garden            | Planters' Choice  | 27.99             | 3.5              | 185                      | 23                    |
| **1_4619352011_1**   | /Patio, Lawn & Garden            | Shop Succulents   | 12.79             | 3.4              | 989                      | 51                    |

​	2、缺失的数据值或为None的统一替换成空值；



**三、使用：**

​	1、将处理好的数据表放到read_csv_tantile.py和read_csv_brand.py的同级目录下，将一下代码中的代码中的**待统计数据表.csv**改为自己文件名，目前只支持csv文件。

```python
with open('./待统计数据表.csv', 'r') as csvfile:
```

