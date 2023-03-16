import os
import pickle
from pathlib import Path

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]


def get_pickle_path():
    os.getcwd()
    current_directory = Path(os.getcwd())
    pkl_path = os.path.join(current_directory, 'pickle_files')
    return pkl_path

def load_pkl_model(filename):
    pickle_path = get_pickle_path()
    pkl_file = os.path.join(pickle_path, filename + '.pkl')
    model = pickle.load(open(pkl_file,'rb'))
    return model