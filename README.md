
# **Sentiment Analysis and Flight Ticket Pricing Prediction**

![GitHub repo size](https://img.shields.io/github/repo-size/your-username/repo-name)
![GitHub stars](https://img.shields.io/github/stars/your-username/repo-name)
![GitHub forks](https://img.shields.io/github/forks/your-username/repo-name)
![GitHub issues](https://img.shields.io/github/issues/your-username/repo-name)
![GitHub license](https://img.shields.io/github/license/your-username/repo-name)

This repository contains a **Sentiment Analysis** project and **Flight Ticket Pricing Prediction** model using Python, Scikit-learn, and Azure. The goal of the project is to classify customer reviews into sentiment categories and predict flight ticket prices using machine learning models.

---

## **Table of Contents**
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [License](#license)

---

## **Project Overview** <a name="project-overview"></a>

This project aims to perform sentiment analysis on customer feedback and predict flight ticket prices. The sentiment analysis categorizes reviews into different categories, such as **Poor**, **Average**, **Good**, **Very Good**, and **Must Read**, using NLP models. Additionally, the flight ticket pricing model predicts ticket prices based on various factors, including the time of booking, class, and flight duration.

---

## **Features** <a name="features"></a>
- **Sentiment Analysis:** Classifies feedback into sentiment categories using VADER sentiment scoring.
- **Flight Ticket Price Prediction:** Predicts prices using regression models based on input features.
- **Modeling:** Applies Random Forest and Decision Tree models for price prediction.
- **MLOps:** Integrated with **MLflow** to track and manage machine learning experiments.
- **Azure Integration:** Uses Azure Data Studio and Azure Storage for data processing and storage.

---

## **Installation** <a name="installation"></a>

To get started with the project, follow the steps below:

### **Clone the repository:**
```bash
git clone https://github.com/your-username/repo-name.git
cd repo-name
```

### **Set up the environment:**
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scriptsctivate
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **Azure Integration Setup:**
1. Make sure you have an Azure account and configure Azure Storage for storing large datasets.
2. Use **Azure Data Studio** to connect to your database and process the feedback data.

---

## **Usage** <a name="usage"></a>

### **Running Sentiment Analysis**
```bash
python sentiment_analysis.py
```

### **Running the Flight Ticket Price Prediction Model**
```bash
python price_prediction.py
```

### **Using MLflow for Experiment Tracking**
Start the MLflow server and track your experiments:
```bash
mlflow ui
```

---

## **Models** <a name="models"></a>

### **Sentiment Analysis Model**
- **Algorithm:** VADER Sentiment Scoring
- **Categories:** Poor, Average, Good, Very Good, Must Read

### **Flight Ticket Pricing Model**
- **Algorithms:** Random Forest, Decision Tree, Linear Regression
- **Evaluation Metrics:** MAE, RMSE, R² Score

---

## **Technologies Used** <a name="technologies-used"></a>

- **Programming Languages:** Python
- **Libraries:** Scikit-learn, Pandas, Numpy, SpaCy, VADER, Matplotlib, Seaborn
- **Data Storage:** Azure Data Studio, Azure Storage
- **MLOps:** MLflow
- **Deployment:** Flask, Streamlit (Optional)

---

## **Project Structure** <a name="project-structure"></a>

```bash
├── data/
│   ├── raw/
│   ├── processed/
├── models/
│   ├── sentiment_model.pkl
│   ├── pricing_model.pkl
├── notebooks/
│   └── data_analysis.ipynb
├── sentiment_analysis.py
├── price_prediction.py
├── mlflow_experiment.py
├── README.md
├── requirements.txt
```

---

## **Deployment** <a name="deployment"></a>

For deploying the models, you can either use **Flask** or **Streamlit**.

### **Flask Deployment**:
1. Install **Flask**:
   ```bash
   pip install Flask
   ```
2. Run the Flask app:
   ```bash
   python app.py
   ```

### **Streamlit Deployment** (Optional):
1. Install **Streamlit**:
   ```bash
   pip install streamlit
   ```
2. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## **License** <a name="license"></a>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

