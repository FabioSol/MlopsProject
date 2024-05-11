import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

def clean_data(X: pd.DataFrame):
    X = X.copy()
    X = X.set_index(['pidnum'])

    Q1 = X['wtkg'].quantile(0.25)
    Q3 = X['wtkg'].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    X = X[(X['wtkg'] >= lower_bound) & (X['wtkg'] <= upper_bound)]

    X = X[(X[['cd40', 'cd420', 'cd80', 'cd820']] != 0).any(axis=1)]

    X.drop(['oprior', 'zprior'], axis=1, inplace=True)

    return X


def clean_outliers(X: pd.DataFrame):
    X = X.copy()

    Q1 = X['wtkg'].quantile(0.25)
    Q3 = X['wtkg'].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    X = X[(X['wtkg'] >= lower_bound) & (X['wtkg'] <= upper_bound)]

    X = X[(X[['cd40', 'cd420', 'cd80', 'cd820']] != 0).any(axis=1)]

    return X

class CleanDataTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformed = X.copy()
        X_transformed = X_transformed.set_index(['pidnum'])
        X_transformed = X_transformed[(X_transformed[['cd40', 'cd420', 'cd80', 'cd820']] != 0).any(axis=1)]
        X_transformed.drop(['oprior', 'zprior'], axis=1, inplace=True)
        return X_transformed

