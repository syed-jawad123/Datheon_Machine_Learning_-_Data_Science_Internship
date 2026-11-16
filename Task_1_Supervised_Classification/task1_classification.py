# Task 1: Supervised Classification Benchmark
# Candidate: Syed Jawad Hussain Shah | Datheon ID: DT-2026-QZJDN

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def run_classification():
    data = load_iris()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Model 1: Logistic Regression
    lr = LogisticRegression(max_iter=200, random_state=42)
    lr.fit(X_train_scaled, y_train)
    preds_lr = lr.predict(X_test_scaled)
    print("Logistic Regression Accuracy:", accuracy_score(y_test, preds_lr))
    print(classification_report(y_test, preds_lr, target_names=data.target_names))
    
    # Model 2: Decision Tree
    dt = DecisionTreeClassifier(max_depth=4, random_state=42)
    dt.fit(X_train, y_train)
    preds_dt = dt.predict(X_test)
    print("Decision Tree Accuracy:", accuracy_score(y_test, preds_dt))
    print(classification_report(y_test, preds_dt, target_names=data.target_names))

if __name__ == '__main__':
    run_classification()
