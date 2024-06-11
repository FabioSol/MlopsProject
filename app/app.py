from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

from model.predict import model_predict

# Define a FastAPI app instance
app = FastAPI()



class InputData(BaseModel):
    pidnum: int
    time: int
    trt: int
    age: int
    wtkg: float
    hemo: bool
    homo: bool
    drugs: bool
    karnof: int
    oprior: bool
    z30: bool
    zprior: bool
    preanti: int
    race: bool
    gender: bool
    str2: bool
    strat: int
    symptom: bool
    treat: bool
    offtrt: bool
    cd40: int
    cd420: int
    cd80: int
    cd820: int



@app.post("/predict/")
def predict(input_data: InputData):

    prediction = model_predict([list(input_data.dict().values())])

    return {"prediction": prediction}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)