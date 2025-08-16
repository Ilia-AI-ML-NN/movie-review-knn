# 🎬 AI Movie Review Analyzer

**AI-powered CLI tool** that analyzes movie reviews using **KNN** and **TF-IDF**.

It can:
- 🕵️ **Detect** whether the review is written by a **viewer** or a **critic**
- ⭐ **Predict** the movie rating on a **10-point scale**

---

## 📌 Features

- ⚡ **K-Nearest Neighbors (KNN)** classification  
- ✍ **TF-IDF** text vectorization  
- 🎯 Two independent models:  
  - Source classifier (**viewer** / **critic**)  
  - Rating classifier (**1–10**)  
- 💾 **Model persistence** with `joblib` (no retraining every run)  
- 🖥 **Interactive CLI** input for real-time analysis  
- 🎨 **Color-coded output** for readability  

