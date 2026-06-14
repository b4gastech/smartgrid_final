import os
import joblib


def safe_load(path):

    if os.path.exists(path):

        try:

            return joblib.load(path)

        except:

            return None

    return None


def load_models():

    dt = safe_load(
        "models/decision_tree_model.pkl"
    )

    knn = safe_load(
        "models/knn.pkl"
    )

    svm = safe_load(
        "models/svm.pkl"
    )

    return dt, knn, svm