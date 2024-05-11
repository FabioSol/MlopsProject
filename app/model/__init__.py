import pickle
import os

model_path = os.path.dirname(__file__)+'/model.pkl'


with open(model_path, 'rb') as f:
    model = pickle.load(f)
