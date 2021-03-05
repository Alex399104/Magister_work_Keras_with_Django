from keras.models import load_model
from FnsCnslt.CreatNeiron import CrtNrn
import numpy as np
import os.path

patchModel = 'FnsCnslt/static/img/model.png'
patchMean1 = "mean1file.txt"
patchStd1 = "std1file.txt"
def tmp():
    global NrFnRes, mean1, std1
    NrFnRes = load_model('NrMdl.h5')
    ReadMean1 = np.loadtxt( patchMean1, delimiter='\t', dtype=np.float)
    mean1 = np.array([ReadMean1])
    ReadStd1 = np.loadtxt( patchStd1, delimiter='\t', dtype=np.float)
    std1 = np.array([ReadStd1])


if os.path.isfile('NrMdl.h5') and  os.path.isfile(patchModel) and os.path.isfile(patchMean1) and os.path.isfile(patchStd1):
    tmp()
else:
    CrtNrn()
    tmp()