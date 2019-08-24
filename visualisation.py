import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
path = "C:/Users/swapn/DSP22062019/train.csv"
def boxplot(path):
    pdfile= pd.read_csv(path)
    plt.boxplot(pdfile.dropna(subset=['Age'])['Age'])
    plt.show()
def histogram(path):
    pdfile= pd.read_csv(path)
    plt.hist(pdfile.dropna(subset=['Age'])['Age'])
    plt.show()
if __name__ == "__main__":
    print(boxplot(path))
    print(histogram(path))
    