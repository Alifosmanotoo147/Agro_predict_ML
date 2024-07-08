''' 
from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd

# Load the trained model
classifier = joblib.load('crop_classifier.joblib')

# Initialize FastAPI app
app = FastAPI()

# Mapping dictionary provided by the user
reverse_crop_mapping = {0: 'rice', 1: 'maize', 2: 'chickpea', 3: 'kidneybeans', 4: 'pigeonpeas',
                        5: 'mothbeans', 6: 'mungbean', 7: 'blackgram', 8: 'lentil', 9: 'pomegranate',
                        10: 'banana', 11: 'mango', 12: 'grapes', 13: 'watermelon', 14: 'muskmelon',
                        15: 'apple', 16: 'orange', 17: 'papaya', 18: 'coconut', 19: 'cotton',
                        20: 'jute', 21: 'coffee'}

@app.post("/predict")
async def predict_crop(N: float, P: float, K: float, temperature: float, humidity: float):
    try:
        # Create a DataFrame from user input
        data = {'N': [N], 'P': [P], 'K': [K], 'temperature': [temperature], 'humidity': [humidity]}
        df = pd.DataFrame(data)

        # Use the pre-trained classifier to predict crop
        prediction = classifier.predict(df)

        # Convert the prediction to crop name using reverse mapping
        crop_name = reverse_crop_mapping[prediction[0]]

        return {"predicted_crop": crop_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

'''
from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd

# Load the trained model
classifier = joblib.load('crop_classifier.joblib')

# Initialize FastAPI app
app = FastAPI()

# Mapping dictionary provided by the user
reverse_crop_mapping = {0: 'rice', 1: 'maize', 2: 'chickpea', 3: 'kidneybeans', 4: 'pigeonpeas',
                        5: 'mothbeans', 6: 'mungbean', 7: 'blackgram', 8: 'lentil', 9: 'pomegranate',
                        10: 'banana', 11: 'mango', 12: 'grapes', 13: 'watermelon', 14: 'muskmelon',
                        15: 'apple', 16: 'orange', 17: 'papaya', 18: 'coconut', 19: 'cotton',
                        20: 'jute', 21: 'coffee'}

@app.post("/predict")
async def predict_crop(N: float, P: float, K: float, temperature: float, humidity: float):
    try:
        # Create a DataFrame from user input
        data = {'N': [N], 'P': [P], 'K': [K], 'temperature': [temperature], 'humidity': [humidity]}
        df = pd.DataFrame(data)

        # Use the pre-trained classifier to predict crop
        prediction = classifier.predict(df)

        # Convert the prediction to crop name using reverse mapping
        crop_name = reverse_crop_mapping[prediction[0]]

        return {"predicted_crop": crop_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
