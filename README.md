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

---

## 🛠 Installation

1. **Clone the repository**  
```bash
git clone https://github.com/YourUsername/movie-review-analyzer.git
cd movie-review-analyzer

2. **Install dependencies**

bash
Копировать
Редактировать
pip install -r requirements.txt

▶ Usage
Run the program:

bash
Копировать
Редактировать
python main.py
Example session:

bash
Копировать
Редактировать
Введите новый отзыв для анализа (или 'exit' для выхода): Отличный сюжет, шикарная игра актёров
Отзыв от: зритель
Оценка фильма по 10-бальной шкале: 9

| Review                          | Source  | Rating |
| ------------------------------- | ------- | ------ |
| Отлично снято, шикарный сюжет   | зритель | 10     |
| Скучный и нудный фильм          | критик  | 3      |
| Мой любимый фильм, супер актёры | зритель | 9      |
| Ужасно, плохой сюжет            | критик  | 2      |
