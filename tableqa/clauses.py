
from tensorflow.keras.models import load_model
from sentence_transformers import SentenceTransformer
from numpy import asarray,argmax
import os

bert_model = SentenceTransformer('bert-base-nli-mean-tokens')
model=load_model(os.path.join(os.path.abspath(os.path.dirname(__file__)),"Question_Classifier.h5"))

class Clause:
    def __init__(self):
        self.types={0:'SELECT {} FROM {}', 1:'SELECT MAX({}) FROM {}', 2:'SELECT MIN({}) FROM {}', 3:'SELECT COUNT({}) FROM {}', 4:'SELECT SUM({}) FROM {}', 5:'SELECT AVG({}) FROM {}'}

    def adapt(self,q,inttype=False,summable=False):
        emb=asarray(bert_model.encode([q]))
        self.clause=self.types[argmax(model.predict(emb),axis=-1)[0]]        
        if summable and inttype  and "COUNT" in self.clause:
            self.clause= '''SELECT SUM({}) FROM {}'''
        return self.clause
    
    


                
                

            

