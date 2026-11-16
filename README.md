# 🚀 Datheon Machine Learning & Data Science Internship

[![Datheon Verified](https://img.shields.io/badge/Datheon-Official%20Internship-0052FF?style=for-the-badge&logo=datheon&logoColor=white)](https://datheon.in/verify)
[![Candidate ID](https://img.shields.io/badge/Application%20ID-DT--2026--QZJDN-10B981?style=for-the-badge)](https://datheon.in/verify)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Intern:** Syed Jawad Hussain Shah  
**Degree:** BS Artificial Intelligence, Barani Institute of Information Technology (BIIT), Rawalpindi, Pakistan (CGPA: 3.64, Graduating 2026)  
**Program:** Machine Learning & Data Science Internship (Standard 4 Weeks Residency · Batch 01)  
**Host Directorate:** Datheon Admissions & Talent Directorate (`admissions@datheon.in`)  
**Official Verification Registry:** [datheon.in/verify](https://datheon.in/verify) (Credential Ref: `DT-2026-QZJDN`)

---

## 📌 Executive Summary

This repository contains the complete, production-grade project deliverables for the **Datheon Machine Learning & Data Science Internship**. In accordance with the Directorate Task Pack rule (*"Complete at least 2 or 3 predictive modeling tasks"*), this repository delivers **all 4 official curriculum tasks** executed with Jupyter Notebooks, publication-quality diagnostic plots, and reproducible Python code.

---

## 🗂️ Project Directory Layout

```
Datheon_Machine_Learning_&_Data_Science_Internship/
│
├── Task_1_MultiClass_Classification/
│   ├── Task1_MultiClass_Classification.ipynb      # Executed Notebook (Iris / Wine)
│   └── plots/
│       ├── confusion_matrix_heatmap.png            # Logistic Regression vs Decision Tree
│       └── decision_boundary.png                   # 2D non-linear classification boundary
│
├── Task_2_Real_Estate_Regression/
│   ├── Task2_Real_Estate_Regression.ipynb          # Ridge & Lasso Regression pipeline
│   └── plots/
│       └── ridge_regression_residuals.png          # Predicted vs Actual & Residual error curve
│
├── Task_3_Customer_Churn_Classifier/
│   ├── Task3_Customer_Churn_Classifier.ipynb       # Random Forest & XGBoost with SMOTE
│   └── plots/
│       └── churn_roc_and_feature_importance.png    # ROC-AUC curve (>80%) & Top features
│
├── Task_4_NLP_Sentiment_Classification/
│   ├── Task4_NLP_Sentiment_Classification.ipynb   # TF-IDF & Multinomial Naive Bayes
│   └── plots/
│       └── nlp_sentiment_confusion_matrix.png      # Sentiment classification heatmap
│
└── README.md                                       # Comprehensive technical documentation
```

---

## 🧪 Curriculum Tasks Breakdown

### 🔬 Task 1: Multi-Class Benchmark Classification Pipeline (Iris / Wine)
- **Objective:** Build an end-to-end multi-class classification pipeline with feature scaling (`StandardScaler`), 80/20 train/test stratified split, and benchmark algorithmic performance.
- **Models Benchmarked:** Logistic Regression vs. Decision Tree Classifier.
- **Results:** Logistic Regression achieved **100.0% test accuracy**, Decision Tree achieved **96.67% test accuracy**.
- **Deliverables:** Executed notebook with full confusion matrix heatmap and non-linear 2D decision boundary visualization.

---

### 📈 Task 2: Real Estate Housing Price Prediction (Ridge & Lasso Regression)
- **Objective:** Train continuous price predictors on the California Housing dataset using OLS, Ridge (L2), and Lasso (L1) regression models with `GridSearchCV` hyperparameter optimization.
- **Results:** Identified optimal Ridge penalty ($lpha = 10.0$) achieving $R^2 = 0.605$, with residual errors symmetrically centered around 0.
- **Deliverables:** Executed notebook with actual-vs-predicted diagnostics and residual distribution plots.

---

### 🛡️ Task 3: Predictive Customer Churn Classifier (Random Forest & XGBoost)
- **Objective:** Resolve severe telecom customer churn class imbalance using **SMOTE oversampling**, train ensemble classifiers (**Random Forest** and **XGBoost**), and optimize the **ROC-AUC curve (>80%)**.
- **Results:**
  - **Random Forest:** ROC-AUC = **86.4%**, Accuracy = **82.2%**.
  - **XGBoost Classifier:** ROC-AUC = **87.8%**, Accuracy = **83.6%**.
  - Identified `Tenure`, `MonthlyCharges`, and `ContractType` as the top 3 drivers of churn risk.
- **Deliverables:** Executed notebook with ROC-AUC curve comparison and horizontal feature importance bar chart.

---

### 💬 Task 4: NLP Sentiment Classification on Customer Reviews (TF-IDF)
- **Objective:** Ingest customer reviews, clean and tokenize text, generate numerical TF-IDF feature embeddings, and train a **Multinomial Naive Bayes** classifier.
- **Results:** Achieved **98.5% classification accuracy** with an interactive `predict_sentiment()` inference function.
- **Deliverables:** Executed NLP notebook with confusion matrix heatmap and live inference test suite.

---

## ⚙️ Quickstart & Local Reproduction

```bash
# Clone the repository
git clone https://github.com/syed-jawad123/Datheon_Machine_Learning_&_Data_Science_Internship.git

# Navigate to directory
cd Datheon_Machine_Learning_&_Data_Science_Internship

# Install dependencies
pip install numpy pandas scikit-learn matplotlib seaborn xgboost imbalanced-learn jupyter

# Launch Jupyter
jupyter notebook
```

---

## 🏆 Candidate Declaration

- **Author:** Syed Jawad Hussain Shah
- **Portfolio:** [github.com/syed-jawad123](https://github.com/syed-jawad123)
- **LinkedIn:** [linkedin.com/in/syed-jawad-hussain-shah](https://www.linkedin.com/in/syed-jawad-hussain-shah)
- **Application ID:** `DT-2026-QZJDN`
- **Institution:** Barani Institute of Information Technology (BIIT), Rawalpindi, Pakistan

*Submitted for Directorate Evaluation & Official Certificate of Completion Verification.*
