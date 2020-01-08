import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
import pandas as pd
import numpy as np

class scattertest:
    def __init__(self):
        pass

    def test(self):
        #350페이지
        #csv로드
        #\s+ -> 인식안돔
        df = pd.read_csv('./data/Output.csv', header=None, sep=",")
        print(df)
        df.columns = ['date', 'last', 'byyesterday', 'value', 'high', 'low', 'count']
        df.head()

        #산점도
        cols = [ 'last', 'byyesterday', 'value', 'low', 'count']
        #sns.pairplot(df[cols])
        #plt.tight_layout()
        #plt.show()

        #상관관계
        cm = np.corrcoef(df[cols].values.T)
        sns.set(font_scale=1.5)
        hm = sns.heatmap(cm,
                         cbar=True,
                         annot=True,
                         square=True,
                         fmt='.2f',
                         annot_kws={'size':15},
                         yticklabels=cols,
                         xticklabels=cols
                         )
        plt.tight_layout()
        plt.show()


