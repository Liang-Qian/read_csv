import pandas as pd
import numpy as np
import math

data_table=pd.read_excel('Garden(12.24-26)评论数.xlsx')

data_array=np.array(data_table)
data_list=data_array.tolist()

data_dict={}

for row in data_list:
	if row[1] in data_dict.keys():
		data_dict[row[1]]['category_rank'].append(row[2])
		data_dict[row[1]]['total_rank'].append(row[13].split('(')[0].strip().split(' in ')[0])
		try:
			data_dict[row[1]]['total_category'].append(row[13].split('(')[0].strip().split(' in ')[1])
		except:
			data_dict[row[1]]['total_category'].append('None')
	else:
		data_dict[row[1]]={'category_rank':[],
							'total_rank':[],
							'total_category':[]
							}
		data_dict[row[1]]['category_rank'].append(row[2])
		data_dict[row[1]]['total_rank'].append(row[13].split('(')[0].strip().split(' in ')[0])
		try:
			data_dict[row[1]]['total_category'].append(row[13].split('(')[0].strip().split(' in ')[1])
		except:
			data_dict[row[1]]['total_category'].append('None')
#print(data_dict)

#计算权重和权重和
for key in data_dict:
	data_dict[key]['category_weight']=[]
	data_dict[key]['sum_weight']=0
	for i in range(len(data_dict[key]['category_rank'])):
		data_dict[key]['category_weight'].append(5-math.log(data_dict[key]['category_rank'][i]))
		data_dict[key]['sum_weight']+=5-math.log(data_dict[key]['category_rank'][i])

#print(i for i in data_dict.values()[:100])

#计算最多的大类
for key in data_dict:
	cate_dict={}
	for cate in data_dict[key]['total_category']:
		if cate in cate_dict.keys():
			cate_dict[cate]+=1
		else:
			cate_dict[cate]=1
	# print(cate_dict)
	# print(sorted(cate_dict.items(),key=lambda cate_dict:cate_dict[1],reverse=True))
	data_dict[key]['max_cate']=sorted(cate_dict.items(),key=lambda cate_dict:cate_dict[1],reverse=True)[0][0]
	data_dict[key]['max_cate_num']=sorted(cate_dict.items(),key=lambda cate_dict:cate_dict[1],reverse=True)[0][1]

#print(i for i in data_dict.values()[:100])

#使用权重函数-ln(x)+5
def weightrank(key,i,j):
	try:
		a=float(data_dict[key]['total_rank'][i].replace(',',''))*data_dict[key]['category_weight'][j]/data_dict[key]['sum_weight']
	except:
		if i==0:
			a=0
		else:
			a=weightrank(key,i-1,j)
	return a

#计算品类加权平均排名
for key in data_dict:
	data_dict[key]['weighted_rank']=0

	for i in range(len(data_dict[key]['total_rank'])):
		j=i
		a=weightrank(key,i,j)
		data_dict[key]['weighted_rank']+=a

#print(data_dict)

output_data={'category':[],
			'max_cate':[],
			'max_cate_num':[],
			'weighted_rank':[]	
				}
for key in data_dict:
	output_data['category'].append(key)
	output_data['max_cate'].append(data_dict[key]['max_cate'])
	output_data['max_cate_num'].append(data_dict[key]['max_cate_num'])
	output_data['weighted_rank'].append(data_dict[key]['weighted_rank'])

#print(output_data)

output_dataframe=pd.DataFrame.from_dict(output_data)

output_dataframe.to_excel('Garden.xlsx')
print(output_dataframe)

# data_dict={'category':[],
# 			'category_rank':[],
# 			'total_rank':[],
# 			'total_category':[]
# 			}

# tem_list=[]
# for row in data_list:
# 	tem_list.append(row[13].split('(')[0].strip().split(' in '))

# print(tem_list)

# for j in tem_list:
# 	data_dict['total_rank'].append(j[0])
# 	try:
# 		data_dict['total_category'].append(j[1])
# 	except:
# 		data_dict['total_category'].append('None')

# print(data_dict)