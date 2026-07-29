import os
import sys
import pickle

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from src.exception import CustomException


def save_object(file_path, obj):

    try:

        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:

            pickle.dump(obj, file_obj)

    except Exception as e:

        raise CustomException(e, sys)


def load_object(file_path):

    try:

        with open(file_path, "rb") as file_obj:

            return pickle.load(file_obj)

    except Exception as e:

        raise CustomException(e, sys)


def evaluate_models(

        X_train,
        y_train,
        X_test,
        y_test,
        models,
        param

):

    try:

        report = {}
        fitted_models = {}

        for model_name, model in models.items():

            parameters = param[model_name]

            gs = GridSearchCV(

                estimator=model,

                param_grid=parameters,

                cv=3,

                scoring="accuracy",

                n_jobs=-1

            )

            gs.fit(X_train, y_train)

            best_model = gs.best_estimator_

            best_model.fit(X_train, y_train)

            y_train_pred = best_model.predict(X_train)

            y_test_pred = best_model.predict(X_test)

            train_accuracy = accuracy_score(
                y_train,
                y_train_pred
            )

            test_accuracy = accuracy_score(
                y_test,
                y_test_pred
            )

            train_precision = precision_score(
                y_train,
                y_train_pred
            )

            test_precision = precision_score(
                y_test,
                y_test_pred
            )

            train_recall = recall_score(
                y_train,
                y_train_pred
            )

            test_recall = recall_score(
                y_test,
                y_test_pred
            )

            train_f1 = f1_score(
                y_train,
                y_train_pred
            )

            test_f1 = f1_score(
                y_test,
                y_test_pred
            )

            report[model_name] = test_accuracy
            fitted_models[model_name] = best_model

            print("=" * 70)

            print(model_name)

            print(f"Train Accuracy  : {train_accuracy:.4f}")
            print(f"Test Accuracy   : {test_accuracy:.4f}")

            print(f"Train Precision : {train_precision:.4f}")
            print(f"Test Precision  : {test_precision:.4f}")

            print(f"Train Recall    : {train_recall:.4f}")
            print(f"Test Recall     : {test_recall:.4f}")

            print(f"Train F1 Score  : {train_f1:.4f}")
            print(f"Test F1 Score   : {test_f1:.4f}")

        return report, fitted_models

    except Exception as e:

        raise CustomException(e, sys)