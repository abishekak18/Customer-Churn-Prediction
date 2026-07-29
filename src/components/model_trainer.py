import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier,
    ExtraTreesClassifier
)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from xgboost import XGBClassifier
from catboost import CatBoostClassifier

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join(
        "artifacts",
        "model.pkl"
    )


class ModelTrainer:

    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):

        try:

            logging.info("Splitting train and test arrays")

            X_train = train_array[:, :-1]
            y_train = train_array[:, -1]

            X_test = test_array[:, :-1]
            y_test = test_array[:, -1]

            models = {

                "Logistic Regression": LogisticRegression(max_iter=1000),

                "KNN": KNeighborsClassifier(),

                "Decision Tree": DecisionTreeClassifier(),

                "Random Forest": RandomForestClassifier(),

                "Gradient Boosting": GradientBoostingClassifier(),

                "Extra Trees": ExtraTreesClassifier(),

                "AdaBoost": AdaBoostClassifier(),

                "XGBoost": XGBClassifier(
                    eval_metric="logloss"
                ),

                "CatBoost": CatBoostClassifier(
                    verbose=False,
                    allow_writing_files=False,
                    random_state=42
                )

            }

            params = {

                "Logistic Regression": {

                    "C": [0.01, 0.1, 1, 10],

                    "solver": [
                        "liblinear",
                        "lbfgs"
                    ]

                },

                "KNN": {

                    "n_neighbors": [3, 5, 7, 9]

                },

                "Decision Tree": {

                    "criterion": [
                        "gini",
                        "entropy"
                    ],

                    "max_depth": [
                        5,
                        10,
                        20,
                        None
                    ]

                },

                "Random Forest": {

                    "n_estimators": [
                        100,
                        200,
                        300
                    ],

                    "max_depth": [
                        5,
                        10,
                        20,
                        None
                    ]

                },

                "Gradient Boosting": {

                    "learning_rate": [
                        0.01,
                        0.05,
                        0.1
                    ],

                    "n_estimators": [
                        100,
                        200,
                        300
                    ]

                },

                "Extra Trees": {

                    "n_estimators": [
                        100,
                        200,
                        300
                    ]

                },

                "AdaBoost": {

                    "learning_rate": [
                        0.01,
                        0.1,
                        1
                    ],

                    "n_estimators": [
                        50,
                        100,
                        200
                    ]

                },

                "XGBoost": {

                    "learning_rate": [
                        0.01,
                        0.05,
                        0.1
                    ],

                    "n_estimators": [
                        100,
                        200,
                        300
                    ],

                    "max_depth": [
                        3,
                        5,
                        7
                    ]

                },

                "CatBoost": {

                    "iterations": [
                        100,
                        200
                    ],

                    "learning_rate": [
                        0.01,
                        0.05,
                        0.1
                    ],

                    "depth": [
                        4,
                        6,
                        8
                    ]

                }

            }

            model_report, fitted_models = evaluate_models(

                X_train=X_train,
                y_train=y_train,

                X_test=X_test,
                y_test=y_test,

                models=models,
                param=params

            )

            best_model_score = max(model_report.values())

            best_model_name = max(
                model_report,
                key=model_report.get
            )

            best_model = fitted_models[best_model_name]

            logging.info(
                f"Best Model : {best_model_name}"
            )

            logging.info(
                f"Best Accuracy : {best_model_score}"
            )

            save_object(

                file_path=self.model_trainer_config.trained_model_file_path,

                obj=best_model

            )

            prediction = best_model.predict(X_test)

            accuracy = accuracy_score(
                y_test,
                prediction
            )

            return accuracy

        except Exception as e:
            raise CustomException(e, sys)