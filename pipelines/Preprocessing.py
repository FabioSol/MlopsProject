from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
import numpy as np


class CustomTimeTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.mean_ = None
        self.var_ = None

    def fit(self, X, y=None):
        self.thresh = 900
        X_greater_than = X[X[:, 0] > self.thresh, 0]
        self.mean_ = np.mean(X_greater_than)
        self.var_ = np.var(X_greater_than)
        return self

    def transform(self, X):
        X_transformed = np.zeros((X.shape[0], 2))
        X_transformed[:, 0] = np.where(X[:, 0] < self.thresh, X[:, 0] / self.thresh, 0)
        X_transformed[:, 1] = np.where(X[:, 0] > self.thresh, (X[:, 0] - self.mean_) / np.sqrt(self.var_), 0)
        return X_transformed


class LogTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Apply log transformation
        X_log = np.log(X + 1)  # Adding 1 to avoid log(0)

        return X_log


class KarnofTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X / 100  # Divide 'karnof' values by 100


# Define custom transformer for 'preanti' column
class PreantiTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        bins = [0, 1, 1000, np.inf]  # Define bin edges
        labels = ["0", "1", "2"]  # Define labels for bins
        X_binned = np.digitize(X, bins=bins, right=True)
        return X_binned.reshape(-1, 1)  # Reshape to column vector


pipeline_binary = Pipeline(steps=[])

pipeline_time = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('custom', CustomTimeTransformer()),
    ('scaler', MinMaxScaler())
])

log_minmax_pipeline = Pipeline(steps=[
    ('log_minmax_transform', LogTransformer()),
    ('scaler', MinMaxScaler())
])

pipeline_oh = Pipeline(steps=[
    ('onehot', OneHotEncoder())
])

pipeline_minmax = Pipeline(steps=[
    ('scaler', MinMaxScaler())
])

pipeline_preanti = Pipeline(steps=[
    ('binning', PreantiTransformer()),  # Apply binning
    ('onehot', OneHotEncoder())  # Apply one-hot encoding
])

pipeline_karnof = Pipeline(steps=[
    ('transformer', KarnofTransformer())  # Apply custom transformation for 'karnof'
])

preprocessor_beta = ColumnTransformer(
    transformers=[
        ('binary', 'passthrough',
         ['hemo', 'homo', 'drugs', 'z30', 'gender', 'str2', 'symptom', 'treat', 'offtrt', 'race']),
        ('time', pipeline_time, ['time']),
        ('oh', pipeline_oh, ['trt', 'strat']),
        ('minmax', pipeline_minmax, ['age', 'wtkg']),
        ('linfo', log_minmax_pipeline, ['cd40', 'cd420', 'cd80', 'cd820']),
        ('karnof', pipeline_karnof, ['karnof']),
        ('preanti', pipeline_preanti, ['preanti'])
    ],
    remainder='drop'
)

preprocessor = ColumnTransformer(
    transformers=[
        ('binary', 'passthrough',
         ['hemo', 'homo', 'drugs', 'z30', 'gender', 'str2', 'symptom', 'treat', 'offtrt', 'race']),
        ('time', pipeline_time, ['time']),
        ('oh', pipeline_oh, ['trt']),
        ('minmax', pipeline_minmax, ['age', 'wtkg']),
        ('linfo', log_minmax_pipeline, ['cd40', 'cd420', 'cd80', 'cd820']),
        ('karnof', pipeline_karnof, ['karnof']),
        ('preanti', pipeline_preanti, ['preanti'])
    ],
    remainder='drop'
)

if __name__ == '__main__':
    from ucimlrepo import fetch_ucirepo

    aids_clinical_trials_group_study_175 = fetch_ucirepo(id=890)
    data = aids_clinical_trials_group_study_175.data.original
