import os
import re
import gensim
import pickle
from tqdm import tqdm
from pyvi import ViTokenizer
from underthesea import word_tokenize


def read_data(folder_path):
    data = ''
    dirs = os.listdir(folder_path)
    for path in tqdm(dirs):
        file_paths = os.listdir(os.path.join(folder_path, path))
        for file_path in (file_paths):
            with open(os.path.join(folder_path, path, file_path), 'r',encoding='utf-8') as f:
                lines = f.read()
                lines = re.sub(
                    r'(?:(?:http|https):\/\/)?([-a-zA-Z0-9.]{2,256}\.[a-z]{2,4})\b(?:\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?',
                    "", lines)

                lines = re.sub(r'<[^>]+>', '', lines)
                #               Tien xu li du lieu don gian
                # lines = gensim.utils.simple_preprocess(lines)
                lines = ' '.join(lines)

                #               Tách từ tiếng Việt
                data += lines
    return data

Train= read_data('Data')
pickle.dump(Train,open('Data_full/Old_train.pkl', 'wb'))
X_train = pickle.load(open('Data_full/Old_train.pkl','rb'))
print(X_train)
#X_data,y_data = read_data('Data/Train')
#pickle.dump(X_data, open('Data_full/X_train_1.pkl', 'wb'))
#pickle.dump(y_data, open('Data_full/Y_train_1.pkl', 'wb'))
#x_test, y_test = read_data('Data/Test')
#pickle.dump(x_test, open('Data_full/X_test_1.pkl', 'wb'))
#pickle.dump(y_test, open('Data_full/Y_test_1.pkl', 'wb'))
#X_train = pickle.load(open('Data_full/X_4.pkl','rb'))
#print(X_train)'''

