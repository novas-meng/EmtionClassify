
def readWords():
	f=open('train.csv',encoding='utf-8')
	item_emotion_map={}
	for line in f:
		array=line.strip().split(',')
		if len(array) == 3:
			#print(len(array))
			#print(line)
			text=array[1]
			label=array[2]
			for item in text.split(' '):
				if item not in item_emotion_map:
					h={}
					h[label]=1
					item_emotion_map[item]=h
				else:
					h=item_emotion_map[item]
					if label in h:
						h[label]=h[label]+1
					else:
						h[label]=1
	return item_emotion_map

if __name__=='__main__':
	h=readWords()
	print(len(h))
