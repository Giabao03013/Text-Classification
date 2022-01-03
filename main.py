import re
import pandas as pd
from os import listdir,sep
from underthesea import sent_tokenize
from pyvi import ViTokenizer

def preProcess(text):
    text = re.sub(r'(?:(?:http|https):\/\/)?([-a-zA-Z0-9.]{2,256}\.[a-z]{2,4})\b(?:\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?',
                     "", text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[|\^&+\-%*"/"=!>]','',text)
    text = re.sub(r'[,?()""]','',text)
    #text = re.sub(r'([^\s\w]|_)+', ' ', text)
    text = re.sub(r'\d+','',text)
    text = text.replace('.','. ')
    text = text.lower().strip()
    return text

def loadData(data_folder):
    label_sent= ' '
    for folder in listdir(data_folder):
        for file in listdir(data_folder + sep + folder):
            with open(data_folder + sep + folder + sep + file, 'r', encoding="utf-8") as f:
                text = f.read()
                text = preProcess(text)
                sentences = sent_tokenize(text)
                for sent in sentences:
                    if(len(sent.split())>10 and len(sent.split()) <= 50):
                        label_sent += folder + '///'+ str(sent) +'\n'
                s = open('Data_full/Data_test_full.txt', 'w+', encoding='utf-8')
                s.write(label_sent)

filename = 'stopwords.csv'
data = pd.read_csv(filename, sep="\t", encoding='utf-8')
list_stopwords = data['stopwords']
def remove_stopword(text):
    pre_text = []
    words = text.split()
    for word in words:
        if word not in list_stopwords:
            pre_text.append(word)
    text2 = ' '.join(pre_text)
    return text2

def word_tokenize(file):
    r = open(file,'r',encoding='utf-8')
    sent = ''
    sentences_list=r.readlines()
    for sentece in sentences_list:
        if (len(sentece.split()) < 5):
            sentences_list.remove(sentece)
        sentece = re.sub(r"[-()#@;:<>{}`+=~|!?,]", "", sentece)
        tokenize = ViTokenizer.tokenize(sentece)
        tokenize = remove_stopword(tokenize)
        sent += tokenize + '\n'
    s = open('Data_full/Train.txt','w+',encoding='utf-8')
    s.write(sent)

#loadData("Data/Test")
word_tokenize("Data_full/Data_train_full.txt")



