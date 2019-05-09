from sklearn.linear_model import LogisticRegression as LR
import numpy as np
import math
import random

def getidf():
	item_file_count_map={}
	f=open('train.csv',encoding='utf-8')
	file_count=0
	for line in f:
		array=line.strip().split(',')
		if len(array) == 3:
			file_count=file_count+1
			text=array[1]
			items=text.split(' ')
			for item in items:
				if item in item_file_count_map:
					item_file_count_map[item]=item_file_count_map[item]+1
				else:
					item_file_count_map[item]=1
	for item in item_file_count_map:
		item_file_count_map[item]=math.log(file_count/item_file_count_map[item])
	return item_file_count_map

def gettfidf(idf):
	tf_idf_map={}
	f=open('train.csv',encoding='utf-8')
	file_count=0
	for line in f:
		array=line.strip().split(',')
		if len(array) == 3:
			file_count=file_count+1
			text=array[1]
			items=text.split(' ')
			h={}
			for item in items:
				if item in h:
					h[item]=h[item]+1
				else:
					h[item]=1
			for item in h:
				tf=h[item]/len(items)
				print(tf)
				tf_idf=tf*idf[item]
				print(tf_idf)
				print("=======")
				tf_idf_map[item]=tf_idf
	return tf_idf_map

def SplitTrainAndTest():
	f=open('train.csv',encoding='utf-8')
	file_count=0
	for line in f:
		array=line.strip().split(',')
		if len(array) 

if __name__=='__main__':

	x=[[5,6,7],[2,3,4]]
	y=[0,1]

	lr=LR()
	lr.fit(np.array(x),np.array(y))

	x_test=np.array([[1,2,3],[2,3,4]])
	y2=lr.predict(x_test)
	print(y2)
	print(len(y2))
	idf=getidf()
	gettfidf(idf)