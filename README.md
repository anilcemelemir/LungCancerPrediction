# 🫁 Lung Cancer Prediction

This project combines machine learning with a Flask web interface to predict the risk of lung cancer and survival likelihood based on user input. It consists of two trained models: one for lung cancer risk prediction, and another for survival prediction using comorbidities and clinical data.

---

## ⚙️ Functionality

- **Lung Cancer Risk Prediction**  
  Uses a Random Forest model trained on survey data. Takes inputs like smoking, coughing, fatigue, etc. and predicts the probability of lung cancer risk.

- **Survival Prediction**  
  Uses a Decision Tree model trained on clinical data including age class, stage, tumor location, and comorbidities.

---

## 🛠️ Tech Stack

- Python 3.x  
- Flask  
- pandas, numpy  
- scikit-learn  
- joblib  
- matplotlib, seaborn

---


## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/anilcemelemir/LungCancerPrediction.git
cd LungCancerPrediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the Models (Only Once)

Before running the Flask app, make sure the following `.pkl` files are created:

- `models/rf_model.pkl`
- `models/survival_model.pkl`

You can do this by running the training scripts (or copying the provided `.pkl` files):

```bash
# Make sure data/ folder contains both CSV files
python src/train_cancer_model.py 
python src/train_survival_model.py
```


### 4. Run the App

```bash
python main.py
```

Then go to `http://localhost:5000` in your browser.


---

## 📄 License

MIT License © 2025 Anıl Cem Elemir

---

## 🏷️ Tags

```
machine-learning
flask
lung-cancer
survival-analysis
healthcare
classification
scikit-learn
pandas
python
```
