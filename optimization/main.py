import optuna
from ucimlrepo import fetch_ucirepo
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import f1_score
from pipelines import CleanDataTransformer, preprocessor, clean_outliers
import pickle
from model import model_path
import pandas as pd

def hyperparam_optimization(n_trials: int = 100, save: bool = True):
    data = clean_outliers(fetch_ucirepo(id=890).data.original)
    y = data['cid']
    X = data.drop(['cid'], axis=1)
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=69)

    def objective(trial):
        C = trial.suggest_float('C', 1e-3, 100)
        kernel = trial.suggest_categorical('kernel', ['linear', 'rbf', 'sigmoid'])
        degree = trial.suggest_int('degree', 1, 50)
        gamma = trial.suggest_categorical('gamma', ['scale', 'auto'])

        method = trial.suggest_categorical('method', ['sigmoid', 'isotonic'])

        svc = SVC(probability=True, C=C, kernel=kernel, degree=degree, gamma=gamma)
        calibrated_svc = CalibratedClassifierCV(svc, method=method, cv=3)
        pipeline = Pipeline([
            ('cleaning', CleanDataTransformer()),
            ('preprocessor', preprocessor),
            ('classifier', calibrated_svc)
        ])

        pipeline.fit(X_train, y_train)

        y_pred = pipeline.predict(X_valid)
        score = f1_score(y_valid, y_pred)

        return score

    study = optuna.create_study(direction='maximize')
    study.optimize(objective, n_trials=n_trials)

    trial = study.best_trial

    best_params = trial.params

    svc = SVC(probability=True, C=best_params.get('C'), kernel=best_params.get('kernel'),
              degree=best_params.get('degree'), gamma=best_params.get('gamma'))
    calibrated_svc = CalibratedClassifierCV(svc, method=best_params.get('method'), cv=3)
    pipeline = Pipeline([
        ('cleaning', CleanDataTransformer()),
        ('preprocessor', preprocessor),
        ('classifier', calibrated_svc)
    ])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_valid)
    report = classification_report(y_valid, y_pred)
    cm = confusion_matrix(y_valid, y_pred)
    cm_df = pd.DataFrame(cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"])

    if save:
        with open(model_path, 'wb') as f:
            pickle.dump(pipeline, f)
    return best_params, report, cm_df


if __name__ == '__main__':
    hyperparam_optimization()
