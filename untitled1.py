# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11q08pVRZWV1gHmYnDaU-ypqfs9gkvsr8
"""

from google.colab import files

files.upload()

import pandas as pd

dados = pd.read_csv('Bicicletas.csv')

dados.head()

dados.shape

import matplotlib.pyplot as plt

plt.scatter(dados['temperatura'],dados['bicicletas_alugadas'])
plt.ylabel('bicicletas')
plt.xlabel('temperatura')

plt.scatter(dados['clima'],dados['bicicletas_alugadas'])
plt.ylabel('bicicletas_alugadas')
plt.xlabel('clima')
indice = [1,2,3]
plt.xticks(indice,fontsize=14)

import numpy as np

y = dados['bicicletas_alugadas'].values

x = dados [['clima','temperatura']].values
print(x)

x = x/np.amax(x,axis=0)
print(x)

ymax = np.amax(y)

y =y/ymax

