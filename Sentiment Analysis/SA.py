# HelpMate User Comment Sentiment Analysis

import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.compat.v1.keras.layers import CuDNNGRU
from tensorflow.keras.layers import LeakyReLU, Dropout
from tensorflow.keras.layers import Conv1D
from tensorflow.keras.layers import MaxPooling1D
from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing import sequence

max_review_length=1000
NUM_WORDS=10000 # only use top 1000 words
INDEX_FROM=3   # word index offset

train,test = keras.datasets.imdb.load_data(num_words=NUM_WORDS, index_from=INDEX_FROM)
xtr,ytr = train
xte,yte = test
xtr = sequence.pad_sequences(xtr, padding='pre', maxlen=max_review_length)
xte = sequence.pad_sequences(xte, padding='pre', maxlen=max_review_length)

embedding_vecor_length =64
bs=32
ep=2
num_classes=2 

ytr1 = keras.utils.to_categorical(ytr, num_classes)
yte1 = keras.utils.to_categorical(yte, num_classes)

rl=LeakyReLU(alpha=.01)

model = Sequential()
model.add(Embedding(NUM_WORDS, embedding_vecor_length, input_length=max_review_length))
# model.add(Dropout(0.5))
model.add(Conv1D(filters=64, kernel_size=3, padding='same', activation=rl))
model.add(MaxPooling1D(pool_size=2))
model.add(Dropout(0.5))
model.add(CuDNNGRU(50, return_sequences=True))
model.add(CuDNNGRU(50))
model.add(Dropout(0.3))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# print(model.summary())
model.fit(xtr, ytr1, epochs=ep, batch_size=bs, validation_data=(xte, yte1))
