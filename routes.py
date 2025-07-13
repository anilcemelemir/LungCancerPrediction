from flask import render_template, request, redirect, url_for
from models.train_survival_model import preprocess_user_input

import pandas as pd
import joblib

# Eğitilmiş modeli yükleme
model_path = "models/rf_model.pkl"
rf_model = joblib.load(model_path)
survival_model_path = "models/survival_model.pkl"
survival_model = joblib.load(survival_model_path)

# Modelin beklediği sütun sıralaması
input_columns = [
    'GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY', 'PEER_PRESSURE',
    'CHRONIC DISEASE', 'FATIGUE', 'ALLERGY', 'WHEEZING', 'ALCOHOL CONSUMING',
    'COUGHING', 'SHORTNESS OF BREATH', 'SWALLOWING DIFFICULTY', 'CHEST PAIN'
]

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/predict', methods=['POST'])
    def predict():
        try:
            # Kullanıcıdan gelen verileri işleme
            user_input = {}
            for col in input_columns:
                if col == 'AGE':
                    user_input[col] = int(request.form[col])  # Yaş bilgisi sayısal değer
                elif col == 'GENDER':
                    user_input[col] = int(request.form[col])  # Dropdown seçiminden gelen değer
                else:
                    # Checkbox işaretlenmediyse varsayılan olarak 2 (yok) atanır
                    user_input[col] = 2 if request.form.get(col) == 'on' else 1

            # Giriş verilerini DataFrame'e dönüştürme
            input_df = pd.DataFrame([user_input])[input_columns]  # Sütun sırasını sabitle

            # Tahmin yapma
            prediction = rf_model.predict(input_df)[0]
            probability = rf_model.predict_proba(input_df)[0][1] * 100

            # Tahmin sonucunu gösteren sayfaya yönlendirme
            return redirect(url_for('result', 
                                    prediction=("Kanser riski yok" if prediction == 2 else "Kanser riski var"),
                                    probability=f"%{probability:.2f}"))
        except Exception as e:
            return f"Bir hata oluştu: {e}", 400

    @app.route('/result')
    def result():
        prediction = request.args.get('prediction')
        probability = request.args.get('probability')
        return render_template('result.html', prediction=prediction, probability=probability)
    
    @app.route('/survival')
    def survival_form():
        return render_template('survival.html')

    @app.route('/predict_survival', methods=['POST'])
    def predict_survival():
        try:
            # Formdan gelen verileri işleme
            smoking_history = int(request.form['Smoking_History'])
            tumor_location = int(request.form['Tumor_Location'])
            stage = int(request.form['Stage'])
            age_class = int(request.form['Age_Class'])
            survival_class = int(request.form['Survival_Class'])

            # Komorbidite bilgileri
            comorbidities = [
                1 if request.form.get(f'Comorbidity_{c}') else 0
                for c in ['Diabetes', 'Hypertension', 'Heart_Disease',
                          'Chronic_Lung_Disease', 'Kidney_Disease',
                          'Autoimmune_Disease', 'Other']
            ]

            # Kullanıcı verisini modele uygun hale getirme
            input_data = preprocess_user_input(smoking_history, tumor_location, stage, age_class, survival_class, comorbidities)

            # Tahmin yapma
            prediction = survival_model.predict(input_data)
            result = "Yaşayacak" if prediction[0] == 1 else "Yaşamayacak"

            return render_template('result.html', prediction=result)
        except Exception as e:
            return f"Bir hata oluştu: {e}", 400
