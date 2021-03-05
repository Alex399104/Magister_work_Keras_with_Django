import numpy as np
from keras.models import Model
from keras.layers import Input
from keras.layers.core import Dense
from keras.layers.recurrent import LSTM
from keras.layers import Reshape, LeakyReLU, BatchNormalization
from keras.utils import plot_model

def CrtNrn():
    ReadFile = np.loadtxt("DataFile.txt", delimiter='\t', dtype=np.float)

    DataNeuron = np.array([ReadFile])
    DataNeuron = DataNeuron.reshape(20,10)
   
    mean1 = np.mean(DataNeuron, axis=0)
    np.savetxt('mean1file.txt', mean1)
    std1 = np.std(DataNeuron, axis=0)
    np.savetxt('std1file.txt', std1)
    DataNeuron = (DataNeuron - mean1)/std1

    DataTrain = DataNeuron[:16]
    DataTest = DataNeuron[16:]
    DataTrain = DataTrain.reshape(16,10)
    DataTest = DataTest.reshape(4,10)

    allinput = Input(batch_shape=(None,10))

    NrFnRes1_1 = Dense(10, kernel_initializer='random_normal')(allinput)
    NrFnRes1_2 = Dense(9, kernel_initializer='random_normal')(NrFnRes1_1)
    LkRl1_1 = LeakyReLU(0.1)(NrFnRes1_2)
    BtchNrmlz1_1 = BatchNormalization()(LkRl1_1)
    NrFnRes1_3 = Dense(8, kernel_initializer='random_normal')(BtchNrmlz1_1)
    LkRl1_2 = LeakyReLU(0.1)(NrFnRes1_3)
    NrFnRes1_4 = Dense(9, kernel_initializer='random_normal')(LkRl1_2)
    LkRl1_3 = LeakyReLU(0.1)(NrFnRes1_4)
    NrFnRes1_5 = Dense(10, kernel_initializer='random_normal')(LkRl1_3)
  
    LSTMInpt = Reshape((10,1))(allinput)
    NrFnRes2_1 = LSTM(10, kernel_initializer='random_normal', return_sequences=True)(LSTMInpt)
    NrFnRes2_2 = LSTM(9, kernel_initializer='random_normal', return_sequences=True)(NrFnRes2_1)
    LkRl2_1 = LeakyReLU(0.1)(NrFnRes2_2)
    BtchNrmlz2_1 = BatchNormalization()(LkRl2_1)
    NrFnRes2_3 = LSTM(8, kernel_initializer='random_normal', return_sequences=True)(BtchNrmlz2_1)
    LkRl2_2 = LeakyReLU(0.1)(NrFnRes2_3)
    NrFnRes2_4 = LSTM(9, kernel_initializer='random_normal', return_sequences=True)(LkRl2_2)
    LkRl2_3 = LeakyReLU(0.1)( NrFnRes2_4)
    NrFnRes2_5 = LSTM(10, kernel_initializer='random_normal')(LkRl2_3)
    
    NrFnRes = Model(inputs=allinput, outputs=(NrFnRes1_5, NrFnRes2_5))

    # Компилируем модель
    NrFnRes.compile(loss="mse", 
                    optimizer="adam", 
                    metrics=["mae"])
    
    
    # Обучаем сеть
    history = NrFnRes.fit(DataTrain, [DataTrain, DataTrain], batch_size=2, epochs=160, verbose=1)
    
    # Оцениваем качество обучения сети на тестовых данных
    scores = NrFnRes.evaluate(DataTest, [DataTest, DataTest], verbose=1)
    print("Доля верных ответов на тестовых данных, в процентах:", round((scores[1] * 10)/2, 2))
    
    NrFnRes.save('NrMdl.h5')
    plot_model(NrFnRes, to_file='FnsCnslt/static/img/model.png', show_shapes=True)
    