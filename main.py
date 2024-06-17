from fastapi import FastAPI, Request
from models import Iris, Advertising
import joblib

# Read models saved during train phase
estimator_iris_loaded = joblib.load("saved_models/01.knn_with_iris_dataset.pkl")
encoder_iris_loaded = joblib.load("saved_models/02.iris_label_encoder.pkl")
estimator_advertising_loaded = joblib.load("saved_models/03.randomforest_with_advertising.pkl")

app = FastAPI()


# prediction function
def make_iris_prediction(model, encoder, request):
    # parse input from the request
    SepalLengthCm = request["SepalLengthCm"]
    SepalWidthCm = request['SepalWidthCm']
    PetalLengthCm = request['PetalLengthCm']
    PetalWidthCm = request['PetalWidthCm']

    # Make an input vector
    flower = [[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]]

    # Predict
    prediction_raw = model.predict(flower)

    # Convert Species index to Species name
    prediction_real = encoder.inverse_transform(prediction_raw)

    return prediction_real[0]


def make_advertising_prediction(model, request):
    # parse input from request
    TV = request["TV"]
    Radio = request['Radio']
    Newspaper = request['Newspaper']

    # Make an input vector
    advertising = [[TV, Radio, Newspaper]]

    # Predict
    prediction = model.predict(advertising)

    return prediction[0]


# Iris Prediction endpoint
@app.post("/prediction/iris")
def predict_iris(request: Iris):
    prediction = make_iris_prediction(estimator_iris_loaded, encoder_iris_loaded, request.dict())
    return prediction


# Advertising Prediction endpoint
@app.post("/prediction/advertising")
def predict_iris(request: Advertising):
    prediction = make_advertising_prediction(estimator_advertising_loaded, request.dict())
    return prediction

# Get client info
@app.get("/client")
def client_info(request: Request):
    client_host = request.client.host
    client_port = request.client.port
    return {"client-host": client_host,
            "client-port": client_port}