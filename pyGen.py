import csv
import array
import pandas
import pickle
import pprint
import os
import sys
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
csvFile=open('CSV_Data/newfrequency300.csv', 'rt')
csvReader=csv.reader(csvFile)
print('Reading stop_words from database...')
mydict={row[1]: int(row[0]) for row in csvReader}
pprint.pprint(mydict)
print('<===================================================================================>')

y=[]
print('Training Model for Judging/Perception')
with open ('CSV_Data/PJFinaltest.csv', 'rt') as f:
	reader=csv.reader(f)
	corpus=[rows[0] for rows in reader]

with open ('CSV_Data/PJFinaltest.csv', 'rt') as f:
	csvReader1=csv.reader(f)
	for rows in csvReader1:
		y.append([int(rows[1])])
vectorizer=TfidfVectorizer(vocabulary=mydict,min_df=1)
x=vectorizer.fit_transform(corpus).toarray()
result=np.append(x,y,axis=1)
X=pandas.DataFrame(result)
model=GaussianNB()
train = X.sample(frac=0.8, random_state=1)
test=X.drop(train.index)
y_train=train[301]
y_test=test[301]
print(train.shape)
print(test.shape)
xtrain=train.drop(301,axis=1)
xtest=test.drop(301,axis=1)
model.fit(xtrain,y_train)
pickle.dump(model, open('Pickle_Data/BNPJFinal.sav', 'wb'))
del result

print('<===================================================================================>')
y=[]
print('Training Model for Introversion/Extraversion')
with open ('CSV_Data/IEFinaltest.csv', 'rt') as f:
	reader=csv.reader(f)
	corpus=[rows[0] for rows in reader]

with open ('CSV_Data/IEFinaltest.csv', 'rt') as f:
	csvReader1=csv.reader(f)
	for rows in csvReader1:
		y.append([int(rows[1])])
vectorizer=TfidfVectorizer(vocabulary=mydict,min_df=1)
x=vectorizer.fit_transform(corpus).toarray()
result=np.append(x,y,axis=1)
X=pandas.DataFrame(result)
model=GaussianNB()
train = X.sample(frac=0.8, random_state=1)
test=X.drop(train.index)
y_train=train[301]
y_test=test[301]
print(train.shape)
print(test.shape)
xtrain=train.drop(301,axis=1)
xtest=test.drop(301,axis=1)
model.fit(xtrain,y_train)
pickle.dump(model, open('Pickle_Data/BNIEFinal.sav', 'wb'))
del result

print('<===================================================================================>')
y=[]
print('Training Model for Thinking/Feeling')
with open ('CSV_Data/TFFinaltest.csv', 'rt') as f:
	reader=csv.reader(f)
	corpus=[rows[0] for rows in reader]

with open ('CSV_Data/TFFinaltest.csv', 'rt') as f:
	csvReader1=csv.reader(f)
	for rows in csvReader1:
		y.append([int(rows[1])])
vectorizer=TfidfVectorizer(vocabulary=mydict,min_df=1)
x=vectorizer.fit_transform(corpus).toarray()
result=np.append(x,y,axis=1)
X=pandas.DataFrame(result)
model=GaussianNB()
train = X.sample(frac=0.8, random_state=1)
test=X.drop(train.index)
y_train=train[301]
y_test=test[301]
print(train.shape)
print(test.shape)
xtrain=train.drop(301,axis=1)
xtest=test.drop(301,axis=1)
model.fit(xtrain,y_train)
pickle.dump(model, open('Pickle_Data/BNTFFinal.sav', 'wb'))
del result

print('<===================================================================================>')
y=[]
with open ('CSV_Data/SNFinaltest.csv', 'rt') as f:
	reader=csv.reader(f)
	corpus=[rows[0] for rows in reader]

with open ('CSV_Data/SNFinaltest.csv', 'rt') as f:
	csvReader1=csv.reader(f)
	for rows in csvReader1:
		y.append([int(rows[1])])
vectorizer=TfidfVectorizer(vocabulary=mydict,min_df=1)
x=vectorizer.fit_transform(corpus).toarray()
result=np.append(x,y,axis=1)
X=pandas.DataFrame(result)
model=GaussianNB()
train = X.sample(frac=0.8, random_state=1)
test=X.drop(train.index)
y_train=train[301]
y_test=test[301]
print(train.shape)
print(test.shape)
xtrain=train.drop(301,axis=1)
xtest=test.drop(301,axis=1)
model.fit(xtrain,y_train)
pickle.dump(model, open('Pickle_Data/BNSNFinal.sav', 'wb'))
