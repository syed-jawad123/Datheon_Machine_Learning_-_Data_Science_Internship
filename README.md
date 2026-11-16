# 🚀 Datheon Machine Learning & Data Science Internship

[![Datheon Verified](https://img.shields.io/badge/Datheon-Official%20Internship-0052FF?style=for-the-badge&logo=datheon&logoColor=white)](https://datheon.in/verify)
[![Candidate ID](https://img.shields.io/badge/Application%20ID-DT--2026--QZJDN-10B981?style=for-the-badge)](https://datheon.in/verify)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**Intern:** Syed Jawad Hussain Shah  
**Degree:** BS Artificial Intelligence, BIIT Rawalpindi (Graduating 2026, CGPA 3.64)  
**Program:** Machine Learning & Data Science Technical Residency (Batch 01, Pakistan)  
**Host Directorate:** Datheon Admissions & Talent Directorate (`admissions@datheon.in`)  
**Official Verification Registry:** [datheon.in/verify](https://datheon.in/verify) (Ref: `DT-2026-QZJDN`)

---

## 📌 Executive Summary

This repository contains the complete production-grade engineering deliverables for the **Datheon Machine Learning & Data Science Internship**. All tasks adhere to the strict Directorate Evaluation Criteria, implementing clean exploratory data analysis (EDA), data scaling, algorithm benchmarking, diagnostic residual validation, and unsupervised clustering heuristics.

---

## 🗂️ Project Architecture & Directory Layout

```
Datheon_Machine_Learning_&_Data_Science_Internship/
│
├── Task_1_Supervised_Classification/
│   ├── Task1_Supervised_Classification.ipynb    # Executed Jupyter Notebook with outputs
│   ├── task1_classification.py                 # Modular standalone Python pipeline
│   └── plots/
│       ├── confusion_matrix_comparison.png      # Side-by-side Logistic Regression vs Decision Tree
│       └── decision_boundary.png                # 2D non-linear classification contour map
│
├── Task_2_Predictive_Regression/
│   ├── Task2_Predictive_Regression.ipynb        # Regression training & diagnostic notebook
│   └── plots/
│       ├── regression_performance.png           # Actual vs Predicted & Error Residuals
│       └── feature_importance.png               # Gini importance ranking (Random Forest)
│
├── Task_3_Customer_Segmentation_Clustering/
│   ├── Task3_Customer_Segmentation.ipynb        # K-Means, Elbow & Silhouette evaluation
│   └── plots/
│       ├── elbow_and_silhouette_analysis.png    # WCSS Inertia Elbow & Silhouette curves
│       └── customer_clusters_pca.png            # 2D PCA Dimensionality Reduction projection
│
└── README.md                                    # Comprehensive technical documentation
```

---

## 🧪 Technical Deliverables Breakdown

### 🔬 Task 1: Supervised Classification Benchmark (Iris & Wine Datasets)
- **Objective:** Build a robust supervised classification model handling feature scaling (`StandardScaler`), 80/20 train/test stratified split, and benchmark algorithmic performance across **Logistic Regression**, **Decision Tree Classifier**, and **Random Forest**.
- **Key Metrics Achieved:**
  - **Logistic Regression:** 100% Precision, 100% Recall, **100.0% Accuracy** on test set.
  - **Decision Tree Classifier:** 96.67% Test Accuracy with bounded depth to prevent overfitting.
- **Visual Diagnostics:** Plotted complete Confusion Matrices and non-linear Decision Boundary contours.

---

### 📈 Task 2: Predictive Housing Price Regression
- **Objective:** Train and evaluate continuous price predictors on the California Housing dataset using **Linear Regression**, **Ridge Regularization**, and **Random Forest Regressors**.
- **Key Metrics Achieved:**
  - **Random Forest Regressor:** $R^2 = 0.812$, $RMSE = 0.504$, $MAE = 0.332$ ($100k valuation scale).
  - Outperformed baseline linear model ($R^2 = 0.605$) by over 34% in variance explanation.
- **Visual Diagnostics:** Residual error distribution (normally centered around 0) and Gini feature importance ranking showing `MedInc` (Median Income) as the predominant price driver.

---

### 🧩 Task 3: Customer Segmentation & Unsupervised Clustering
- **Objective:** Discover organic behavioral customer clusters using **K-Means Clustering**, verified using the **Elbow Method (Inertia WCSS)** and **Silhouette Coefficient Analysis**.
- **Key Metrics Achieved:**
  - Optimal cluster count mathematically determined at **$K = 5$** with peak silhouette coefficient of **0.582**.
  - Dimensionality reduction via **Principal Component Analysis (PCA)** preserving over 85% variance for 2D visual cluster separation.

---

## ⚙️ Quickstart & Local Execution

To clone and run these deliverables locally:

```bash
# 1. Clone repository
git clone https://github.com/syed-jawad123/Datheon_Machine_Learning_&_Data_Science_Internship.git

# 2. Navigate to project root
cd Datheon_Machine_Learning_&_Data_Science_Internship

# 3. Install requirements
pip install numpy pandas scikit-learn matplotlib seaborn jupyter

# 4. Launch Jupyter Notebook
jupyter notebook
```

---

## 🏆 Candidate Information & Declaration

- **Author:** Syed Jawad Hussain Shah
- **Portfolio:** [github.com/syed-jawad123](https://github.com/syed-jawad123)
- **LinkedIn:** [linkedin.com/in/syed-jawad-hussain-shah](https://www.linkedin.com/in/syed-jawad-hussain-shah)
- **Application ID:** `DT-2026-QZJDN`
- **Institution:** Barani Institute of Information Technology (BIIT), Rawalpindi, Pakistan

*Submitted for Directorate Evaluation & Official Certificate of Completion Verification.*
