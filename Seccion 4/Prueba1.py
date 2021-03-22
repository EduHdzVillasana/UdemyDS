import pandas as pd
import os
mainpath = "E:/Curso de Python/Repositorio/python-ml-course/datasets"
filename = "titanic/titanic3.csv"
fullpath = os.path.join(mainpath, filename)
data = pd.read_csv(fullpath)
print("\n DATASET ORIGINAL\n" , data.tail())

data_2 = pd.read_csv(fullpath)
#data_2 = data Funciona como un puntero, lo que modifiques en data_2 lo modificarás en data

data_2["home.dest"] = data_2["home.dest"].fillna("Desconocido")
print("\n DATASET MODIFICADO\n" , data_2.tail())

print("\n\n DATASET ORIGINAL OTRA VEZ\n" , data.tail())