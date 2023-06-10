from typing import List
from urllib.request import Request
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import uvicorn
import traceback
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import StandardScaler
import os

# Init priority instances
app = FastAPI()


class RequestText(BaseModel):
    ayam_dagingT: float
    ikan_seafoodT: float
    tahu_tempe_telurT: float
    sayurT: float
    sambalT: float
    nasi_mie_pastaT: float
    sop_soto_baksoT: float
    kue_rotiT: float
    jajanan_pasarT: float
    puding_jeliT: float
    keripik_kerupukT: float
    buah_minumanT: float

model = tf.keras.saving.load_model("model.h5")

@app.get("/")
async def index():
    return "Hello food recommendation endpoint!"


@app.post("/")
async def predict(req: RequestText, response: Response):
    try:
        feature = [
            req.ayam_dagingT,
            req.ikan_seafoodT,
            req.tahu_tempe_telurT,
            req.sayurT,
            req.sambalT,
            req.nasi_mie_pastaT,
            req.sop_soto_baksoT,
            req.kue_rotiT,
            req.jajanan_pasarT,
            req.puding_jeliT,
            req.keripik_kerupukT,
            req.buah_minumanT,
        ]
        input_model = np.array(feature, dtype=np.float32)
        #TODO
        #Lakukan normalisasi atau standarisasi saat kalian membuat modelnya
        scaler = StandardScaler()
        input_model = np.reshape(input_model,(-1,12))
        input_model = scaler.fit_transform(input_model)
        print(input_model)
        result = model.predict(input_model)
        
        # Kak Kaenova Guess, output menggunakan softmax
        result = np.argmax(result,axis=1)
        print(result)

        return int(result[0]) 
    except Exception as e:
        traceback.print_exc()
        response.status_code = 500
        return {"message": "Internal Server Error"}


port = os.environ.get("PORT", 8001)
print(f"Listening to http://0.0.0.0:{port}")
uvicorn.run(app, host="0.0.0.0", port=port)
