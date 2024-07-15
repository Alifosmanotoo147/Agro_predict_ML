import streamlit as st
import requests

# Streamlit app title
st.title('Crop Prediction')

# User inputs
N = st.number_input('Nitrogen (N)', min_value=0.0, value=0.0)
P = st.number_input('Phosphorus (P)', min_value=0.0, value=0.0)
K = st.number_input('Potassium (K)', min_value=0.0, value=0.0)
temperature = st.number_input('Temperature', min_value=0.0, value=0.0)
humidity = st.number_input('Humidity', min_value=0.0, value=0.0)

# Predict button
if st.button('Predict Crop'):
    # Prepare the input data
    data = {
        'N': N,
        'P': P,
        'K': K,
        'temperature': temperature,
        'humidity': humidity
    }

    try:
        # Send a request to the FastAPI backend
        response = requests.post('http://127.0.0.1:8000/predict', json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        
        result = response.json()
        
        # Check if the response contains the expected key
        if 'predicted_crop' in result:
            st.write(f"Predicted Crop: {result['predicted_crop']}")
        else:
            st.error("Unexpected response format: 'predicted_crop' key not found")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
