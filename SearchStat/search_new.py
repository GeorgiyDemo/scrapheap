# -*- coding: utf-8 -*-
from pytils import numeral
import os, xlrd, time
from keras import backend as K
from keras.models import model_from_json
from utils import *

#кол-во ячеек в таблице
count_range = 153

kun = 0
tyan = 0
i=1
book = xlrd.open_workbook("CONF.xlsx")
first_sheet = book.sheet_by_index(0)

model_dir = './output'
K.set_learning_phase(0)
with open(os.path.join(model_dir, 'model.json'), 'r') as fp:
    model = model_from_json(fp.read())

model.compile(loss='categorical_crossentropy', optimizer='adam',
              metrics=['accuracy'])
model.load_weights(os.path.join(model_dir, 'model.h5'))

def predict(m, word):
    out = m.predict(np.array([word2input(word, 50)]))
    return np.argmax(out[0])

def OutWork(result,files):
    f = open(files, 'a')
    f.write(result+"\n")
    f.close()

while i < count_range:
	this_name = first_sheet.cell(i,0).value
	print(this_name)

	if predict(model,this_name) == 2:
		OutWork(this_name,"TYAN")
		tyan = tyan + 1

	if predict(model,this_name) == 1:
		OutWork(this_name,"KUN")
		kun = kun + 1

	i = i + 1

print("Кол-во кунов: "+str(kun))
print("Кол-во тянок: "+str(tyan))
