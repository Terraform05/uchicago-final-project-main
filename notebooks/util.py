import pickle

def save_model(model, model_name):
    file = open(f"../models/{model_name}.pkl", "wb")
    pickle.dump(model, file)

def load_model(model_name):
    file = open(f"../models/{model_name}.pkl", "rb")
    return pickle.load(file)
