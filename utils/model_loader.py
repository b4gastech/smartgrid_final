import joblib

def load_model():

    model=joblib.load(
        "models/decision_tree_model.pkl"
    )

    return model