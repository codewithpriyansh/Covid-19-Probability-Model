import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

def data_split(data, ratio):
    np.random.seed(42)
    shuffeld = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio)
    test_indices = shuffeld[:test_set_size]
    train_indices = shuffeld[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

if __name__ == "__main__":

    # Reading of data

    df = pd.read_csv('Book1.csv')
    train, test = data_split(df, 0.2)

    x_train = train[['fever', 'bodypain', 'age', 'runny nose', 'diffbreath']].to_numpy()
    x_test = test[['fever', 'bodypain', 'age', 'runny nose', 'diffbreath']].to_numpy()

    y_train = train[['infectionprob']].to_numpy().reshape(17478, )
    y_test = test[['infectionprob']].to_numpy().reshape(4369, )

    clf = LogisticRegression()
    clf.fit(x_train, y_train)

    file = open('model.pkl', 'wb')
    pickle.dump(clf, file)
    file.close()




    


