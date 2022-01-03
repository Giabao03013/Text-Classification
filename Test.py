import os
import re
import gensim
from tqdm import tqdm
from underthesea import sent_tokenize
from pyvi import ViTokenizer
import pickle
'''
def read_data(folder_path):
    data = []
    labels = []
    dirs = os.listdir(folder_path)
    for path in tqdm(dirs):
        file_paths = os.listdir(os.path.join(folder_path, path))
        for file_path in (file_paths):
            with open(os.path.join(folder_path, path, file_path), 'r', encoding="utf-8") as f:
                lines = f.readlines()
                lines = ' '.join(lines)
                lines = re.sub(
                    r'(?:(?:http|https):\/\/)?([-a-zA-Z0-9.]{2,256}\.[a-z]{2,4})\b(?:\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?',
                    "", lines)
                lines = re.sub(r'<[^>]+>', '', lines)
                #Tien xu li du lieu don gian
                lines = gensim.utils.simple_preprocess(lines)
                lines = ' '.join(lines)

                #Tách từ tiếng Việt
                lines = ViTokenizer.tokenize(lines)
                data.append(lines)
                labels.append(path)

    return data, labels


X_data, y_data = read_data('Data/Train')
pickle.dump(X_data, open('Data_full/X_train.pkl', 'wb'))
pickle.dump(y_data, open('Data_full/Y_train.pkl', 'wb'))

#X_train = pickle.load(open('X_train.pkl','rb'))
#Y_train = pickle.load(open('Y_train.pkl','rb'))
#for line in lines:'''
from itertools import islice, chain, repeat

_no_padding = object()

def chunk(it, size, padval=_no_padding):
    if padval == _no_padding:
        it = iter(it)
        sentinel = ()
    else:
        it = chain(iter(it), repeat(padval))
        sentinel = (padval,) * size
    return list(iter(lambda: tuple(islice(it, size)), sentinel))

def read_data(folder_path):
    data = []
    labels = []
    dirs = os.listdir(folder_path)
    for path in tqdm(dirs):
        file_paths = os.listdir(os.path.join(folder_path, path))
        for file_path in (file_paths):
            with open(os.path.join(folder_path, path, file_path), 'r', encoding="utf-8") as f:
                list_4 = []
                lines = f.read()
                lines = re.sub(
                    r'(?:(?:http|https):\/\/)?([-a-zA-Z0-9.]{2,256}\.[a-z]{2,4})\b(?:\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?',
                    "", lines)
                lines = re.sub(r'<[^>]+>', '', lines)
                lines = re.sub(r'[|\^&+\-%*"/"=!>]','',lines)

                lines = ViTokenizer.tokenize(lines)
                sent = sent_tokenize(lines)
                list_sent = chunk(sent,4)
                data.append(list(list_sent))
                labels.append(path)

    return data, labels

X_data,y_data = read_data('Data/Train')
pickle.dump(X_data, open('Data_full/X_4.pkl', 'wb'))
pickle.dump(y_data, open('Data_full/Y_4.pkl', 'wb'))


