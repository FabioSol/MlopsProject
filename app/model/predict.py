import pickle
import pandas as pd
from typing import Iterable
import numpy as np
from aids_project.model import model

def model_predict(l:list):
    column_names = ['pidnum', 'time', 'trt', 'age', 'wtkg', 'hemo', 'homo', 'drugs',
                    'karnof', 'oprior', 'z30', 'zprior', 'preanti', 'race', 'gender',
                    'str2', 'strat', 'symptom', 'treat', 'offtrt', 'cd40', 'cd420', 'cd80',
                    'cd820']
    if isinstance(l[0],(int,float)):
        data = pd.DataFrame(l, columns=column_names)
    elif isinstance(l[0], Iterable):
        data = pd.DataFrame(np.array(l), columns=column_names)
    else:
        raise NotImplementedError



    predictions = model.predict_proba(data)
    return predictions


if __name__ == '__main__':
    model_predict([[10140.0, #pidnum
                   1181.0, #time
                   1.0, #trt
                   46.0,# age
                   88.9056,#wtkg
                   0.0,#hemo
                   1.0,#homo
                   1.0,#drugs
                   100.0,#karnof
                   0.0, #oprior
                   1.0,#z30
                   1.0,#zprior
                   1181.0,#preanti
                   0.0,# race
                   1.0,#gender
                   1.0,#str2
                   3.0,#strat
                   0.0,#symptom
                   1.0,#treat
                   0.0,#offtrt
                   235.0,#cd40
                   339.0,#cd420
                   860.0,#cd80
                   1060.0]]*2)#cd820

