import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df =  pd.read_csv("train.csv")
def getnumpyarray(dft,colname):
   return dft[colname].to_numpy()
#nulls per column
def getnumpyarray(dft,colname):
   return dft[colname].to_numpy()
#def reject_outliers(data, m=2):
#   return data[abs(data - np.mean(data)) < m * np.std(data)]
def spread(data_1):
   return np.std(data_1)
def get_outlier(data_1):
   outliers=[]
   threshold=3
   mean_1 = np.mean(data_1)
   std_1 =spread(data_1)
   for y in data_1:
       z_score= (y - mean_1)/std_1
       if np.abs(z_score) > threshold:
           outliers.append(y)
   return outliers
def get_iqr(data_1):
   q1, q3= np.percentile(sorted(data_1),[25,75])
   iqr=(q3 - q1)
   return {'standard_dev':spread(data_1), 'iqr':iqr,'lower_bound':(q1 -(1.5 * iqr)),'upper_bound':(q3 +(1.5 * iqr))}
age_nparry=getnumpyarray(df,"Age")
def boxplot(path):
    plt.boxplot(path.dropna(subset=['Age'])['Age'])
    plt.show()
def histogram(path):
    plt.hist(path.dropna(subset=['Age'])['Age'])
    plt.show()
if __name__ == "__main__":
    print(boxplot(df))
    print(histogram(df))
    print(get_outlier(age_nparry))
