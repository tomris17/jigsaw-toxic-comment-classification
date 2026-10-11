# 🛡️ Jigsaw Toxic Comment Classification

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Library-Scikit_Learn-orange.svg)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Library-Pandas-yellow.svg)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/App-Streamlit-red.svg)](https://streamlit.io/)

This repository contains a Natural Language Processing (NLP) solution for identifying and classifying toxic online comments (such as toxicity, severe toxicity, obscenity, threat, insult, and identity hate).

---

## 📊 Project Overview
* **Objective:** Build a multi-label classification model to evaluate comment toxicity across various categories.
* **Key Steps:**
  * Text cleaning, normalization, and stopword removal pipelines.
  * Vectorization using TF-IDF or text embeddings.
  * Multi-label model training using classification algorithms (e.g., Logistic Regression, Naive Bayes, or LightGBM).
  * Model evaluation via ROC-AUC and precision-recall metrics.
  * Interactive web dashboard deployment via **Streamlit** for real-time comment moderation.

---

## 🛠️ Tech Stack & Libraries
* **Python**
* **Pandas & NumPy** (Data Manipulation)
* **Scikit-Learn** (Vectorization & Multi-label Modeling)
* **Matplotlib & Seaborn** (Data Visualization)
* **Streamlit** (Interactive Dashboard)

---

## 🚀 Getting Started & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tomris17/jigsaw-toxic-comment-classification.git](https://github.com/tomris17/jigsaw-toxic-comment-classification.git)
   cd jigsaw-toxic-comment-classification
