import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

def load_model(model_path):
    """Memuat model dari file joblib."""
    return joblib.load(model_path)

def preprocess_input(data, numerical_features, categorical_features, scaler, encoder):
    """Melakukan preprocessing data input."""
    data[numerical_features] = scaler.transform(data[numerical_features])
    data[categorical_features] = data[categorical_features].apply(lambda x: encoder.transform(x))
    return data

def predict(model, data):
    """Melakukan prediksi dengan model yang telah dimuat."""
    return model.predict(data)

if __name__ == "__main__":
    model_path = "model/model_nn.joblib"
    model = load_model(model_path)

    numerical_features = ['Age', 'DistanceFromHome', 'MonthlyIncome', 'JobLevel',
                          'TotalWorkingYears', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsWithCurrManager']
    categorical_features = ['Gender', 'Education', 'EducationField', 'MaritalStatus',
                            'BusinessTravel', 'EnvironmentSatisfaction', 'JobInvolvement',
                            'JobSatisfaction', 'OverTime', 'PerformanceRating',
                            'RelationshipSatisfaction', 'WorkLifeBalance']
    
    new_data = pd.DataFrame([
        [35, 5, 5000, 2, 10, 5, 3, 3, 'Male', 'Bachelor', 'Technical Degree', 'Single',
         'Travel_Rarely', 'Medium', 'High', 'Very High', 'No', 'Excellent', 'High', 'Good']
    ], columns=numerical_features + categorical_features)

    scaler = MinMaxScaler()
    encoder = LabelEncoder()
    
    new_data_processed = preprocess_input(new_data, numerical_features, categorical_features, scaler, encoder)
    
    prediction = predict(model, new_data_processed)
    
    print("Hasil Prediksi Attrition:", "Yes" if prediction[0] == 1 else "No")
