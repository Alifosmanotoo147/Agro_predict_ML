import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
dataset = pd.read_csv('dataset.csv')

# Ensure the dataset's label column has numeric values corresponding to crop_mapping
crop_mapping = {
    'rice': 0, 'maize': 1, 'chickpea': 2, 'kidneybeans': 3, 'pigeonpeas': 4,
    'mothbeans': 5, 'mungbean': 6, 'blackgram': 7, 'lentil': 8, 'pomegranate': 9,
    'banana': 10, 'mango': 11, 'grapes': 12, 'watermelon': 13, 'muskmelon': 14,
    'apple': 15, 'orange': 16, 'papaya': 17, 'coconut': 18, 'cotton': 19, 'jute': 20,
    'coffee': 21
}

# Reverse the mapping dictionary to get crop name from digit
reverse_crop_mapping = {value: key for key, value in crop_mapping.items()}

# Map the crop names to their corresponding numeric labels in the dataset
dataset['label'] = dataset['label'].map(crop_mapping)

# Split the data into features and target
X = dataset[['N', 'P', 'K', 'temperature', 'humidity']]
y = dataset['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the classifier
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

# Save the trained model with the current version of scikit-learn
joblib.dump(classifier, 'crop_classifier.joblib')
