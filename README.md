# 🫁 Lung Cancer Prediction

This project combines machine learning with a Flask web interface to predict the **risk of lung cancer** and **survival likelihood** based on user input. It consists of two trained models: one for lung cancer risk prediction, and another for survival analysis using comorbidities and clinical indicators.

> ⚠️ **Experimental Project Notice**  
> This tool is created for educational and experimental purposes only. It is **not a medical device**. The results are derived from limited, small-scale datasets and do **not represent clinically validated predictions**.

---

## ⚙️ Functionality

- **Lung Cancer Risk Prediction**  
  Uses a Random Forest model trained on basic survey features like smoking, fatigue, anxiety, etc.

- **Survival Prediction**  
  Uses a Decision Tree model trained on synthetic clinical data including comorbidities, tumor stage, and survival duration classes.

---

## 🧪 Limitations

- Small and potentially biased datasets  
- Simplified feature encoding  
- No hyperparameter tuning or cross-validation  
- Not suitable for clinical decision-making

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

### 3. Train the Models (Once)

```bash
python src/train_cancer_model.py
python src/train_survival_model.py
```

> Make sure both `.csv` files are inside the `data/` folder before training.

### 4. Run the Flask App

```bash
python main.py
```

Go to [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📄 License

MIT License © 2025 Semih Çetin, Velihan Özge, Anıl Cem Elemir

---

## 🏷️ Tags

```
machine-learning
flask
lung-cancer
healthcare
survival-analysis
classification
python
experimental
```
