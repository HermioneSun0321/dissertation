from nlptriples import triples,setup
import numpy as np
import pandas as pd

df_triple = pd.read_csv('text.csv')

list_s = []
list_p = []
list_o = []

for i in df_triple.index:
    rdf = triples.RDF_triple()
    triple = rdf.extract(df_triple['sent'][i])
    list_s.append(triple[0])
    list_p.append(triple[1])
    list_o.append(triple[2])
    
df_triple['subject'] = list_s
df_triple['predictae'] = list_p
df_triple['object'] = list_o

df_triple.to_csv("./triple.csv")