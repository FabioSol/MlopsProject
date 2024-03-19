import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

def clean_data(X: pd.DataFrame):
    X = X.copy()
    X = X.set_index(['pidnum'])
    X = X[X['wtkg'] <= 140]
    X = X[(X[['cd40', 'cd420', 'cd80', 'cd820']] != 0).any(axis=1)]
    X.drop(['oprior', 'zprior'], axis=1, inplace=True)
    return X

def clean_outliers(X: pd.DataFrame):
    X = X.copy()
    X = X[X['wtkg'] <= 140]
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

