import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
path= "C:\Users\Vaibhav\Desktop\DSP19\train.csv"
def boxplot(path):
   titanic= pd.read_csv(path)
   plt.boxplot(titanic.dropna(subset=['Age'])['Age'])
   plt.show()
if __name__ == "__main__":
   print(boxplot(path))